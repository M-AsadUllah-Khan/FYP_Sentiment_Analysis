import streamlit as st
import sqlite3
import time
import re  # ADDED: For password validation
from layout import render_header, render_footer

def init_db():
    conn = sqlite3.connect('fyp_database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT UNIQUE, first_name TEXT, last_name TEXT, password TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS usage (email TEXT UNIQUE, total INTEGER, positive INTEGER, negative INTEGER, neutral INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS history (email TEXT, review TEXT, sentiment TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)')
    conn.commit()
    conn.close()

def check_persistent_login():
    if not st.session_state.get('logged_in', False):
        if 'auth_email' in st.query_params:
            email = st.query_params['auth_email']
            conn = sqlite3.connect('fyp_database.db')
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE email=?', (email,))
            user = c.fetchone()
            conn.close()
            if user:
                st.session_state['logged_in'] = True
                st.session_state['user_email'] = user[0] 
                st.session_state['last_name'] = user[2]
                st.session_state['page'] = 'dashboard'

def render_auth_ui():
    check_persistent_login()
    
    if st.session_state.get('logged_in', False):
        st.session_state['page'] = 'dashboard'
        st.rerun()

    render_header()
    init_db()
    
    col1, col2, col3 = st.columns([2.5, 5, 2.5])
    
    with col2:
        st.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>🔐 Secure Access Portal</h2>", unsafe_allow_html=True)
        t1, t2 = st.tabs(["🔑 Login", "📝 Register"])

        with t1:
            with st.form("login_form"):
                email_login = st.text_input("Email *")
                p = st.text_input("Password *", type="password")
                
                if st.form_submit_button("AUTHORIZE CONNECTION", type="primary", use_container_width=True):
                    if not email_login or not p:
                        st.warning("⚠️ Both Email and Password are required.")
                    else:
                        conn = sqlite3.connect('fyp_database.db')
                        c = conn.cursor()
                        c.execute('SELECT * FROM users WHERE email=? AND password=?', (email_login, p))
                        user = c.fetchone()
                        conn.close()
                        
                        if user:
                            with st.spinner("Establishing Secure Connection..."): time.sleep(1)
                            st.session_state['logged_in'] = True
                            st.session_state['user_email'] = user[0] 
                            st.session_state['last_name'] = user[2]
                            st.session_state['page'] = 'dashboard'
                            st.query_params['auth_email'] = user[0]
                            st.rerun()
                        else:
                            st.error("⚠️ Incorrect Email or Password!")

        with t2:
            with st.form("register_form"):
                fn = st.text_input("First Name *")
                ln = st.text_input("Last Name *")
                email_reg = st.text_input("Email *")
                pw = st.text_input("Password *", type="password")
                cp = st.text_input("Confirm Password *", type="password")
                
                if st.form_submit_button("INITIALISE PROFILE", type="primary", use_container_width=True):
                    if not all([fn, ln, email_reg, pw, cp]):
                        st.warning("⚠️ Please fill in all mandatory fields.")
                    elif pw != cp:
                        st.error("⚠️ Passwords do not match!")
                    elif len(pw) < 8 or not re.search(r"[A-Z]", pw) or not re.search(r"[!@#$%^&*(),.?\":{}|<>]", pw):
                        st.error("⚠️ Password must be at least 8 characters long, contain at least 1 Uppercase letter, and 1 Special character.")
                    else:
                        try:
                            conn = sqlite3.connect('fyp_database.db')
                            c = conn.cursor()
                            c.execute('INSERT INTO users VALUES (?, ?, ?, ?)', (email_reg, fn, ln, pw))
                            c.execute('INSERT INTO usage VALUES (?, 0, 0, 0, 0)', (email_reg,))
                            conn.commit()
                            conn.close()
                            st.success("✅ Profile established permanently in Database! Please switch to Login tab.")
                        except sqlite3.IntegrityError:
                            st.error("⚠️ This Email is already registered! Only one account per email is allowed.")
                            conn.close()
                            
    render_footer()
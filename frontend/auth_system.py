import streamlit as st
import psycopg2
import time
import re
import random
import smtplib
import os 
from email.mime.text import MIMEText
from layout import render_header, render_footer

DB_URL = os.environ.get("DB_URL") or st.secrets.get("DB_URL")
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
APP_PASSWORD = os.environ.get("APP_PASSWORD")

def get_db_connection():
    return psycopg2.connect(DB_URL)


@st.cache_resource
def init_db():
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS users (email TEXT UNIQUE, first_name TEXT, last_name TEXT, password TEXT)')
        c.execute('CREATE TABLE IF NOT EXISTS usage (email TEXT UNIQUE, total INTEGER, positive INTEGER, negative INTEGER, neutral INTEGER)')
        c.execute('CREATE TABLE IF NOT EXISTS history (email TEXT, review TEXT, sentiment TEXT, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)')
        conn.commit()
        conn.close()
    except Exception as e:
        st.error(f"Database Init Error: {e}")

def send_otp_email(receiver_email, otp_code, purpose="Registration"):
    try:
        msg = MIMEText(f"""Your OTP for Secure Access Portal {purpose} is: <span style="text-align:center;font-weight:800px;font-size:16px;">{otp_code}</span>\n\nPlease enter this code to verify your action.""")
        msg['Subject'] = f'{purpose} OTP - AI Sentiments Analysis System'
        msg['From'] = SENDER_EMAIL
        msg['To'] = receiver_email

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print("Email Error:", e)
        return False

def check_persistent_login():
    if not st.session_state.get('logged_in', False):
        if 'auth_email' in st.query_params:
            email = st.query_params['auth_email']
            try:
                conn = get_db_connection()
                c = conn.cursor()
                c.execute('SELECT * FROM users WHERE email=%s', (email,))
                user = c.fetchone()
                conn.close()
                if user:
                    st.session_state['logged_in'] = True
                    st.session_state['user_email'] = user[0] 
                    st.session_state['last_name'] = user[2]
                    st.session_state['page'] = 'dashboard'
            except:
                pass

def render_auth_ui():
    check_persistent_login()
    
    if st.session_state.get('logged_in', False):
        st.session_state['page'] = 'dashboard'
        st.rerun()

    if 'otp_step' not in st.session_state: st.session_state['otp_step'] = False
    if 'temp_user_data' not in st.session_state: st.session_state['temp_user_data'] = None
    if 'generated_otp' not in st.session_state: st.session_state['generated_otp'] = None
    if 'rec_step' not in st.session_state: st.session_state['rec_step'] = 'start'
    if 'rec_email' not in st.session_state: st.session_state['rec_email'] = None
    if 'rec_otp' not in st.session_state: st.session_state['rec_otp'] = None

    render_header()
    init_db() 
    
    col1, col2, col3 = st.columns([2.5, 5, 2.5])
    
    with col2:
        st.markdown("<h2 style='text-align: center; margin-bottom: 20px;'>🔐 Secure Access Portal</h2>", unsafe_allow_html=True)
        
        t1, t2, t3 = st.tabs(["🔑 Login", "📝 Register", "🔄 Recover"])

        with t1:
            with st.form("login_form"):
                email_login = st.text_input("Email *")
                p = st.text_input("Password *", type="password")
                
                if st.form_submit_button("AUTHORIZE CONNECTION", type="primary", use_container_width=True):
                    if not email_login or not p:
                        st.warning("⚠️ Both Email and Password are required.")
                    else:
                        try:
                            conn = get_db_connection()
                            c = conn.cursor()
                            c.execute('SELECT * FROM users WHERE email=%s AND password=%s', (email_login, p))
                            user = c.fetchone()
                            conn.close()
                            
                            if user:
                                st.session_state['logged_in'] = True
                                st.session_state['user_email'] = user[0] 
                                st.session_state['last_name'] = user[2]
                                st.session_state['page'] = 'dashboard'
                                st.query_params['auth_email'] = user[0]
                                st.rerun()
                            else:
                                st.error("⚠️ Incorrect Email or Password!")
                        except Exception as e:
                            st.error(f"Login Error: {e}")

        with t2:
            if not st.session_state['otp_step']:
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
                                conn = get_db_connection()
                                c = conn.cursor()
                                c.execute('SELECT * FROM users WHERE email=%s', (email_reg,))
                                existing_user = c.fetchone()
                                conn.close()

                                if existing_user:
                                    st.error("⚠️ This Email is already registered! PLease register with another Email.")
                                else:
                                    with st.spinner("Generating OTP and sending to your email..."):
                                        otp = str(random.randint(100000, 999999))
                                        if send_otp_email(email_reg, otp, "Registration"):
                                            st.session_state['temp_user_data'] = (email_reg, fn, ln, pw)
                                            st.session_state['generated_otp'] = otp
                                            st.session_state['otp_step'] = True
                                            st.rerun()
                                        else:
                                            st.error("⚠️ Failed to send OTP. Please check your network.")
                            except Exception as e:
                                st.error(f"Registration Error: {e}")

            else:
                st.info(f"📧 A 6-digit OTP has been sent to **{st.session_state['temp_user_data'][0]}**")
                with st.form("otp_form"):
                    entered_otp = st.text_input("Enter OTP Code *", max_chars=6)
                    col_a, col_b = st.columns(2)
                    with col_a:
                        verify_btn = st.form_submit_button("VERIFY & REGISTER", type="primary", use_container_width=True)
                    with col_b:
                        cancel_btn = st.form_submit_button("Cancel", use_container_width=True)

                    if verify_btn:
                        if entered_otp == st.session_state['generated_otp']:
                            try:
                                user_data = st.session_state['temp_user_data']
                                conn = get_db_connection()
                                c = conn.cursor()
                                c.execute('INSERT INTO users VALUES (%s, %s, %s, %s)', user_data)
                                c.execute('INSERT INTO usage VALUES (%s, 0, 0, 0, 0)', (user_data[0],))
                                conn.commit()
                                conn.close()
                                
                                st.session_state['otp_step'] = False
                                st.session_state['temp_user_data'] = None
                                st.session_state['generated_otp'] = None
                                
                                st.success("✅ Profile established securely! You can now log in.")
                            except Exception as e:
                                st.error(f"Database Error: {e}")
                        else:
                            st.error("⚠️ Incorrect OTP! Please try again.")
                            
                    if cancel_btn:
                        st.session_state['otp_step'] = False
                        st.session_state['temp_user_data'] = None
                        st.session_state['generated_otp'] = None
                        st.rerun()

        with t3:
            st.markdown("<h4 style='text-align: center; margin-bottom: 15px;'>Account Recovery</h4>", unsafe_allow_html=True)
            
            if st.session_state['rec_step'] == 'start':
                with st.form("recover_email_form"):
                    st.write("Enter your registered email to receive a recovery OTP.")
                    rec_email_input = st.text_input("Recovery Email")
                    submit_recover = st.form_submit_button("Send Recovery OTP", type="primary", use_container_width=True)
                    
                    if submit_recover:
                        if rec_email_input:
                            try:
                                conn = get_db_connection()
                                c = conn.cursor()
                                c.execute('SELECT * FROM users WHERE email=%s', (rec_email_input,))
                                existing_user = c.fetchone()
                                conn.close()
                                
                                if existing_user:
                                    with st.spinner("Sending Recovery OTP..."):
                                        otp = str(random.randint(100000, 999999))
                                        if send_otp_email(rec_email_input, otp, "Account Recovery"):
                                            st.session_state['rec_email'] = rec_email_input
                                            st.session_state['rec_otp'] = otp
                                            st.session_state['rec_step'] = 'otp'
                                            st.rerun()
                                        else:
                                            st.error("⚠️ Failed to send OTP. Try again.")
                                else:
                                    st.error("⚠️ Email not found in our database.")
                            except Exception as e:
                                st.error(f"Recovery Error: {e}")
                        else:
                            st.warning("Please enter your email.")
                            
            elif st.session_state['rec_step'] == 'otp':
                st.info(f"📧 Recovery OTP sent to **{st.session_state['rec_email']}**")
                with st.form("recover_otp_form"):
                    entered_rec_otp = st.text_input("Enter 6-digit OTP", max_chars=6)
                    col_x, col_y = st.columns(2)
                    with col_x:
                        verify_rec_btn = st.form_submit_button("Verify OTP", type="primary", use_container_width=True)
                    with col_y:
                        cancel_rec_btn = st.form_submit_button("Cancel Recovery", use_container_width=True)
                        
                    if verify_rec_btn:
                        if entered_rec_otp == st.session_state['rec_otp']:
                            st.session_state['rec_step'] = 'reset'
                            st.rerun()
                        else:
                            st.error("⚠️ Incorrect OTP!")
                            
                    if cancel_rec_btn:
                        st.session_state['rec_step'] = 'start'
                        st.rerun()
                        
            elif st.session_state['rec_step'] == 'reset':
                st.success("✅ Identity Verified! Set a new password.")
                with st.form("reset_password_form"):
                    new_pw = st.text_input("New Password *", type="password")
                    conf_new_pw = st.text_input("Confirm New Password *", type="password")
                    update_btn = st.form_submit_button("Update Password", type="primary", use_container_width=True)
                    
                    if update_btn:
                        if new_pw != conf_new_pw:
                            st.error("⚠️ Passwords do not match!")
                        elif len(new_pw) < 8 or not re.search(r"[A-Z]", new_pw) or not re.search(r"[!@#$%^&*(),.?\":{}|<>]", new_pw):
                            st.error("⚠️ Minimum 8 characters, 1 Uppercase, 1 Special character required.")
                        else:
                            try:
                                conn = get_db_connection()
                                c = conn.cursor()
                                c.execute("UPDATE users SET password = %s WHERE email = %s", (new_pw, st.session_state['rec_email']))
                                conn.commit()
                                conn.close()
                                
                                st.session_state['rec_step'] = 'start'
                                st.success("✅ Password updated successfully! Please switch to Login tab.")
                            except Exception as e:
                                st.error(f"Password Update Error: {e}")

    render_footer()
import streamlit as st
from auth_system import render_auth_ui
from dashboards import render_user_dashboard
from intro_page import render_intro_page
from auth_system import check_persistent_login

check_persistent_login()

# ==========================================
st.set_page_config(page_title="FYP | Sentiment Analysis", page_icon="📊", layout="wide")

# ==========================================
# 2. SESSION STATE & DYNAMIC DATA INIT
# ==========================================
if 'page' not in st.session_state:
    st.session_state['page'] = 'intro'
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

# Dashboard Live Counters & Chart Memory
if 'total_count' not in st.session_state:
    st.session_state['total_count'] = 2450
    st.session_state['pos_count'] = 1592
    st.session_state['neg_count'] = 490
    st.session_state['neu_count'] = 368
    st.session_state['chart_history'] = {
        "Mon": {"pos": 120, "neg": 40, "neu": 20},
        "Tue": {"pos": 130, "neg": 45, "neu": 25},
        "Wed": {"pos": 150, "neg": 30, "neu": 20},
        "Thu": {"pos": 110, "neg": 50, "neu": 30},
        "Fri": {"pos": 180, "neg": 20, "neu": 10},
        "Sat": {"pos": 200, "neg": 15, "neu": 15},
        "Today": {"pos": 0, "neg": 0, "neu": 0} 
    }

# ==========================================

if st.query_params.get("logged_in") == "true":
    st.session_state['logged_in'] = True
    st.session_state['username'] = st.query_params.get("user", "User")
    st.session_state['last_name'] = st.query_params.get("last_name", "User")
    st.session_state['page'] = 'dashboard'

# ==========================================
# 4. GLOBAL ROUTING SYSTEM
# ==========================================
if st.session_state['logged_in'] and st.session_state['page'] == 'dashboard':
    render_user_dashboard()
elif st.session_state['page'] == 'login':
    render_auth_ui()
else:
    render_intro_page()
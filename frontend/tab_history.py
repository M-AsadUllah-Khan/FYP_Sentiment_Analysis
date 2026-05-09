import streamlit as st
import sqlite3
import pandas as pd

def get_user_history(email):
    conn = sqlite3.connect('fyp_database.db')
    df = pd.read_sql_query("SELECT review as 'Review Text', sentiment as 'Prediction', timestamp as 'Date/Time' FROM history WHERE email=? ORDER BY timestamp DESC", conn, params=(email,))
    conn.close()
    return df

def render_history_tab():
    user_email = st.session_state.get('user_email', 'Unknown')
    st.markdown("### Your Complete Work History")
    
    history_df = get_user_history(user_email)
    
    if not history_df.empty:
        st.dataframe(history_df, use_container_width=True, hide_index=True)
    else:
        st.info("Your database history is currently empty. Run some tests in the 'Manual Review' or 'Bulk Search' tabs to see your history here.")
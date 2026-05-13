import streamlit as st
import psycopg2
import pandas as pd

def get_user_history(email):
    conn = psycopg2.connect(st.secrets["DB_URL"])
    
    query = 'SELECT review as "Review Text", sentiment as "Prediction", timestamp as "Date/Time" FROM history WHERE email=%s ORDER BY timestamp DESC'
    
    df = pd.read_sql_query(query, conn, params=(email,))
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
import streamlit as st
import psycopg2
import pandas as pd
import time
import sys
import os

# --- REAL NLP ENGINE INTEGRATION ---
try:
    from backend.nlp_engine import analyze_sentiment
except ModuleNotFoundError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from backend.nlp_engine import analyze_sentiment

# --- DB FETCH LOGIC ---
def get_user_usage(email):
    conn = psycopg2.connect(os.environ["DB_URL"])
    c = conn.cursor()
    c.execute('SELECT total, positive, negative, neutral FROM usage WHERE email=%s', (email,))
    data = c.fetchone()
    conn.close()
    return data if data else (0, 0, 0, 0)

# --- DB LOGIC ---
def update_user_usage_and_history(email, text, result):
    tot, pos, neg, neu = get_user_usage(email)
    tot += 1
    if result == "POSITIVE": pos += 1
    elif result == "NEGATIVE": neg += 1
    else: neu += 1
    
    conn = psycopg2.connect(st.secrets["DB_URL"])
    c = conn.cursor()
    c.execute('UPDATE usage SET total=%s, positive=%s, negative=%s, neutral=%s WHERE email=%s', (tot, pos, neg, neu, email))
    c.execute('INSERT INTO history (email, review, sentiment) VALUES (%s, %s, %s)', (email, text, result))
    conn.commit()
    conn.close()

# --- THE MAIN DASHBOARD FUNCTION ---
def render_performance_and_manual():
    user_email = st.session_state.get('user_email', 'Unknown')
    tot, pos, neg, neu = get_user_usage(user_email)

    # 1. Performance Metrics Section
    st.markdown(f"### System Telemetry")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Analysed", str(tot))
    m2.metric("Positive", f"{round((pos/tot)*100,1)}%" if tot > 0 else "0%")
    m3.metric("Negative", f"{round((neg/tot)*100,1)}%" if tot > 0 else "0%")
    m4.metric("Neutral", f"{round((neu/tot)*100,1)}%" if tot > 0 else "0%")
    
    st.divider()
    if tot > 0:
        df_chart = pd.DataFrame({"Sentiment": ["Positive", "Negative", "Neutral"], "Count": [pos, neg, neu]})
        st.bar_chart(df_chart.set_index("Sentiment"), color="#3b82f6")
    else:
        st.info("No data analysed yet. Test a review below.")

    st.markdown("---")
    
    # 2. Manual Review Section
    st.markdown("### Test Individual Reviews")
    user_input = st.text_area("Enter Review Text:", height=150)
    
    if st.button("Run Model", type="primary"):
        if user_input:
            with st.spinner("Data Analysing..."): 
                time.sleep(0.5) 
            
            # --- CALLING YOUR REAL NLP ENGINE ---
            category, compound, raw_scores = analyze_sentiment(user_input)
            res = category.upper()
            
            # Backend Database
            update_user_usage_and_history(user_email, user_input, res)
            
            clr = "green" if res=="POSITIVE" else "red" if res=="NEGATIVE" else "orange"
            st.markdown(f"<div style='border:2px solid {clr}; padding:20px; border-radius:10px; text-align:center;'><h3>Detected: {res}</h3><p style='margin:0; opacity:0.8;'>Confidence (Compound Score): {round(compound, 3)}</p></div>", unsafe_allow_html=True)
            st.success("✅ Dashboard Metrics Updated in Backend Successfully!")
            time.sleep(1.5)
            st.rerun()
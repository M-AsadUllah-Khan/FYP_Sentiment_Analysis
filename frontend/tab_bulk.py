import streamlit as st
import pandas as pd
import time
import sys
import os

try:
    from backend.nlp_engine import analyze_sentiment
except ModuleNotFoundError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from backend.nlp_engine import analyze_sentiment

def render_bulk_tab():
    st.markdown("### 📁 Bulk Data Processing Pipeline")
    st.info("Upload a CSV file with a column named 'review' to process using VADER.")

    uploaded_file = st.file_uploader("Upload CSV Dataset", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        
        if 'review' in df.columns:
            if st.button("Process Batch Data", type="primary"):
                with st.spinner("Neural Engine is processing rows..."):
                    results = []
                    # Processing each row realistically
                    for text in df['review'].astype(str):
                        category, compound, _ = analyze_sentiment(text)
                        results.append(category.upper())
                    
                    df['Sentiment_Result'] = results
                    time.sleep(1)
                
                st.success(f"✅ Processed {len(df)} reviews successfully!")
                
                # Dynamic Metrics based on REAL data
                pos_count = results.count("POSITIVE")
                neg_count = results.count("NEGATIVE")
                neu_count = results.count("NEUTRAL")
                
                c1, c2, c3 = st.columns(3)
                c1.metric("Positive", f"{pos_count}")
                c2.metric("Negative", f"{neg_count}")
                c3.metric("Neutral", f"{neu_count}")
                
                st.dataframe(df, use_container_width=True)
        else:
            st.error("⚠️ CSV must contain a column named 'review'.")
import streamlit as st
import time
import random
import string
from ai_engine import predict_sentiment, extract_aspects, get_quantum_gauge

def render_realtime_tab(ai_threshold): # AI Threshold passed here!
    st.markdown("### Real-Time Inference Scanner")
    user_input = st.text_area("Input Review Text:", height=100)
    
    if st.button("Run Classification", type="primary"):
        if user_input.strip() == "":
            st.warning("Please provide input text.")
        else:
            st.session_state['total_count'] += 1
            scan_placeholder = st.empty()
            
            # Animation
            animated_text = ""
            for w in user_input.split():
                hx = ''.join(random.choices(string.hexdigits.upper(), k=4))
                animated_text += f" <span style='color:var(--text-color); opacity:0.8;'>{w}</span>"
                scan_placeholder.markdown(f"<div style='background:var(--secondary-background-color); padding:15px; border-radius:8px; border:1px solid rgba(59,130,246,0.3);'>{animated_text} <span class='hex-token'>0x{hx}</span></div>", unsafe_allow_html=True)
                time.sleep(0.05)
                
            sentiment, confidence, icon, color_class, hex_color = predict_sentiment(user_input, ai_threshold)
            
            if sentiment == "POSITIVE": 
                st.session_state['pos_count'] += 1
                st.session_state['chart_history']['Today']['pos'] += 1
            elif sentiment == "NEGATIVE": 
                st.session_state['neg_count'] += 1
                st.session_state['chart_history']['Today']['neg'] += 1
            else: 
                st.session_state['neu_count'] += 1
                st.session_state['chart_history']['Today']['neu'] += 1

            aspects = extract_aspects(user_input)
            aspect_html = ""
            if aspects:
                aspect_html += "<div style='margin-top: 15px; border-top: 1px dashed rgba(128,128,128,0.2); padding-top:10px; text-align:center;'>"
                for aspect, pol in aspects.items():
                    dot_color = "#10b981" if pol == "POSITIVE" else "#ef4444"
                    aspect_html += f"<span class='aspect-badge'><span style='color:{dot_color}; font-size:16px;'>•</span> {aspect}</span>"
                aspect_html += "</div>"

            svg_gauge = get_quantum_gauge(confidence, hex_color)

            st.markdown(f"""
                <div class="result-card">
                    <div style="text-align: center;">
                        <h3 style="margin:0; color:{hex_color}; text-shadow: 0 0 10px {hex_color}80;">{icon} {sentiment}</h3>
                    </div>
                    {svg_gauge}
                    {aspect_html}
                </div>
            """, unsafe_allow_html=True)
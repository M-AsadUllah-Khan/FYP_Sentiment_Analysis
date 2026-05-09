import streamlit as st
from layout import render_header, render_footer

# Importing your modular tab components
from tab_dashboard import render_performance_and_manual  # Ensure this file contains your Metrics/Manual review logic
from tab_bulk import render_bulk_tab                     # Ensure this file contains your Bulk processing logic
from tab_comparison import render_comparison_tab         # Ensure this file contains your Comparison logic
from tab_history import render_history_tab               # The new history file we just created

def render_user_dashboard():
    render_header()
    
    st.markdown("<div class='main-content-fade'>", unsafe_allow_html=True)
    
    # Setup Tabs
    t1, t2, t3, t4 = st.tabs([
        "📊 Dashboard & Testing", 
        "📁 Bulk Data Search", 
        "⚖️ Product Comparison", 
        "🕒 Testing History"
    ])

    # Routing to your modular files
    with t1:
        render_performance_and_manual()
        
    with t2:
        render_bulk_tab()
        
    with t3:
        render_comparison_tab()
        
    with t4:
        render_history_tab()

    st.markdown("</div>", unsafe_allow_html=True)
    render_footer()
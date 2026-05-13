import streamlit as st
import os
import base64
from layout import render_header, render_footer

def render_intro_page():
    render_header()
    
    # Custom CSS for Intro Page
    st.markdown("""
        <style>
            .main-content-fade {
                animation: fadeUp 1s ease-out forwards;
                opacity: 0;
                transform: translateY(20px);
            }
            @keyframes fadeUp {
                to { opacity: 1; transform: translateY(0); }
            }
            .intro-hero { padding: 20px 0 20px 0; z-index: 3; position: relative; display: flex; flex-direction: column; align-items: center; }
            .hero-title { font-size: 3.5rem; font-weight: 900; text-align: center; width: 100%; margin-bottom: 15px; }
            
            .profile-img-container {
                width: 100%;
                display: flex;
                justify-content: center;
                margin-bottom: 20px;
            }
            .profile-img {
                width: 100%;
                border-radius: 20px;
                box-shadow: 0 8px 25px rgba(59, 130, 246, 0.4);
                border: 2px solid rgba(59, 130, 246, 0.6);
                pointer-events: none;
                transition: transform 0.3s ease;
            }
            .profile-img:hover { transform: scale(1.02); }
            
            .skill-text { font-size: 13px; font-weight: 700; margin-bottom: 4px; display: flex; justify-content: space-between; color: #3b82f6; }
            .skill-bar-bg { background: rgba(128, 128, 128, 0.15); height: 10px; border-radius: 5px; margin-bottom: 18px; overflow: hidden; position: relative; }
            .skill-bar-fill { 
                background: linear-gradient(90deg, #3b82f6, #8b5cf6); height: 100%; border-radius: 5px;
                box-shadow: 0 0 10px rgba(59, 130, 246, 0.5); 
                animation: skillFill 2s cubic-bezier(0.1, 1, 0.2, 1) forwards; transform-origin: left; width: 0%; 
            }
            @keyframes skillFill { from { width: 0%; } to { width: var(--target-width); } }
            
            .contact-card { background: rgba(128, 128, 128, 0.05); border-left: 3px solid #3b82f6; padding: 20px; border-radius: 0 15px 15px 0; margin-top: 10px; }
            .contact-item { font-size: 14px; margin-bottom: 8px; display: flex; align-items: center; gap: 10px; opacity: 0.9; }

            .feature-card {
                background: rgba(128, 128, 128, 0.05);
                border: 1px solid rgba(59, 130, 246, 0.2);
                border-radius: 15px;
                padding: 20px;
                margin-bottom: 20px;
                height: 210px;
                display: flex;
                flex-direction: column;
                transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                animation: fadeUp 0.8s ease-out forwards;
                opacity: 0;
                transform: translateY(30px);
            }
            .feature-card:hover {
                transform: translateY(-8px);
                box-shadow: 0 12px 25px rgba(59, 130, 246, 0.25);
                border-color: rgba(59, 130, 246, 0.7);
                background: rgba(59, 130, 246, 0.05);
            }
            .card-icon { font-size: 32px; margin-bottom: 15px; display: inline-block; animation: floatIcon 3s ease-in-out infinite; filter: drop-shadow(0 4px 6px rgba(0,0,0,0.2)); }
            @keyframes floatIcon { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-5px); } }
            .card-title { font-size: 1.25rem; font-weight: 800; margin-bottom: 10px; color: var(--text-color); }
            .card-text { font-size: 0.95rem; opacity: 0.85; line-height: 1.5; margin: 0; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='main-content-fade'>", unsafe_allow_html=True)
    
    st.markdown("<div class='intro-hero'>", unsafe_allow_html=True)
    st.markdown("<h1 class='hero-title'>Intelligence Beyond <span style='color: #3b82f6;'>Words</span></h1>", unsafe_allow_html=True)
    
    st.markdown("""
        <div style='display: flex; justify-content: center; width: 100%; margin-bottom: 25px;'>
            <div style='max-width: 850px; width: 100%;'>
                <p style='font-size: 1.15rem; opacity: 0.85; text-align: justify; line-height: 1.7; margin: 0;'>
                    Reading thousands of customer reviews manually is nearly impossible for any business. To solve this practical problem, I developed this AI SENTIMENTS ANALYSIS SYSTEM. As my Capstone Project, the <b>NATURAL LANGUAGE PROCESSING (NLP) SYSTEM</b> automates sentiment analysis, decoding complex human emotions into actionable strategic metrics. By identifying underlying patterns in e-commerce feedback, it empowers businesses to optimise product development and proactively enhance customer satisfaction.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Symmetry ensured by parent layout CSS for primary button
    if st.button("🚀 ACCESS LIVE SYSTEM", type="primary", use_container_width=True):
        st.session_state['page'] = 'login'
        st.rerun()
    st.markdown("</div><br>", unsafe_allow_html=True)

    # Animated Feature Cards
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
            <div class='feature-card' style='animation-delay: 0.1s;'>
                <div class='card-icon'>📈</div>
                <div class='card-title'>Data Visualization</div>
                <p class='card-text'>Real-time telemetry update processing live review shifts.</p>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
            <div class='feature-card' style='animation-delay: 0.3s;'>
                <div class='card-icon'>🗂️</div>
                <div class='card-title'>Neural Pipeline</div>
                <p class='card-text'>Scalable batch processing for large-scale e-commerce datasets.</p>
            </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
            <div class='feature-card' style='animation-delay: 0.5s;'>
                <div class='card-icon'>🔬</div>
                <div class='card-title'>Inference Logic</div>
                <p class='card-text'>Context-aware sentiment classification with high confidence rates.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # Developer details section
    col_left, col_spacer, col_right = st.columns([0.85, 0.15, 2.0])
    
    with col_left:
        # Dynamic Absolute Path for Image (Fix - Goal Intro)
        # Assuming app runs from project root. This ensures paths like intro_page.py working.
        base_dir = os.path.dirname(os.path.abspath(__file__)) # F:/FYP.../frontend/
        project_root = os.path.dirname(base_dir) # F:/FYP.../
        img_relative_path = os.path.join("assets", "images", "asad.jpeg")
        
        # Test paths
        img_abs_path1 = os.path.join(base_dir, img_relative_path) 
        img_abs_path2 = os.path.join(project_root, img_relative_path) #

        # Main dynamic loader with fallbacks
        encoded_string = None
        loaded_path = ""
        
        potential_paths = [
            img_abs_path2, # Priority 1 (Correct structure)
            "assets/images/asad.jpeg", # Streamlit runs from root
            os.path.join("assets", "images", "asad.jpeg"), # Cross-platformStreamlit Runs
            img_abs_path1, # Fallback
            "assets/images/placeholder.png" # Safe fallback image path
        ]

        for p in potential_paths:
            try:
                if os.path.exists(p) and os.path.isfile(p):
                    with open(p, "rb") as image_file:
                        encoded_string = base64.b64encode(image_file.read()).decode()
                        loaded_path = p
                        break
            except Exception as e:
                continue

        if encoded_string:
            st.markdown(f'<div class="profile-img-container"><img src="data:image/jpeg;base64,{encoded_string}" class="profile-img"></div>', unsafe_allow_html=True)
        else:
            # Fallback placeholder circle if image fails completely
            st.markdown("""
                <div class='profile-img-container'>
                    <div style='width:100%; aspect-ratio:1; border-radius:20px; background:#1e293b; display:flex; justify-content:center; align-items:center; border:2px solid rgba(59,130,246,0.6);'>
                        👨‍💻
                    </div>
                </div>
                """, unsafe_allow_html=True)
            
        # Skills bars below image
        st.markdown("<h4 style='margin-top:25px; color:#3b82f6; text-align:center;'>Technical Expertise</h4>", unsafe_allow_html=True)
        skills = [("HTML 5", "95%"), ("CSS", "90%"), ("JavaScript", "85%"), ("Python", "90%"), ("AI Specialist", "85%")]
        for name, perc in skills:
            st.markdown(f"<div class='skill-text'><span>{name}</span><span>{perc}</span></div><div class='skill-bar-bg'><div class='skill-bar-fill' style='--target-width: {perc};'></div></div>", unsafe_allow_html=True)

    with col_right:
        # About & Contact Details
        st.markdown(f"""
            <h1 style='margin-bottom:0px; color:var(--text-color);'>Muhammad Asad Ullah</h1>
            <p style='color:#3b82f6; font-weight:600; font-size:18px; margin-top:5px;'>Bachelor of Science in Computer Science (GCUF)</p>
            <div style='margin-bottom:20px; font-style:italic; opacity:0.8;'>Leading Web Developer | AI-Driven Engineer</div>
            
            <div class='contact-card'>
                <div class='contact-item'>📧 <b>Email:</b> asaddevpk@gmail.com</div>
                <div class='contact-item'>📱 <b>WhatsApp:</b> +92 325 0404096</div>
                <div class='contact-item'>📍 <b>Location:</b> Faisalabad, Pakistan</div>
            </div>
            
            <h3 style='margin-top:30px; color:#3b82f6; border-bottom:1px solid rgba(59,130,246,0.3); padding-bottom:10px;'>About The Project</h3>
            <p style='text-align:justify; line-height:1.7; opacity:0.85;'>I am a passionate Full-Stack Developer and AI specialist. This <b>AI SENTIMENTS ANALYSIS SYSTEM</b> is my Capstone Project, designed to automate sentiment analysis in the e-commerce sector. I independently engineered the entire pipeline—from the high-performance NLP algorithms to this interactive dashboard—ensuring a seamless blend of data science and premium user experience.</p>
            
            <p style='text-align:justify; line-height:1.7; opacity:0.85; margin-top: 15px;'><b style='color: #3b82f6;'>Why I Selected This Project:</b><br>In today's digital era, e-commerce businesses are overwhelmed by thousands of customer reviews. Manually reading and extracting meaningful insights from this massive unstructured data is practically impossible. I chose this project to solve this real-world bottleneck by leveraging Artificial Intelligence to decode human emotions accurately at scale.</p>

            <p style='text-align:justify; line-height:1.7; opacity:0.85; margin-top: 15px;'><b style='color: #3b82f6;'>Key Benefits & Impact:</b><br>This application empowers businesses to instantly gauge customer satisfaction, identify critical product flaws, and discover market trends. By transforming raw text into visual, actionable metrics, it enables companies to make data-driven decisions, proactively improve their services, and ultimately drive higher customer retention and sales.</p>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True) # close fade Up div
    render_footer()
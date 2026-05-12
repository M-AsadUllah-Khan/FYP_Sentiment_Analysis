import streamlit as st
import datetime
import time


def inject_global_styles():
    if "theme" not in st.session_state:
        st.session_state["theme"] = "dark"

    is_dark = st.session_state["theme"] == "dark"
    bg = "#0f172a" if is_dark else "#f8fafc"
    text = "#ffffff" if is_dark else "#0f172a"
    accent = "#3b82f6"
    card_bg = "rgba(30, 41, 59, 0.85)" if is_dark else "rgba(255, 255, 255, 0.95)"
    border = "rgba(59, 130, 246, 0.5)"

    footer_bg = (
        "linear-gradient(135deg, rgba(30, 41, 59, 0.75), rgba(15, 23, 42, 0.9))"
        if is_dark
        else "linear-gradient(135deg, rgba(255, 255, 255, 0.8), rgba(241, 245, 249, 0.95))"
    )
    footer_text = "#e2e8f0" if is_dark else "#334155"
    footer_shadow = "rgba(0, 0, 0, 0.4)" if is_dark else "rgba(148, 163, 184, 0.3)"

    st.markdown(
        f"""
        <style>
            div[data-testid="InputInstructions"] {{ display: none !important; }}
            .stApp {{ background-color: {bg}; background-image: radial-gradient(rgba(59, 130, 246, {0.15 if is_dark else 0.1}) 2px, transparent 2px), radial-gradient(rgba(139, 92, 246, {0.15 if is_dark else 0.1}) 2px, transparent 2px); background-size: 60px 60px; background-position: 0 0, 30px 30px; animation: moveBg 30s linear infinite; transition: background-color 0.5s ease; }}
            @keyframes moveBg {{ 0% {{ background-position: 0 0, 30px 30px; }} 100% {{ background-position: 600px 600px, 630px 630px; }} }}
            [data-testid="stAppViewBlockContainer"], [data-testid="stHorizontalBlock"], .stTabs {{ animation: cinematicTransition 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards; transform-origin: center top; }}
            @keyframes cinematicTransition {{ 0% {{ opacity: 0; transform: translateY(30px) scale(0.97); filter: blur(10px); }} 100% {{ opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }} }}
            .stMarkdown, p, h1, h2, h3, h4, h5, h6 {{ color: {text} !important; }}
            
            /* --- LOCKED BUTTONS --- */
            div.stButton > button {{ 
                background: {card_bg} !important; color: {text} !important; border: 1px solid {border} !important; border-radius: 8px !important; font-weight: bold !important; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); 
                height: 45px !important; margin-top: 0px !important; padding: 0 15px !important; box-sizing: border-box !important;
                display: flex !important; align-items: center !important; justify-content: center !important;
                white-space: nowrap !important; overflow: hidden !important; text-overflow: ellipsis !important;
            }}
            div.stButton > button p {{ white-space: nowrap !important; margin: 0 !important; }}
            div.stButton > button:hover {{ border-color: {accent} !important; box-shadow: 0 0 15px {border} !important; transform: translateY(-3px) scale(1.02); }}
            button[kind="primary"], div[data-testid="stForm"] button {{ background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%) !important; color: white !important; border: none !important; box-shadow: 0 4px 15px rgba(59,130,246,0.3) !important; }}
            button[kind="primary"]:hover, div[data-testid="stForm"] button:hover {{ box-shadow: 0 8px 25px rgba(59,130,246,0.6) !important; }}
            
            .secure-badge-static, .welcome-badge {{ height: 45px !important; display: flex !important; align-items: center !important; justify-content: center !important; margin-top: 0px !important; box-sizing: border-box !important; }}

            /* ========================================================= */
            /* --- ULTRA PRO MAX CYBER HEADER --- */
            /* ========================================================= */
            .cyber-header {{ 
                background: linear-gradient(135deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.85) 50%, rgba(15, 23, 42, 0.95) 100%);
                backdrop-filter: blur(18px); 
                -webkit-backdrop-filter: blur(18px);
                border-top: 1px solid rgba(255, 255, 255, 0.15);
                border-bottom: 2px solid rgba(59, 130, 246, 0.6);
                border-left: 1px solid rgba(59, 130, 246, 0.2);
                border-right: 1px solid rgba(59, 130, 246, 0.2);
                border-radius: 16px; 
                padding: 15px 20px; 
                position: relative; 
                overflow: hidden; 
                animation: float 6s ease-in-out infinite; 
                margin-bottom: 15px; 
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4), inset 0 0 25px rgba(59, 130, 246, 0.05); 
                z-index: 3; 
                transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            }}
            .cyber-header:hover {{ transform: translateY(-3px); box-shadow: 0 20px 45px rgba(0, 0, 0, 0.6), inset 0 0 35px rgba(59, 130, 246, 0.15); }}
            .cyber-header::before {{ content: ''; position: absolute; top: -100%; left: 0; width: 100%; height: 2px; background: linear-gradient(90deg, transparent, #6366f1, #0ea5e9, #6366f1, transparent); animation: cyber-scan 3.5s infinite; }}
            .cyber-header::after {{ content: ''; position: absolute; top: 0; left: -100%; width: 50%; height: 100%; background: linear-gradient(to right, transparent, rgba(255, 255, 255, 0.08), transparent); transform: skewX(-25deg); animation: glass-sweep 7s infinite; pointer-events: none; }}
            @keyframes glass-sweep {{ 0% {{ left: -100%; }} 15% {{ left: 200%; }} 100% {{ left: 200%; }} }}
            @keyframes cyber-scan {{ 0% {{ top: -10%; }} 100% {{ top: 110%; }} }}
            @keyframes float {{ 0%, 100% {{ transform: translateY(0px); }} 50% {{ transform: translateY(-6px); }} }}
            
            .header-flex-main {{ display: flex !important; flex-direction: row !important; justify-content: space-between !important; align-items: center !important; width: 100%; flex-wrap: nowrap !important; }}
            .header-left-col {{ flex: 1; display: flex; justify-content: flex-start; align-items: center; padding-left: 20px; }}
            .header-center-col {{ flex: 4; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; gap: 0px !important; }}
            .header-right-col {{ flex: 1; display: flex; justify-content: flex-end; align-items: center; padding-right: 15px; }}
            
            .glow-text {{ font-family: 'Segoe UI', system-ui, sans-serif; font-weight: 900; background: linear-gradient(to right, #ffffff 0%, #a5b4fc 50%, #38bdf8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-size: 200% auto; animation: shine 4s linear infinite; margin: 0 !important; padding: 0 !important; font-size: 27px; line-height: 0.95 !important; letter-spacing: 1.5px; text-shadow: 0 4px 15px rgba(59, 130, 246, 0.25); }}
            @keyframes shine {{ to {{ background-position: 200% center; }} }}
            
            .powered-by-reverted {{ margin: 2px 0 0 0 !important; padding: 0 !important; font-size: 13.5px; font-weight: 800; background: linear-gradient(90deg, #94a3b8, #e2e8f0, #94a3b8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-size: 200% auto; animation: shine 4s linear infinite reverse; letter-spacing: 2.5px; line-height: 1.0 !important; text-shadow: 0 2px 8px rgba(0,0,0,0.5); }}
            .college-header-info {{ margin: 4px 0 0 0 !important; font-size: 11px; opacity: 0.65; color: #cbd5e1 !important; letter-spacing: 0.5px; font-weight: 500; }}

            .neural-core {{ width: 24px; height: 24px; border-radius: 50%; background: {accent}; position: relative; margin: 0; margin-right: 10px !important; display: inline-block; box-shadow: 0 0 12px {accent}; animation: corePulse 2s infinite alternate; flex-shrink: 0; transition: all 0.3s ease; }}
            .cyber-header:hover .neural-core {{ box-shadow: 0 0 20px #3b82f6, 0 0 35px #8b5cf6; transform: scale(1.1); }}
            .neural-core::before, .neural-core::after {{ content: ''; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); border-radius: 50%; border: 2px solid {accent}; }}
            .neural-core::before {{ width: 42px; height: 42px; border-top-color: transparent; border-bottom-color: transparent; animation: spinCore 3s linear infinite; }}
            .neural-core::after {{ width: 58px; height: 58px; border-left-color: transparent; border-right-color: transparent; border-color: #8b5cf6 transparent #8b5cf6 transparent; animation: spinCoreReverse 4s linear infinite; border-width: 3px; }}
            @keyframes corePulse {{ 0% {{ transform: scale(0.9); box-shadow: 0 0 8px {accent}; }} 100% {{ transform: scale(1.15); box-shadow: 0 0 25px {accent}, 0 0 40px #8b5cf6; background: #8b5cf6; }} }}
            @keyframes spinCore {{ 100% {{ transform: translate(-50%, -50%) rotate(360deg); }} }}
            @keyframes spinCoreReverse {{ 100% {{ transform: translate(-50%, -50%) rotate(-360deg); }} }}
            
            .graph-container {{ display: flex; align-items: flex-end; gap: 6px; height: 45px; margin: 0; padding: 0; flex-shrink: 0; padding-right: 15px; transition: all 0.3s ease; }}
            .cyber-header:hover .graph-container {{ filter: brightness(1.2); }}
            .bar {{ width: 8px; border-radius: 4px; animation: equalize 1.2s infinite alternate ease-in-out; box-shadow: 0 0 8px rgba(0,0,0,0.5); }}
            .bar:nth-child(1) {{ background-color: {accent}; animation-delay: 0.1s; height: 18px; }}
            .bar:nth-child(2) {{ background-color: #10b981; animation-delay: 0.4s; height: 33px; }}
            .bar:nth-child(3) {{ background-color: #ef4444; animation-delay: 0.2s; height: 42px; }}
            .bar:nth-child(4) {{ background-color: #8b5cf6; animation-delay: 0.6s; height: 24px; }}
            .bar:nth-child(5) {{ background-color: #f59e0b; animation-delay: 0.3s; height: 36px; }}
            .bar:nth-child(6) {{ background-color: #ec4899; animation-delay: 0.5s; height: 27px; }}
            .bar:nth-child(7) {{ background-color: #06b6d4; animation-delay: 0.7s; height: 21px; }}
            @keyframes equalize {{ 0% {{ height: 8px; }} 100% {{ height: 45px; }} }}
            
            /* ========================================================= */
            
            .footer-block {{ display: flex; align-items: center; justify-content: center; flex-wrap: wrap; color: {footer_text}; font-size: 13px; font-weight: 600; opacity: 0.95; gap: 5px; text-align: center; line-height: 1.5; }}
            .animated-footer {{ position: static !important; width: 100%; max-width: 1400px; margin: 20px auto !important; background: {footer_bg}; border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 50px; padding: 12px 35px; z-index: 1000; display: flex; justify-content: space-between; align-items: center; backdrop-filter: blur(25px); -webkit-backdrop-filter: blur(25px); box-shadow: 0 10px 40px {footer_shadow}; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); overflow: hidden; flex-wrap: wrap; }}
            .animated-footer:hover {{ box-shadow: 0 15px 50px {footer_shadow}, 0 0 30px rgba(59, 130, 246, 0.3); transform: translateY(-6px); border-color: rgba(59, 130, 246, 0.8); }}
            .animated-footer::before {{ content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 3px; background: linear-gradient(90deg, transparent, #3b82f6, #06b6d4, #8b5cf6, transparent); background-size: 200% 100%; animation: laserScan 3s linear infinite; }}
            @keyframes laserScan {{ 0% {{ background-position: 100% 0; }} 100% {{ background-position: -100% 0; }} }}
            
            .anim-copyright {{ display: inline-block; animation: spin-slow 4s linear infinite; font-size: 15px; }}
            @keyframes spin-slow {{ 100% {{ transform: rotate(360deg); }} }}
            .anim-core {{ display: inline-flex; align-items: center; justify-content: center; animation: pulse-core 2s ease-in-out infinite alternate; font-size: 17px; filter: drop-shadow(0 0 5px rgba(6, 182, 212, 0.8)); margin: 0 2px; }}
            @keyframes pulse-core {{ 0% {{ transform: scale(0.9); }} 100% {{ transform: scale(1.2) rotate(15deg); filter: drop-shadow(0 0 12px rgba(59, 130, 246, 1)); }} }}
            .anim-dev {{ display: inline-block; animation: typing-bounce 1.5s infinite; font-size: 17px; }}
            @keyframes typing-bounce {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-4px); }} }}
            .anim-grad {{ display: inline-block; animation: float-cap 3s ease-in-out infinite; font-size: 17px; filter: drop-shadow(0 0 4px rgba(255,255,255,0.3)); }}
            @keyframes float-cap {{ 0%, 100% {{ transform: translateY(0) rotate(0deg); }} 50% {{ transform: translateY(-4px) rotate(-10deg); }} }}
            .dev-name {{ background: linear-gradient(90deg, #3b82f6, #06b6d4, #8b5cf6, #3b82f6); -webkit-background-clip: text; color: transparent !important; background-size: 200% auto; font-weight: 900; font-size: 14.5px; letter-spacing: 0.5px; display: inline-block; cursor: pointer; animation: shine 3s linear infinite, devPulse 2s infinite alternate; border-bottom: 2px dashed rgba(6,182,212, 0.4); padding-bottom: 2px; }}
            @keyframes devPulse {{ 0% {{ transform: scale(1); filter: drop-shadow(0 0 2px rgba(59,130,246,0.5)); }} 100% {{ transform: scale(1.04); filter: drop-shadow(0 0 8px rgba(6,182,212,0.8)); }} }}
            
            /* --- RESPONSIVE FIXES LOCKED --- */
            @media (max-width: 1024px) {{
                .animated-footer {{ justify-content: center !important; border-radius: 25px !important; gap: 15px; }}
            }}

            @media (max-width: 768px) {{
                .header-flex-main {{ flex-direction: row !important; justify-content: space-between !important; }} 
                .glow-text {{ font-size: 14px !important; letter-spacing: 1px !important; text-align: center !important; line-height: 1.2 !important; margin-bottom: 2px !important; }} 
                .powered-by-reverted {{ display: block !important; font-size: 8.5px !important; letter-spacing: 1.5px !important; margin-top: 0px !important; text-align: center !important; }}
                .college-header-info {{ display: none !important; }} 
                .cyber-header {{ padding: 12px 8px !important; }} 
                .header-left-col {{ flex: 0 0 auto !important; padding-left: 2px !important; justify-content: flex-start !important; }}
                .header-center-col {{ flex: 1 !important; padding: 0 5px !important; justify-content: center !important; gap: 0 !important; }}
                .header-right-col {{ flex: 0 0 auto !important; padding-right: 2px !important; justify-content: flex-end !important; }}
                
                .neural-core {{ width: 16px !important; height: 16px !important; margin: 0 !important; }}
                .neural-core::before {{ width: 28px !important; height: 28px !important; }}
                .neural-core::after {{ width: 38px !important; height: 38px !important; }}
                
                .graph-container {{ height: 25px !important; gap: 3px !important; padding: 0 !important; }}
                .bar {{ width: 4px !important; border-radius: 2px !important; }}
                @keyframes equalize {{ 0% {{ height: 4px; }} 100% {{ height: 25px; }} }}

                div.stButton > button {{ padding: 0 5px !important; font-size: 12px !important; }}
                div[data-testid="stHorizontalBlock"]:first-of-type {{ display: flex !important; flex-wrap: wrap !important; justify-content: space-between !important; }}
                div[data-testid="stHorizontalBlock"]:first-of-type > div[data-testid="column"] {{ flex-grow: 1 !important; flex-basis: 30% !important; margin-bottom: 10px !important; }}
                div[data-testid="stHorizontalBlock"]:first-of-type > div[data-testid="column"]:nth-child(1) {{ flex-basis: 100% !important; order: -1; }} 
                div[data-testid="stHorizontalBlock"]:first-of-type > div[data-testid="column"]:nth-child(2) {{ display: none !important; }} 
                div[data-testid="stHorizontalBlock"]:first-of-type > div[data-testid="column"]:nth-child(3),
                div[data-testid="stHorizontalBlock"]:first-of-type > div[data-testid="column"]:nth-child(4) {{ flex-basis: 48% !important; }} 

                .animated-footer {{ flex-direction: column !important; border-radius: 20px !important; padding: 20px 15px !important; justify-content: center !important; text-align: center !important; gap: 12px !important; }}
                .footer-block {{ width: 100% !important; justify-content: center !important; }}
            }}
            
            @media (max-width: 480px) {{
                div[data-testid="stHorizontalBlock"]:first-of-type > div[data-testid="column"]:nth-child(3),
                div[data-testid="stHorizontalBlock"]:first-of-type > div[data-testid="column"]:nth-child(4) {{ flex-basis: 48% !important; }} 
                div.stButton > button {{ font-size: 11px !important; padding: 0 5px !important; height: 40px !important; }}
                .secure-badge-static, .welcome-badge {{ font-size: 12px !important; height: 40px !important; }}
                
                .footer-block {{ font-size: 11.5px !important; gap: 4px !important; line-height: 1.6 !important; }}
                .dev-name {{ font-size: 12.5px !important; }}
                .anim-core svg {{ width: 16px; height: 16px; }}
            }}

            /* --- STREAMLIT BRANDING NUKE (MASLA 2 FIX) --- */
            header[data-testid="stHeader"] {{ display: none !important; }}
            footer {{ display: none !important; }}
            [data-testid="stDecoration"] {{ display: none !important; }}
            [data-testid="stToolbar"] {{ display: none !important; visibility: hidden !important; }}
            .stDeployButton {{ display: none !important; visibility: hidden !important; }}
            .viewerBadge_container__1QSob {{ display: none !important; visibility: hidden !important; }}
            .viewerBadge_link__1S137 {{ display: none !important; visibility: hidden !important; }}
            div[class^="st-emotion-cache-"] > a {{ display: none !important; }}
            #MainMenu {{ visibility: hidden !important; }}

            div.block-container {{ padding-top: 2.5rem !important; padding-bottom: 0px !important; }}
        </style>
    """,
        unsafe_allow_html=True,
    )


def render_header():
    inject_global_styles()
    last_name = st.session_state.get("last_name", "User")
    is_logged_in = st.session_state.get("logged_in", False)

    html_header = f"""<div class='cyber-header'>
<div class='header-flex-main'>
<div class='header-left-col'>
<div class='neural-core'></div>
</div>
<div class='header-center-col'>
<div class='header-text-container-reverted'>
<h2 class='glow-text'>AI SENTIMENTS ANALYSIS SYSTEM</h2>
<h3 class='powered-by-reverted'>POWERED BY MAU APEX-STUDIO</h3>
<p class='college-header-info'>BS CS Final Year Project Architecture | GOVT. GRADUATE COLLEGE GOJRA</p>
</div>
</div>
<div class='header-right-col'>
<div class='graph-container'>
<div class='bar'></div><div class='bar'></div><div class='bar'></div><div class='bar'></div><div class='bar'></div><div class='bar'></div><div class='bar'></div>
</div>
</div>
</div>
</div>"""

    st.markdown(html_header, unsafe_allow_html=True)

    c_badge, c_space, c_toggle, c_logout = st.columns([4, 4, 1.5, 1.5])

    with c_badge:
        if is_logged_in:
            st.markdown(f"<div class='welcome-badge'>👋 Welcome, {last_name.title()}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='secure-badge-static'>🔒 Secure Access Required</div>", unsafe_allow_html=True)

    with c_toggle:
        theme_label = "☀️\u00A0Light" if st.session_state["theme"] == "dark" else "🌙\u00A0Dark"
        if st.button(theme_label, use_container_width=True):
            st.session_state["theme"] = "light" if st.session_state["theme"] == "dark" else "dark"
            st.rerun()

    with c_logout:
        if is_logged_in:
            if st.button("🚪\u00A0Logout", use_container_width=True):
                st.session_state.clear()
                st.query_params.clear()
                st.rerun()
        else:
            page = st.session_state.get("page", "intro")
            lbl = "🔑\u00A0Login" if page == "intro" else "🏠\u00A0Home"
            if st.button(lbl, use_container_width=True):
                st.session_state["page"] = "login" if page == "intro" else "intro"
                st.rerun()


def render_footer():
    import datetime
    current_year = datetime.datetime.now().year
    
    html = f"""<div class='animated-footer'>
<div class='footer-block'>
<span class='anim-copyright'>©️</span>
<span style='font-weight: bold;'>{current_year}&nbsp;&nbsp;|</span>
<span class='anim-core'><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M21.21 15.89A10 10 0 1 1 8 2.83"></path>
<path d="M22 12A10 10 0 0 0 12 2v10z"></path>
</svg></span>
<span>AI SENTIMENTS ANALYSIS SYSTEM</span>
</div>
<div class='footer-block footer-dev-section'>
<span>DEVELOPED BY :&nbsp;</span>
<span class='anim-dev'>👨‍💻</span> 
<span class='dev-name'>MUHAMMAD ASAD ULLAH</span>
</div>
<div class='footer-block college-details'>
<span class='anim-grad'>🎓</span>
<span style='margin-left: 4px;'>BS Computer Science | SESSION 2022-2026 | ROLL NO : 126168</span>
</div>
</div>"""

    st.markdown(html, unsafe_allow_html=True)


def show_neural_loader():
    if 'app_loaded' not in st.session_state:
        loader_html = """
        <div id="loader-container">
            <div class="loader-spinner"></div>
            <div class="loader-title">AI SENTIMENTS ANALYSIS SYSTEM</div>
            <div class="loader-status">POWERED BY MAU APEX-STUDIO...</div>
        </div>

        <style>
            #loader-container {
                position: fixed;
                top: 0; left: 0; width: 100vw; height: 100vh;
                background-color: #0f172a;
                display: flex;
                flex-direction: column;
                justify-content: center;
                align-items: center;
                z-index: 999999;
                animation: fadeOutLoader 3.5s ease-in-out forwards;
                pointer-events: none; 
            }

            .loader-spinner {
                width: 70px;
                height: 70px;
                border: 4px solid rgba(59, 130, 246, 0.15);
                border-top-color: #3b82f6;
                border-bottom-color: #8b5cf6;
                border-radius: 50%;
                animation: spin 1.2s cubic-bezier(0.68, -0.55, 0.265, 1.55) infinite;
                margin-bottom: 30px;
                box-shadow: 0 0 25px rgba(59, 130, 246, 0.3);
            }

            .loader-title {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                font-size: 24px;
                font-weight: 900;
                letter-spacing: 2.5px;
                text-align: center;
                text-transform: uppercase;
                background: linear-gradient(90deg, #3b82f6, #8b5cf6, #3b82f6);
                background-size: 200% auto;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: shine 3s linear infinite;
                margin-bottom: 15px;
                padding: 0 20px;
            }

            .loader-status {
                font-family: 'Courier New', Courier, monospace;
                font-size: 13px;
                color: #94a3b8;
                letter-spacing: 2px;
                text-transform: uppercase;
                animation: pulse 1.5s ease-in-out infinite;
            }

            @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
            @keyframes pulse { 0%, 100% { opacity: 0.4; } 50% { opacity: 1; text-shadow: 0 0 8px rgba(148, 163, 184, 0.6); } }
            @keyframes shine { to { background-position: 200% center; } }
            
            @keyframes fadeOutLoader {
                0% { opacity: 1; visibility: visible; }
                80% { opacity: 1; visibility: visible; }
                100% { opacity: 0; visibility: hidden; z-index: -10; display: none; }
            }
        </style>
        """
        
        st.markdown(loader_html, unsafe_allow_html=True)
        st.session_state['app_loaded'] = True
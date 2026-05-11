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
            div.stButton > button {{ background: {card_bg} !important; color: {text} !important; border: 1px solid {border} !important; border-radius: 8px !important; font-weight: bold !important; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); }}
            div.stButton > button:hover {{ border-color: {accent} !important; box-shadow: 0 0 15px {border} !important; transform: translateY(-3px) scale(1.02); }}
            button[kind="primary"], div[data-testid="stForm"] button {{ background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%) !important; color: white !important; border: none !important; box-shadow: 0 4px 15px rgba(59,130,246,0.3) !important; }}
            button[kind="primary"]:hover, div[data-testid="stForm"] button:hover {{ box-shadow: 0 8px 25px rgba(59,130,246,0.6) !important; }}
            
            /* --- CYBER HEADER --- */
            .cyber-header {{ background: {card_bg}; backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border: 1px solid {border}; border-radius: 15px; padding: 20px; position: relative; overflow: hidden; animation: float 6s ease-in-out infinite; margin-bottom: 15px; box-shadow: 0 10px 30px rgba(59, 130, 246, 0.15); z-index: 3; }}
            .cyber-header::before {{ content: ''; position: absolute; top: -100%; left: 0; width: 100%; height: 3px; background: linear-gradient(90deg, transparent, #6366f1, #0ea5e9, #6366f1, transparent); animation: cyber-scan 3.5s infinite; }}
            @keyframes cyber-scan {{ 0% {{ top: -10%; }} 100% {{ top: 110%; }} }}
            @keyframes float {{ 0%, 100% {{ transform: translateY(0px); }} 50% {{ transform: translateY(-8px); }} }}
            .header-flex {{ display: flex; justify-content: space-between; align-items: center; }}
            .glow-text {{ font-weight: 900; background: linear-gradient(90deg, #4f46e5, #0ea5e9, #4f46e5); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-size: 200% auto; animation: shine 3s linear infinite; margin: 0; font-size: 28px; }}
            @keyframes shine {{ to {{ background-position: 200% center; }} }}
            .neural-core {{ width: 18px; height: 18px; border-radius: 50%; background: {accent}; position: relative; margin-right: 20px; margin-left: 10px; display: inline-block; vertical-align: middle; box-shadow: 0 0 10px {accent}, 0 0 20px {accent}; animation: corePulse 2s infinite alternate; }}
            .neural-core::before, .neural-core::after {{ content: ''; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); border-radius: 50%; border: 2px solid {accent}; }}
            .neural-core::before {{ width: 32px; height: 32px; border-top-color: transparent; border-bottom-color: transparent; animation: spinCore 3s linear infinite; }}
            .neural-core::after {{ width: 44px; height: 44px; border-left-color: transparent; border-right-color: transparent; border-color: #8b5cf6 transparent #8b5cf6 transparent; animation: spinCoreReverse 4s linear infinite; }}
            @keyframes corePulse {{ 0% {{ transform: scale(0.9); box-shadow: 0 0 5px {accent}; }} 100% {{ transform: scale(1.1); box-shadow: 0 0 20px {accent}, 0 0 30px #8b5cf6; background: #8b5cf6; }} }}
            @keyframes spinCore {{ 100% {{ transform: translate(-50%, -50%) rotate(360deg); }} }}
            @keyframes spinCoreReverse {{ 100% {{ transform: translate(-50%, -50%) rotate(-360deg); }} }}
            .graph-container {{ display: flex; align-items: flex-end; gap: 4px; height: 30px; padding-bottom: 2px; }}
            .bar {{ width: 6px; border-radius: 2px; animation: equalize 1.2s infinite alternate ease-in-out; }}
            .bar:nth-child(1) {{ background-color: {accent}; animation-delay: 0.1s; height: 12px; }}
            .bar:nth-child(2) {{ background-color: #10b981; animation-delay: 0.4s; height: 22px; }}
            .bar:nth-child(3) {{ background-color: #ef4444; animation-delay: 0.2s; height: 28px; }}
            .bar:nth-child(4) {{ background-color: #8b5cf6; animation-delay: 0.6s; height: 16px; }}
            .bar:nth-child(5) {{ background-color: #f59e0b; animation-delay: 0.3s; height: 24px; }}
            .bar:nth-child(6) {{ background-color: #ec4899; animation-delay: 0.5s; height: 18px; }}
            .bar:nth-child(7) {{ background-color: #06b6d4; animation-delay: 0.7s; height: 14px; }}
            @keyframes equalize {{ 0% {{ height: 4px; }} 100% {{ height: 30px; }} }}
            
            .secure-badge-static {{ display: inline-block; background: rgba(100, 116, 139, 0.4); color: white !important; padding: 8px 20px; border-radius: 30px; font-weight: 800; font-size: 13px; margin-top: 5px; border: 1px solid rgba(255,255,255,0.1); cursor: default; user-select: none; }}
            .welcome-badge {{ display: inline-block; background: linear-gradient(135deg, {accent}, #8b5cf6); color: white !important; padding: 8px 20px; border-radius: 30px; font-weight: 800; font-size: 14px; box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4); margin-top: 5px; animation: bounce-in 0.8s cubic-bezier(0.68, -0.55, 0.265, 1.55); }}
            @keyframes bounce-in {{ from {{ transform: scale(0.5); opacity: 0; }} to {{ transform: scale(1); opacity: 1; }} }}
            .animated-footer {{ position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%); width: 96%; max-width: 1400px; background: {footer_bg}; border: 1px solid rgba(59, 130, 246, 0.4); border-radius: 50px; padding: 12px 35px; z-index: 1000; display: flex; justify-content: space-between; align-items: center; backdrop-filter: blur(25px); -webkit-backdrop-filter: blur(25px); box-shadow: 0 10px 40px {footer_shadow}; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); overflow: hidden; }}
            .animated-footer:hover {{ box-shadow: 0 15px 50px {footer_shadow}, 0 0 30px rgba(59, 130, 246, 0.3); transform: translateX(-50%) translateY(-6px); border-color: rgba(59, 130, 246, 0.8); }}
            .animated-footer::before {{ content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 3px; background: linear-gradient(90deg, transparent, #3b82f6, #06b6d4, #8b5cf6, transparent); background-size: 200% 100%; animation: laserScan 3s linear infinite; }}
            @keyframes laserScan {{ 0% {{ background-position: 100% 0; }} 100% {{ background-position: -100% 0; }} }}
            
            .anim-copyright {{ display: inline-block; animation: spin-slow 4s linear infinite; margin-right: 4px; font-size: 15px; }}
            @keyframes spin-slow {{ 100% {{ transform: rotate(360deg); }} }}
            .anim-core {{ display: inline-block; animation: pulse-core 2s ease-in-out infinite alternate; margin: 0 6px; font-size: 17px; filter: drop-shadow(0 0 5px rgba(6, 182, 212, 0.8)); }}
            @keyframes pulse-core {{ 0% {{ transform: scale(0.9); }} 100% {{ transform: scale(1.2) rotate(15deg); filter: drop-shadow(0 0 12px rgba(59, 130, 246, 1)); }} }}
            .anim-dev {{ display: inline-block; animation: typing-bounce 1.5s infinite; margin: 0 6px; font-size: 17px; }}
            @keyframes typing-bounce {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-4px); }} }}
            .anim-grad {{ display: inline-block; animation: float-cap 3s ease-in-out infinite; margin-right: 8px; font-size: 17px; filter: drop-shadow(0 0 4px rgba(255,255,255,0.3)); }}
            @keyframes float-cap {{ 0%, 100% {{ transform: translateY(0) rotate(0deg); }} 50% {{ transform: translateY(-4px) rotate(-10deg); }} }}
            
            .dev-name {{ background: linear-gradient(90deg, #3b82f6, #06b6d4, #8b5cf6, #3b82f6); -webkit-background-clip: text; color: transparent !important; background-size: 200% auto; font-weight: 900; margin-left: 2px; font-size: 14.5px; letter-spacing: 0.5px; display: inline-block; cursor: pointer; animation: shine 3s linear infinite, devPulse 2s infinite alternate; border-bottom: 2px dashed rgba(6,182,212, 0.4); padding-bottom: 2px; }}
            @keyframes devPulse {{ 0% {{ transform: scale(1); filter: drop-shadow(0 0 2px rgba(59,130,246,0.5)); }} 100% {{ transform: scale(1.04); filter: drop-shadow(0 0 8px rgba(6,182,212,0.8)); }} }}
            .dev-name:hover {{ animation: none; transform: scale(1.1); letter-spacing: 1.5px; filter: drop-shadow(0 0 20px rgba(59,130,246,1)); border-bottom: 2px solid rgba(6,182,212, 1); transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); }}
            .college-details, .footer-text {{ color: {footer_text}; font-size: 13px; font-weight: 600; margin: 0; opacity: 0.95; display: flex; align-items: center; }}
            .main .block-container {{ padding-bottom: 100px !important; }}
        </style>
    """,
        unsafe_allow_html=True,
    )


def render_header():
    inject_global_styles()
    last_name = st.session_state.get("last_name", "User")
    is_logged_in = st.session_state.get("logged_in", False)

    st.markdown(
        f"""
        <div class='cyber-header'>
            <div class='header-flex'>
                <div style='display: flex; align-items: center;'>
                    <div class='neural-core'></div>
                    <div>
                        <h2 class='glow-text'>AI SENTIMENTS ANALYSIS SYSTEM</br>POWERED BY MAU APEX-STUDIO</h2>
                        <p style='margin:0; font-size:12px; opacity:0.8;'>BS CS Final Year Project Architecture | GOVT. GRADUATE COLLEGE GOJRA</p>
                    </div>
                </div>
                <div class='graph-container'>
                    <div class='bar'></div><div class='bar'></div><div class='bar'></div>
                    <div class='bar'></div><div class='bar'></div><div class='bar'></div><div class='bar'></div>
                </div>
            </div>
        </div>
    """,
        unsafe_allow_html=True,
    )

    c_badge, c_space, c_toggle, c_logout = st.columns([4, 4, 1.5, 1.5])

    with c_badge:
        if is_logged_in:
            st.markdown(
                f"<div class='welcome-badge'>👋 Welcome, {last_name.title()}</div>",
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"<div class='secure-badge-static'>🔒 Secure Access Required</div>",
                unsafe_allow_html=True,
            )

    with c_toggle:
        theme_label = "☀️ Light" if st.session_state["theme"] == "dark" else "🌙 Dark"
        if st.button(theme_label, use_container_width=True):
            st.session_state["theme"] = (
                "light" if st.session_state["theme"] == "dark" else "dark"
            )
            st.rerun()

    with c_logout:
        if is_logged_in:
            if st.button("🚪 Logout", use_container_width=True):
                st.session_state.clear()
                st.query_params.clear()
                st.rerun()
        else:
            page = st.session_state.get("page", "intro")
            lbl = "🔑 Login" if page == "intro" else "🏠 Home"
            if st.button(lbl, use_container_width=True):
                st.session_state["page"] = "login" if page == "intro" else "intro"
                st.rerun()


def render_footer():
    # <-- Dynamic Year Generation -->
    current_year = datetime.datetime.now().year

    html = f"""
    <div class='animated-footer'>
        <div style='display: flex; align-items: center;'>
            <p class='footer-text' style='font-size: 13.5px; margin: 0; display: flex; align-items: center;'>
                <span class='anim-copyright'>©️</span><span style='opacity: 0.85; margin-right: 12px; font-weight: bold;'>{current_year}&nbsp;&nbsp;|</span>
                <span class='anim-core'><svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M21.21 15.89A10 10 0 1 1 8 2.83"></path>
                    <path d="M22 12A10 10 0 0 0 12 2v10z"></path>
                    </svg></span><span style='opacity: 0.9;'>AI SENTIMENTS ANALYSIS SYSTEM&nbsp;&nbsp;|
                </span>
                <span style='opacity: 0.9;'>&nbsp;&nbsp;DEVELOPED BY : </span><span class='anim-dev'>👨‍💻 </span> 
                <span class='dev-name'> MUHAMMAD ASAD ULLAH</span>
            </p>
        </div>
        <div style='display: flex; align-items: center;'>
            <p class='college-details'>
                <span class='anim-grad'>🎓</span>
                BS Computer Science | SESSION 2022-2026 | ROLL NO : 126168
            </p>
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)

# screen loader

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
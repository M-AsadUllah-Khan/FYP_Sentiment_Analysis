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

    # --- HEADER & FOOTER ---
    header_bg = (
        "linear-gradient(145deg, rgba(15, 23, 42, 0.85) 0%, rgba(30, 41, 59, 0.75) 50%, rgba(15, 23, 42, 0.85) 100%)"
        if is_dark
        else "linear-gradient(145deg, rgba(255, 255, 255, 0.9) 0%, rgba(241, 245, 249, 0.85) 50%, rgba(255, 255, 255, 0.9) 100%)"
    )
    header_border_top = "rgba(255, 255, 255, 0.15)" if is_dark else "rgba(255, 255, 255, 0.6)"
    header_border_bottom = "rgba(59, 130, 246, 0.5)" if is_dark else "rgba(59, 130, 246, 0.4)"
    header_shadow = (
        "0 20px 40px -10px rgba(0, 0, 0, 0.5), inset 0 1px 0px rgba(255, 255, 255, 0.1), inset 0 -1px 20px rgba(59, 130, 246, 0.1)" 
        if is_dark 
        else "0 15px 35px -10px rgba(59, 130, 246, 0.15), inset 0 1px 0px rgba(255, 255, 255, 0.8), inset 0 -1px 20px rgba(59, 130, 246, 0.05)"
    )
    
    footer_bg = (
        "linear-gradient(145deg, rgba(15, 23, 42, 0.9), rgba(30, 41, 59, 0.8))"
        if is_dark
        else "linear-gradient(145deg, rgba(255, 255, 255, 0.95), rgba(241, 245, 249, 0.9))"
    )
    footer_border = "rgba(255, 255, 255, 0.1)" if is_dark else "rgba(59, 130, 246, 0.15)"
    footer_shadow = (
        "0 15px 35px -5px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.1)" 
        if is_dark 
        else "0 10px 30px -5px rgba(59, 130, 246, 0.1), inset 0 1px 0 rgba(255, 255, 255, 0.8)"
    )
    footer_text_color = "#e2e8f0" if is_dark else "#475569"
    
    glow_text_bg = (
        "linear-gradient(to right, #ffffff 0%, #a5b4fc 50%, #38bdf8 100%)"
        if is_dark
        else "linear-gradient(to right, #0f172a 0%, #1d4ed8 50%, #0284c7 100%)"
    )
    glow_text_shadow = "0 4px 15px rgba(59, 130, 246, 0.3)" if is_dark else "0 2px 10px rgba(59, 130, 246, 0.15)"
    
    powered_by_bg = (
        "linear-gradient(90deg, #94a3b8, #e2e8f0, #94a3b8)"
        if is_dark
        else "linear-gradient(90deg, #475569, #0f172a, #475569)"
    )
    
    college_text_color = "#cbd5e1" if is_dark else "#334155"
    college_badge_bg = "rgba(59, 130, 246, 0.15)" if is_dark else "rgba(59, 130, 246, 0.08)"
    college_badge_border = "rgba(59, 130, 246, 0.3)" if is_dark else "rgba(59, 130, 246, 0.2)"

    st.markdown(
        f"""
        <style>
            div[data-testid="InputInstructions"] {{ display: none !important; }}
            .stApp {{ background-color: {bg}; background-image: radial-gradient(rgba(59, 130, 246, {0.15 if is_dark else 0.1}) 2px, transparent 2px), radial-gradient(rgba(139, 92, 246, {0.15 if is_dark else 0.1}) 2px, transparent 2px); background-size: 60px 60px; background-position: 0 0, 30px 30px; animation: moveBg 30s linear infinite; transition: background-color 0.5s ease; }}
            @keyframes moveBg {{ 0% {{ background-position: 0 0, 30px 30px; }} 100% {{ background-position: 600px 600px, 630px 630px; }} }}
            [data-testid="stAppViewBlockContainer"], [data-testid="stHorizontalBlock"], .stTabs {{ animation: cinematicTransition 1.2s cubic-bezier(0.16, 1, 0.3, 1) forwards; transform-origin: center top; }}
            @keyframes cinematicTransition {{ 0% {{ opacity: 0; transform: translateY(30px) scale(0.97); filter: blur(10px); }} 100% {{ opacity: 1; transform: translateY(0) scale(1); filter: blur(0); }} }}
            .stMarkdown, p, h1, h2, h3, h4, h5, h6 {{ color: {text} !important; }}
            
            /* --- BUTTONS --- */
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
            /* --- HEADER --- */
            /* ========================================================= */
            .cyber-header {{ 
                background: {header_bg} !important;
                backdrop-filter: blur(20px) saturate(150%); 
                -webkit-backdrop-filter: blur(20px) saturate(150%);
                border-top: 1px solid {header_border_top} !important;
                border-bottom: 2px solid {header_border_bottom} !important;
                border-left: 1px solid rgba(59, 130, 246, 0.15);
                border-right: 1px solid rgba(59, 130, 246, 0.15);
                border-radius: 20px; 
                padding: 15px 20px; 
                position: relative; 
                overflow: hidden; 
                animation: float 6s ease-in-out infinite; 
                margin-bottom: 15px; 
                box-shadow: {header_shadow} !important; 
                z-index: 3; 
                transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
            }}
            .cyber-header:hover {{ transform: translateY(-4px); filter: brightness(1.08); box-shadow: 0 25px 50px -12px rgba(59, 130, 246, 0.25), inset 0 1px 0px rgba(255, 255, 255, 0.2) !important; }}
            .cyber-header::before {{ content: ''; position: absolute; top: -100%; left: 0; width: 100%; height: 2px; background: linear-gradient(90deg, transparent, #6366f1, #0ea5e9, #6366f1, transparent); animation: cyber-scan 3.5s infinite; }}
            .cyber-header::after {{ content: ''; position: absolute; top: 0; left: -100%; width: 50%; height: 100%; background: linear-gradient(to right, transparent, rgba(255, 255, 255, 0.15), transparent); transform: skewX(-25deg); animation: glass-sweep 7s infinite; pointer-events: none; }}
            @keyframes glass-sweep {{ 0% {{ left: -100%; }} 15% {{ left: 200%; }} 100% {{ left: 200%; }} }}
            @keyframes cyber-scan {{ 0% {{ top: -10%; }} 100% {{ top: 110%; }} }}
            @keyframes float {{ 0%, 100% {{ transform: translateY(0px); }} 50% {{ transform: translateY(-6px); }} }}
            
            .header-flex-main {{ display: flex !important; flex-direction: row !important; justify-content: space-between !important; align-items: center !important; width: 100%; flex-wrap: nowrap !important; }}
            .header-left-col {{ flex: 1; display: flex; justify-content: flex-start; align-items: center; padding-left: 20px; }}
            .header-center-col {{ flex: 4; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; gap: 0px !important; }}
            .header-right-col {{ flex: 1; display: flex; justify-content: flex-end; align-items: center; padding-right: 15px; }}
            
            .glow-text {{ 
                font-family: 'Segoe UI', system-ui, sans-serif; 
                font-weight: 900; 
                background: {glow_text_bg} !important; 
                -webkit-background-clip: text !important; 
                background-clip: text !important;
                -webkit-text-fill-color: transparent !important; 
                color: transparent !important;
                background-size: 200% auto; 
                animation: shine 4s linear infinite; 
                margin: 0 !important; 
                padding: 0 !important; 
                font-size: 27px; 
                line-height: 0.95 !important; 
                letter-spacing: 1.5px; 
                text-shadow: {glow_text_shadow} !important; 
            }}
            @keyframes shine {{ to {{ background-position: 200% center; }} }}
            
            .powered-by-reverted {{ 
                margin: 3px 0 0 0 !important; 
                padding: 0 !important; 
                font-size: 13.5px; 
                font-weight: 800; 
                background: {powered_by_bg} !important; 
                -webkit-background-clip: text !important; 
                background-clip: text !important;
                -webkit-text-fill-color: transparent !important; 
                color: transparent !important;
                background-size: 200% auto; 
                animation: shine 4s linear infinite reverse; 
                letter-spacing: 3px; 
                line-height: 1.0 !important; 
                text-shadow: 0 2px 8px rgba(0,0,0,0.15); 
            }}
            
            .college-header-info {{ margin: 5px 0 0 0 !important; font-size: 11.5px; color: {college_text_color} !important; letter-spacing: 0.8px; font-weight: 600; opacity: 0.85; }}

            .neural-core {{ width: 24px; height: 24px; border-radius: 50%; background: {accent}; position: relative; margin: 0; margin-right: 10px !important; display: inline-block; box-shadow: 0 0 15px {accent}; animation: corePulse 2s infinite alternate; flex-shrink: 0; transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1); }}
            .cyber-header:hover .neural-core {{ box-shadow: 0 0 25px #3b82f6, 0 0 45px #8b5cf6; transform: scale(1.15); }}
            .neural-core::before, .neural-core::after {{ content: ''; position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); border-radius: 50%; border: 2px solid {accent}; }}
            .neural-core::before {{ width: 42px; height: 42px; border-top-color: transparent; border-bottom-color: transparent; animation: spinCore 3s linear infinite; }}
            .neural-core::after {{ width: 58px; height: 58px; border-left-color: transparent; border-right-color: transparent; border-color: #8b5cf6 transparent #8b5cf6 transparent; animation: spinCoreReverse 4s linear infinite; border-width: 3px; }}
            @keyframes corePulse {{ 0% {{ transform: scale(0.9); box-shadow: 0 0 8px {accent}; }} 100% {{ transform: scale(1.15); box-shadow: 0 0 25px {accent}, 0 0 40px #8b5cf6; background: #8b5cf6; }} }}
            @keyframes spinCore {{ 100% {{ transform: translate(-50%, -50%) rotate(360deg); }} }}
            @keyframes spinCoreReverse {{ 100% {{ transform: translate(-50%, -50%) rotate(-360deg); }} }}
            
            .graph-container {{ display: flex; align-items: flex-end; gap: 6px; height: 45px; margin: 0; padding: 0; flex-shrink: 0; padding-right: 15px; transition: all 0.4s ease; }}
            .cyber-header:hover .graph-container {{ filter: brightness(1.2) saturate(1.2); transform: scale(1.05); transform-origin: bottom right; }}
            .bar {{ width: 8px; border-radius: 4px; animation: equalize 1.2s infinite alternate ease-in-out; box-shadow: 0 0 8px rgba(0,0,0,0.3); }}
            .bar:nth-child(1) {{ background-color: {accent}; animation-delay: 0.1s; height: 18px; }}
            .bar:nth-child(2) {{ background-color: #10b981; animation-delay: 0.4s; height: 33px; }}
            .bar:nth-child(3) {{ background-color: #ef4444; animation-delay: 0.2s; height: 42px; }}
            .bar:nth-child(4) {{ background-color: #8b5cf6; animation-delay: 0.6s; height: 24px; }}
            .bar:nth-child(5) {{ background-color: #f59e0b; animation-delay: 0.3s; height: 36px; }}
            .bar:nth-child(6) {{ background-color: #ec4899; animation-delay: 0.5s; height: 27px; }}
            .bar:nth-child(7) {{ background-color: #06b6d4; animation-delay: 0.7s; height: 21px; }}
            @keyframes equalize {{ 0% {{ height: 8px; }} 100% {{ height: 45px; }} }}
            
            /* ========================================================= */
            /* --- FOOTER --- */
            /* ========================================================= */
            
            .footer-block {{ display: flex; align-items: center; justify-content: center; flex-wrap: wrap; color: {footer_text_color}; font-size: 13.5px; font-weight: 600; opacity: 0.95; gap: 6px; text-align: center; line-height: 1.5; letter-spacing: 0.3px; }}
            
            .animated-footer {{ 
                margin: auto auto 10px auto !important; 
                background: {footer_bg} !important; 
                border: 1px solid {footer_border} !important; 
                border-top: 1px solid rgba(255,255,255,0.2) !important;
                border-radius: 100px !important; 
                padding: 14px 40px; 
                z-index: 1000; 
                display: flex; 
                justify-content: space-between; 
                align-items: center; 
                backdrop-filter: blur(24px) saturate(150%); 
                -webkit-backdrop-filter: blur(24px) saturate(150%); 
                box-shadow: {footer_shadow} !important; 
                transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1); 
                overflow: hidden; 
                flex-wrap: wrap; 
                width: 100%; max-width: 1400px;
            }}
            .animated-footer:hover {{ 
                box-shadow: 0 25px 40px -10px rgba(59, 130, 246, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.4) !important; 
                transform: translateY(-5px) scale(1.005); 
                border-color: rgba(59, 130, 246, 0.5) !important; 
            }}
            
            .animated-footer::before {{ content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 2px; background: linear-gradient(90deg, transparent, #3b82f6, #0ea5e9, #8b5cf6, transparent); background-size: 200% 100%; animation: laserScan 4s ease-in-out infinite alternate; opacity: 0.7; }}
            @keyframes laserScan {{ 0% {{ background-position: 100% 0; }} 100% {{ background-position: -100% 0; }} }}
            
            .anim-copyright {{ display: inline-block; animation: spin-slow 4s linear infinite; font-size: 15px; color: {accent}; }}
            @keyframes spin-slow {{ 100% {{ transform: rotate(360deg); }} }}
            .anim-core {{ display: inline-flex; align-items: center; justify-content: center; animation: pulse-core 2s ease-in-out infinite alternate; font-size: 18px; filter: drop-shadow(0 0 6px rgba(6, 182, 212, 0.8)); margin: 0 4px; color: #0ea5e9; }}
            @keyframes pulse-core {{ 0% {{ transform: scale(0.9); }} 100% {{ transform: scale(1.2) rotate(15deg); filter: drop-shadow(0 0 15px rgba(59, 130, 246, 1)); }} }}
            .anim-dev {{ display: inline-block; animation: typing-bounce 1.5s infinite; font-size: 18px; }}
            @keyframes typing-bounce {{ 0%, 100% {{ transform: translateY(0); }} 50% {{ transform: translateY(-4px); }} }}
            .anim-grad {{ display: inline-block; animation: float-cap 3s ease-in-out infinite; font-size: 18px; filter: drop-shadow(0 0 5px rgba(59,130,246,0.4)); }}
            @keyframes float-cap {{ 0%, 100% {{ transform: translateY(0) rotate(0deg); }} 50% {{ transform: translateY(-4px) rotate(-10deg); }} }}
            
            .dev-name {{ background: linear-gradient(90deg, #3b82f6, #06b6d4, #8b5cf6, #3b82f6); -webkit-background-clip: text; color: transparent !important; background-size: 200% auto; font-weight: 900; font-size: 15px; letter-spacing: 0.8px; display: inline-block; cursor: pointer; animation: shine 3s linear infinite, devPulse 2s infinite alternate; padding-bottom: 2px; text-shadow: 0 2px 10px rgba(59,130,246,0.15); }}
            @keyframes devPulse {{ 0% {{ transform: scale(1); filter: drop-shadow(0 0 2px rgba(59,130,246,0.3)); }} 100% {{ transform: scale(1.02); filter: drop-shadow(0 0 10px rgba(6,182,212,0.6)); }} }}
            
            /* --- RESPONSIVE FIXES LOCKED --- */
            @media (max-width: 1024px) {{
                .animated-footer {{ justify-content: center !important; border-radius: 35px !important; gap: 15px; padding: 18px 25px !important; }}
            }}

            @media (max-width: 768px) {{
                .header-flex-main {{ flex-direction: row !important; justify-content: space-between !important; }} 
                .glow-text {{ font-size: 14.5px !important; letter-spacing: 0.5px !important; text-align: center !important; line-height: 1.3 !important; margin-bottom: 2px !important; white-space: normal !important; width: 100% !important; }} 
                .powered-by-reverted {{ display: block !important; font-size: 8px !important; letter-spacing: 1.5px !important; margin-top: 0px !important; text-align: center !important; width: 100% !important; }}
                
                .college-header-info {{ 
                    display: inline-block !important; 
                    font-size: 7px !important; 
                    letter-spacing: 0.5px !important; 
                    margin-top: 8px !important; 
                    padding: 4px 10px !important; 
                    background: {college_badge_bg} !important; 
                    border-radius: 20px !important; 
                    border: 1px solid {college_badge_border} !important; 
                    color: {college_text_color} !important;
                    font-weight: 700 !important;
                    white-space: nowrap !important;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.05) !important;
                }}
                
                .cyber-header {{ padding: 18px 12px !important; border-radius: 18px !important; }} 
                .header-left-col {{ flex: 0 0 65px !important; padding-left: 6px !important; justify-content: flex-start !important; align-items: center !important; overflow: visible !important; }}
                .header-center-col {{ flex: 1 !important; padding: 0 !important; justify-content: center !important; align-items: center !important; display: flex !important; flex-direction: column !important; }}
                .header-right-col {{ flex: 0 0 65px !important; padding-right: 6px !important; justify-content: flex-end !important; align-items: center !important; overflow: visible !important; }}
                
                .neural-core {{ width: 18px !important; height: 18px !important; margin: 0 !important; margin-left: 5px !important; }}
                .neural-core::before {{ width: 30px !important; height: 30px !important; }}
                .neural-core::after {{ width: 40px !important; height: 40px !important; }}
                
                .graph-container {{ height: 26px !important; gap: 3.5px !important; padding: 0 !important; margin-right: 5px !important; }}
                .bar {{ width: 4.5px !important; border-radius: 2px !important; }}
                @keyframes equalize {{ 0% {{ height: 4px; }} 100% {{ height: 26px; }} }}

                div.stButton > button {{ padding: 0 5px !important; font-size: 12px !important; }}
                div[data-testid="stHorizontalBlock"]:first-of-type {{ display: flex !important; flex-wrap: wrap !important; justify-content: space-between !important; }}
                div[data-testid="stHorizontalBlock"]:first-of-type > div[data-testid="column"] {{ flex-grow: 1 !important; flex-basis: 30% !important; margin-bottom: 10px !important; }}
                div[data-testid="stHorizontalBlock"]:first-of-type > div[data-testid="column"]:nth-child(1) {{ flex-basis: 100% !important; order: -1; }} 
                div[data-testid="stHorizontalBlock"]:first-of-type > div[data-testid="column"]:nth-child(2) {{ display: none !important; }} 
                div[data-testid="stHorizontalBlock"]:first-of-type > div[data-testid="column"]:nth-child(3),
                div[data-testid="stHorizontalBlock"]:first-of-type > div[data-testid="column"]:nth-child(4) {{ flex-basis: 48% !important; }} 

                .animated-footer {{ flex-direction: column !important; border-radius: 22px !important; padding: 22px 15px !important; justify-content: center !important; text-align: center !important; gap: 14px !important; }}
                .footer-block {{ width: 100% !important; justify-content: center !important; }}
            }}
            
            @media (max-width: 480px) {{
                .college-header-info {{ display: none !important; }}
                .cyber-header {{ padding: 12px 10px !important; }}
                .header-left-col {{ flex: 0 0 45px !important; padding-left: 2px !important; }}
                .header-right-col {{ flex: 0 0 45px !important; padding-right: 2px !important; }}
                .glow-text {{ font-size: 12.5px !important; line-height: 1.2 !important; }}
                .neural-core {{ width: 15px !important; height: 15px !important; margin-left: 2px !important; }}
                .neural-core::before {{ width: 26px !important; height: 26px !important; }}
                .neural-core::after {{ width: 34px !important; height: 34px !important; }}
                .graph-container {{ height: 22px !important; margin-right: 2px !important; }}
                .bar {{ width: 3.5px !important; }}
                @keyframes equalize {{ 0% {{ height: 4px; }} 100% {{ height: 22px; }} }}
                
                div[data-testid="stHorizontalBlock"]:first-of-type > div[data-testid="column"]:nth-child(3),
                div[data-testid="stHorizontalBlock"]:first-of-type > div[data-testid="column"]:nth-child(4) {{ flex-basis: 48% !important; }} 
                div.stButton > button {{ font-size: 11px !important; padding: 0 5px !important; height: 40px !important; }}
                .secure-badge-static, .welcome-badge {{ font-size: 12px !important; height: 40px !important; }}
                .footer-block {{ font-size: 11.5px !important; gap: 4px !important; line-height: 1.6 !important; }}
                .dev-name {{ font-size: 12.5px !important; }}
                .anim-core svg {{ width: 16px; height: 16px; }}
            }}

            /* --- HIDE STREAMLIT BRANDING  --- */
            header[data-testid="stHeader"] {{ display: none !important; }}
            footer[data-testid="stFooter"] {{ display: none !important; }}
            
            /* Target specific Cloud badges without touching app structural divs */
            .stDeployButton, [data-testid="stToolbar"], #MainMenu {{ display: none !important; visibility: hidden !important; }}
            div[class*="viewerBadge"], div[class*="manage-app"] {{ display: none !important; }}

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
    
    st.markdown("<div style='height: 25vh; flex-grow: 1;'></div>", unsafe_allow_html=True)
    
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
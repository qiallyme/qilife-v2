import streamlit as st
from pathlib import Path
import time
import base64

def show_splash(duration: int = 3):
    """
    Display a branded splash screen for a given duration (in seconds).
    Shows the QLife logo, title, and a loading spinner.
    """
    logo_path = Path(__file__).parent.parent / "qlife.png"
    # Encode logo as base64 for inline HTML
    if logo_path.exists():
        encoded = base64.b64encode(logo_path.read_bytes()).decode()
        img_html = f"<img src='data:image/png;base64,{encoded}' width='200' />"
    else:
        img_html = "<h2>🌐 QLife AI</h2>"

    st.markdown(
        "<div style='text-align:center; margin-top:50px;'>"
        f"{img_html}"
        "<h1 style='margin: 20px 0 10px;'>The One App – EmpowerQNow-713</h1>"
        "</div>",
        unsafe_allow_html=True
    )

    with st.spinner("Loading modules..."):
        time.sleep(duration)
    st.empty()

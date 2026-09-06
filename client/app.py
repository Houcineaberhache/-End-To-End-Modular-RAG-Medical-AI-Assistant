import streamlit as st

from components.upload import render_uploader
from components.history_download import render_history_download
from components.chatUI import render_chat
from style import inject_custom_css

st.set_page_config(
    page_title="MediBot — AI Medical Assistant",
    page_icon="🩺",
    layout="wide",
)

inject_custom_css()

# ---------- Header ----------
st.markdown(
    """
    <div class="medibot-header">
        <div class="icon">🩺</div>
        <div>
            <p class="title">MediBot</p>
            <p class="subtitle">AI Medical Assistant — grounded in your own documents</p>
        </div>
    </div>
    <span class="status-badge">● RAG pipeline active</span>
    <hr class="medibot-divider">
    """,
    unsafe_allow_html=True,
)

render_uploader()
render_chat()
render_history_download()

# ---------- Footer ----------
st.markdown(
    """
    <div class="disclaimer">
        ⚠️ MediBot is a portfolio project and does not provide medical advice or diagnoses.
        Always consult a qualified healthcare professional.
    </div>
    """,
    unsafe_allow_html=True,
)

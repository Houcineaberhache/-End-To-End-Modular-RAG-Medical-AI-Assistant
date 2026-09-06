import streamlit as st
from datetime import datetime


def render_history_download():
    messages = st.session_state.get("messages")
    if not messages:
        return

    st.divider()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")
    chat_text = "\n\n".join(
        f"{m['role'].upper()}: {m['content']}" for m in messages
    )

    col1, col2 = st.columns([3, 1])
    with col1:
        st.caption(f"🗂️ {len(messages)} message(s) in this conversation")
    with col2:
        st.download_button(
            "⬇️ Export chat",
            chat_text,
            file_name=f"medibot_chat_{timestamp}.txt",
            mime="text/plain",
            use_container_width=True,
        )
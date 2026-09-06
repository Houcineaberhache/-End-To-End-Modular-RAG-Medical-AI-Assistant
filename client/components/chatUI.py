import streamlit as st
from utils.api import ask_question


def render_sources(sources):
    if not sources:
        return
    chips = "".join(f'<span class="source-chip">📄 {src}</span>' for src in sources)
    st.markdown(
        f"""
        <div class="source-box">
            <b>Sources referenced:</b><br>{chips}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_chat():
    st.subheader("💬 Chat with your assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # ---------- Empty state ----------
    if not st.session_state.messages:
        st.markdown(
            """
            <div class="empty-state">
                <div class="big-icon">🧬</div>
                <div class="headline">Ask MediBot anything about your uploaded documents</div>
                <div>Try: "What are the symptoms of diabetes?" or "How is it diagnosed?"</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ---------- Render chat history ----------
    for msg in st.session_state.messages:
        avatar = "🧑‍⚕️" if msg["role"] == "user" else "🩺"
        with st.chat_message(msg["role"], avatar=avatar):
            st.markdown(msg["content"])
            if msg["role"] == "assistant" and msg.get("sources"):
                render_sources(msg["sources"])

    # ---------- Input + response ----------
    user_input = st.chat_input("Type your question....")
    if user_input:
        with st.chat_message("user", avatar="🧑‍⚕️"):
            st.markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("assistant", avatar="🩺"):
            with st.spinner("Reviewing your documents..."):
                response = ask_question(user_input)

            if response.status_code == 200:
                data = response.json()
                answer = data["response"]
                sources = [s for s in data.get("sources", []) if s]

                st.markdown(answer)
                render_sources(sources)

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer, "sources": sources}
                )
            else:
                st.error(f"Something went wrong: {response.text}")
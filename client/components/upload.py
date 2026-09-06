import streamlit as st
from utils.api import upload_pdfs_api


def render_uploader():
    with st.sidebar:
        st.header("📁 Knowledge Base")
        st.caption("Upload medical PDFs to ground MediBot's answers.")

        uploaded_files = st.file_uploader(
            "Upload multiple PDFs",
            type="pdf",
            accept_multiple_files=True,
            label_visibility="collapsed",
        )

        if uploaded_files:
            st.caption(f"📄 {len(uploaded_files)} file(s) selected")
            for f in uploaded_files:
                st.markdown(f"- `{f.name}`")

        if st.button("⬆️ Upload & Index", use_container_width=True):
            if not uploaded_files:
                st.warning("Select at least one PDF first.")
            else:
                with st.spinner("Chunking, embedding, and indexing..."):
                    response = upload_pdfs_api(uploaded_files)

                if response.status_code == 200:
                    st.success(f"✅ {len(uploaded_files)} document(s) indexed successfully")
                else:
                    st.error(f"Upload failed: {response.text}")

        st.divider()
        st.caption("Built with LangChain · Groq · Pinecone · FastAPI")
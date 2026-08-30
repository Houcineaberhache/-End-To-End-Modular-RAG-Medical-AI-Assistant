from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def format_docs(docs):
    """Combine retrieved document chunks into a single context string."""
    return "\n\n".join(doc.page_content for doc in docs)


def get_llm_chain(retriever):
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama3-70b-8192"
    )

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
            You are **MediBot**, an AI-powered assistant trained to help users understand medical documents and health-related questions.

            Your job is to provide clear, accurate, and helpful responses based **only on the provided context**.

            ---

            🔍 **Context**:
            {context}

            🙋‍♂️ **User Question**:
            {question}

            ---

            💬 **Answer**:
            - Respond in a calm, factual, and respectful tone.
            - Use simple explanations when needed.
            - If the context does not contain the answer, say: "I'm sorry, but I couldn't find relevant information in the provided documents."
            - Do NOT make up facts.
            - Do NOT give medical advice or diagnoses.
            """
    )

    # This builds the same "answer" the LLM would produce
    answer_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    # This wraps it so you get BOTH the answer AND the raw source documents back,
    # replicating what return_source_documents=True used to give you
    rag_chain = RunnableParallel(
        {
            "source_documents": retriever,
            "question": RunnablePassthrough(),
        }
    ).assign(result=answer_chain)

    return rag_chain
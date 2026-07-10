import time
import streamlit as st

from rag_pipeline import generate_grounded_answer

# -----------------------------------------------------
# Streamlit Page Configuration
# -----------------------------------------------------

st.set_page_config(
    page_title="PolicyRAG Enterprise",
    page_icon="📘",
    layout="wide"
)

# -----------------------------------------------------
# Custom Styling
# -----------------------------------------------------

st.markdown("""
<style>

.main-title{
    font-size:42px;
    font-weight:bold;
    color:#1f4e79;
}

.subtitle{
    font-size:18px;
    color:gray;
}

.answer-box{
    background:#F4F6F7;
    border-left:6px solid #1f77b4;
    padding:20px;
    border-radius:8px;
    font-size:17px;
}

.source-box{
    background:#FAFAFA;
    border:1px solid #DDDDDD;
    padding:15px;
    border-radius:8px;
    margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# Sidebar
# -----------------------------------------------------

with st.sidebar:

    st.header("System Status")
    st.success("RAG pipeline active")

    st.header("Knowledge Base")

    st.write("📄 Documents indexed: **10**")
    st.write("🧩 Chunks indexed: **132**")
    st.write("🗄️ Vector Database: **ChromaDB**")
    st.write("🧠 Embedding Model: **all-MiniLM-L6-v2**")
    st.write("🤖 LLM: **Groq llama-3.1-8b-instant**")

    st.divider()

    st.header("Suggested Questions")

    st.markdown("""
- How many annual leave days do employees receive?

- Can employees use public Wi-Fi?

- How long do I have to submit an expense claim?

- Can I install software on my work laptop?

- What is considered a conflict of interest?

- Can the company sell my personal information?

- Is PPE mandatory?

- Are meals reimbursed during business travel?
""")

# -----------------------------------------------------
# Main Page
# -----------------------------------------------------

st.markdown(
    '<p class="main-title">📘 PolicyRAG Enterprise</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">AI Assistant for NamTech Solutions Ltd Company Policies</p>',
    unsafe_allow_html=True
)

st.divider()

question = st.text_area(
    "Ask a question about NamTech Solutions Ltd policies:",
    height=120,
    placeholder="Example: How many annual leave days do employees receive?"
)

if st.button("Ask PolicyRAG", use_container_width=True):

    if question.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    start = time.time()

    with st.spinner("Searching company policies..."):

        response = generate_grounded_answer(question)

    elapsed = time.time() - start

    st.subheader("🤖 Answer")

    st.markdown(
        f'<div class="answer-box">{response["answer"]}</div>',
        unsafe_allow_html=True
    )

    st.subheader("📚 Sources")

    if response["citations"]:

        for citation in response["citations"]:

            st.markdown(f"""
<div class="source-box">

**Source:** {citation["source"]}

**Chunk ID:** {citation["chunk_id"]}

{citation["snippet"]}

</div>
""", unsafe_allow_html=True)

    else:

        st.info("No supporting citations available.")

    st.caption(f"Response time: {elapsed:.2f} seconds")
    
    
import streamlit as st
from langchain_community.document_loaders import SeleniumURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """
You are an assistant for question-answering tasks. Use the following pieces of retrieved context to answer the question.
If you don't know the answer, just say that you don't know. Use three sentences maximum and keep the answer concise.

Question: {question}
Context: {context}
Answer:
"""

embeddings = OllamaEmbeddings(model="mxbai-embed-large")
llm = OllamaLLM(model="llama3.2")

st.title("🕷️ AI Web Page Crawler + QA")

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

url = st.text_input("Enter a webpage URL to crawl:")

if url:
    with st.spinner("🔍 Crawling and indexing..."):
        loader = SeleniumURLLoader(urls=[url])
        documents = loader.load()
        print(documents)

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        split_docs = splitter.split_documents(documents)

        vector_store = InMemoryVectorStore.from_documents(
            split_docs, embedding=embeddings
        )
        st.session_state.vector_store = vector_store
        st.success("✅ Page indexed! You can now ask questions.")

question = st.chat_input("Ask a question about the page...")

if question and st.session_state.vector_store:
    st.chat_message("user").write(question)

    relevant_docs = st.session_state.vector_store.similarity_search(question)
    context = "\n\n".join([doc.page_content for doc in relevant_docs])

    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | llm
    answer = chain.invoke({"question": question, "context": context})

    st.chat_message("assistant").write(answer)
elif question:
    st.warning("Please enter a URL first to load and index content.")

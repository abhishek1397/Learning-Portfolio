# RAG Chatbot

![RAG Chatbot](https://github.com/user-attachments/assets/5ced6fe0-e56a-4a9a-afd6-68bd1bb3e657)

# 🎓 What I Learned from This Project

🔗 **Project Repository**: [PDF-RAG-Chatbot](https://github.com/abhishek1397/PDF-RAG-Chatbot)

This project was a hands-on deep dive into Retrieval-Augmented Generation (RAG) using modern AI tools. Here’s a breakdown of the key skills and concepts I learned and implemented:

---

## 🧠 Core Concepts

- ✅ **Retrieval-Augmented Generation (RAG)**
  - Understanding how to combine retrieval with LLMs to provide accurate, grounded answers from documents.
  
- ✅ **Vector Databases & Similarity Search**
  - Creating and querying a FAISS vector index.
  - Performing semantic search with sentence embeddings.

- ✅ **Embeddings**
  - Using `sentence-transformers/all-mpnet-base-v2` for generating dense vector representations of text.
  - Understanding how embeddings power semantic search in LLM applications.

---

## 🛠️ Tools & Libraries

- **LangChain**
  - Creating chains with `RetrievalQA` and `ChatOllama`.
  - Integrating embeddings and vector stores in a pipeline.

- **FAISS**
  - Storing and retrieving vectorized PDF chunks efficiently.
  - Saving and loading vector indexes locally.

- **Streamlit**
  - Building a clean and interactive UI for user uploads and chatbot interaction.
  - Managing session state, user input, and dynamic updates.

- **Ollama**
  - Running `llama3.1` locally for fast and private inference.
  - Integrating LLMs into a custom retrieval pipeline.

- **PyPDF2**
  - Extracting and cleaning text from uploaded PDFs.

---

## 🧩 System Design & Integration

- End-to-end PDF RAG pipeline: from upload → chunking → embedding → storing → retrieval → response.
- Caching and performance handling using `@st.cache_resource`.
- Handling deserialization security with `allow_dangerous_deserialization`.

---

## 📁 DevOps / Project Management

- Creating a clean, reproducible `requirements.txt`.
- Structuring and documenting a project on GitHub.
- Applying the MIT License to open-source code.

---

This project not only improved my understanding of retrieval-based LLM workflows but also strengthened my ability to integrate AI into real-world applications.


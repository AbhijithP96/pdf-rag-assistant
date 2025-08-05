# 🧾 PDF Chat Assistant using RAG (LLM + Streamlit)

A lightweight, local, and interactive chatbot that lets you ask questions about the content of any PDF. Built using **Ollama**, **LlamaIndex**, **ChromaDB**, and **Streamlit**, this project showcases a practical implementation of a **Retrieval-Augmented Generation (RAG)** pipeline.

![Demo Screenshot](/data/demo.png) <!-- Optional: Replace with your actual screenshot path -->

---

## 🚀 Features

- 🔍 Ask questions based on the contents of your uploaded PDF
- ⚡ Runs **locally** with an LLM served via Ollama (e.g., `llama3`, `mistral`)
- 📚 Uses **LlamaIndex** to chunk, embed, and retrieve relevant context
- 🧠 Employs **RAG** to combine search results with generative responses
- 🖥️ Built with **Streamlit** for a fast and interactive frontend

---

## 🛠️ Tech Stack

| Component      | Tool/Library             |
|----------------|--------------------------|
| LLM Backend    | Ollama (`llama2`, etc.)  |
| Vector DB      | Chroma                   |
| RAG Framework  | LlamaIndex               |
| UI             | Streamlit                |
| Language       | Python                   |

---

## 📦 Installation

1. **Install Ollama**: Click to install [Ollama](https://ollama.com/) to set up the LLM backend.

2. **Pull the LLM and Embedder**:
```bash
ollama pull [llm_name]  # e.g., ollama pull llama2
# or for Mistral
ollama pull [embedder_name]  # e.g., ollama pull mxbai-embed-large
```
Find available models [here](https://ollama.com/models).

3. **Run Ollama**:
```bash
ollama serve
```

4. **Clone the repo**
```bash
git clone https://github.com/AbhijithP96/pdf-rag-assistant.git
cd pdf-rag-assistant
```
5. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

6. **Run the Streamlit app**:
```bash
streamlit run app.py
```

## How to Use
1. Open your browser and navigate to `http://localhost:8501`.
2. Upload a PDF file using the provided interface.
3. Ask questions about the PDF content in the chat interface.

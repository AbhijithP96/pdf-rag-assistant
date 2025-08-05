import streamlit as st
import tempfile
import chromadb
import asyncio

from llama_index.readers.file import PDFReader
from llama_index.core.readers import SimpleDirectoryReader
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import VectorStoreIndex

import nest_asyncio

class DocLoader:

    def __init__(self):
        self.embed_model = st.session_state.embed_model
        self.infer_model = st.session_state.infer_model

    def read(self, file):

        parser = PDFReader()

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(file.getbuffer())
            tmp_file_path = tmp_file.name

        file_extractor = {'.pdf': parser}
        reader = SimpleDirectoryReader(
            input_files=[tmp_file_path],
            file_extractor=file_extractor
        )

        documents = reader.load_data()
        st.success('☑️ Document Loaded')

        return documents
    
    def generate_db(self):

        db = chromadb.PersistentClient('../data/chroma/')
        collection = db.get_or_create_collection(name='demo')
        vector_store = ChromaVectorStore(chroma_collection=collection)

        st.success('☑️ Chroma DB Initialized')

        return vector_store

    async def get_index(self, file):

        documents = self.read(file)
        vector_store = self.generate_db()

        pipeline = IngestionPipeline(
            name = "demo-rag",
            transformations=[
                SentenceSplitter(),
                self.embed_model
            ],

            vector_store=vector_store
        )

        nodes = await pipeline.arun(documents = documents)

        index = VectorStoreIndex.from_vector_store(vector_store=vector_store, embed_model=self.embed_model)

        st.success('☑️ Document Indexed')

        return index

def infer(prompt):

    if 'index' not in st.session_state:
        loader = DocLoader()
        st.session_state.index = asyncio.run(loader.get_index(st.session_state.uploaded))
        
    nest_asyncio.apply()
    query_engine = st.session_state.index.as_chat_engine(
        llm=st.session_state.infer_model,
        response_mode="tree_summarize",)
    
    response = query_engine.chat(prompt)

    return response
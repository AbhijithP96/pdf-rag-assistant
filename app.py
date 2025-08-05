import streamlit as st

from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

from frontend.options import init_option_gui
from frontend.chat import init_chat_gui

def main():

    # set page layout
    st.set_page_config(
        page_title='📓 PDF Assistant',
        layout='wide')
    
    st.header('PDF Assistant')
    st.markdown('### Chat about your pdf here')
    
    # initialize the ollama models
    init_option_gui()

    if 'uploaded' not in st.session_state:
        st.markdown('### Upload a pdf to start chatting!!!')

    else:

        with st.spinner(text='Initializing'):
            init_and_validate_models()

        if 'embed_model' in st.session_state and 'infer_model' in st.session_state:
            # second column contains the chat interface
            init_chat_gui()

        else:
            st.warning('Model Initialization Error')

def init_and_validate_models():

    if 'embed_model' not in st.session_state:
        embed_model = OllamaEmbedding(model_name="mxbai-embed-large")
        st.session_state.embed_model = embed_model

        try:
            embedding = embed_model.get_text_embedding('Hello World')
            st.success('☑️ Embedding Model Loaded')
        
        except Exception as e:
            st.warning(f'Error Occured while calling the embedding model: {str(e)}')

    if 'infer_model' not in st.session_state:
        infer_model = Ollama(model='llama2', request_timeout=300.0)
        st.session_state.infer_model = infer_model

        try:
            response = infer_model.complete('How are you')
            st.success('☑️ Inference Model Loaded')
        except Exception as e:
            st.warning(f'Error occured while connecting the inference model: {str(e)}')
    

if __name__ == '__main__':
    main()
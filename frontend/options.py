import streamlit as st


def init_option_gui():

    with st.sidebar:
        st.markdown('## Options')

        file = st.file_uploader(label='Upload PDF', type=['pdf'], accept_multiple_files=False)

        if file:
            st.session_state.uploaded = file


        if st.button(label='Clear Session'):
            st.session_state.clear()
            st.rerun(scope='app')

        

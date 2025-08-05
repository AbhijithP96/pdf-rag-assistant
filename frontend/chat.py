import streamlit as st

from backend.infer import infer

def truncate_history(history, max_token = 4096):

    token_count_approx = sum(len(m['content'])//4 for m in history) # 1 token = 4 chars from openAI.

    while token_count_approx > max_token and len(history) > 1:
        removed = history.pop(1) # keeping the system prompt
        token_count_approx -= len(removed['content'])//4

    return history

def init_chat_gui():

    if 'chat_history' not in st.session_state:

        system_prompt = """
                        You are an AI assistant that searches the indexed document to provide
                        relevant information to the question asked by the user.
                        """
        st.session_state.chat_history = [{
            'role': 'system', 'content' : system_prompt
        }]

        response = infer(system_prompt)

    user_input = st.chat_input('Ask Something')

    if user_input:

        st.session_state.chat_history.append({
            'role' : 'user', 'content': user_input
        })

        write_to_ui()
        # truncate history
        #st.session_state.chat_history = truncate_history(st.session_state.chat_history)

        with st.spinner("Thinking..."):
            response = infer(user_input)

        if response:
            st.session_state.chat_history.append({
                'role': 'assistant', 'content': response
            })

            write_to_ui()


def write_to_ui():
    for msg in st.session_state.chat_history:
            
            if msg['role'] == 'user':
                with st.chat_message(name='user', avatar='👦'):
                    st.markdown(msg['content'])

            elif msg['role'] == 'assistant':
                with st.chat_message(name='assistant', avatar='🤖'):
                    st.markdown(msg['content'])
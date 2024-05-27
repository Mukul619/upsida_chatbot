import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
import os
import pandas as pd
import numpy as np
from streamlit.components.v1 import html
import random
import yaml

st.set_page_config(page_title="Chatbot",
                   )

#Chatbot Ques Answers List
with open('ques_ans_list.yaml', 'r') as yaml_file:
    ques_ans_dict = yaml.safe_load(yaml_file)

def get_response(prompt):
    response = 0
    if prompt in ques_ans_dict.keys():
        response = ques_ans_dict[prompt]
        return response
    else:
        return "Sorry, I do not know the answer of this question!"



## generated stores AI generated responses
if 'generated' not in st.session_state:
    # st.session_state['generated'] = ["Hi I'm your assistant, How may I help you?"]
    st.session_state['generated'] = ["Hi"]
## past stores User's questions
if 'past' not in st.session_state:
    # st.session_state['past'] = ['Hi!']
    st.session_state['past'] = ["Hi"]

# Layout of input/response containers
input_container = st.container()
# colored_header(label='', description='', color_name='blue-30')
response_container = st.container(height = 400)

# User input
## Function for taking user provided prompt as input
def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text

# Response output
## Function for taking user prompt as input followed by producing AI generated responses
def generate_response(prompt):
    response = get_response(prompt)
    return response

## Conditional display of AI generated responses as a function of user provided prompts
with response_container:
    user_input = get_text()
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        prompt_length = len(st.session_state['generated'])


        for i in range(len(st.session_state['generated'])-1,0,-1):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
import os
from dotenv import load_dotenv,find_dotenv

from groq import Groq

status=load_dotenv(find_dotenv(),override=True)

print(status)

#key=os.getenv('GROQ_API_KEY')

#print(key)

import streamlit as st

st.title('THIS IS A CHATBOT')


question=st.text_input('enter your question')

client=Groq()

response=client.chat.completions.create(
    model='llama-3.1-8b-instant',
    messages=[
        {"role":"system","content":"You are a helpful assistant"},
        {"role":"user","content":question}
    ])

final_response=response.choices[0].message.content

if st.button('CLICK ME'):
    st.write(final_response)
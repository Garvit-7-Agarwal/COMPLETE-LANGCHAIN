from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate,load_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

template = load_prompt('template.json')
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash',temperature=0.1)

cricketer_name = st.selectbox("Select Player name",["Select....","Virat Kholi","Sachin Tendulkar","MS Dhoni","Rohit Sharma","Hardik Pandya","Sanju Samson"])
style_input = st.selectbox("select style",["select...","Cricket statatics","Bank Balance","About Family","About childhood journey"])
length_input = st.selectbox("slect length",["select...","Small (1-2 paragraphs)","Medium (3-4 paragraphs)","Large (5-6 paragraphs)"])


chain = template|model

if st.button('Summarise'):
    result = chain.invoke({
        'cricketer_name':cricketer_name,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.content)



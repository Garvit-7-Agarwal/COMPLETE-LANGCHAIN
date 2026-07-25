from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash',temperature=0.1)

st.header("Cricket Research....")

cricketer_name = st.selectbox("Select Player name",["Select....","Virat Kholi","Sachin Tendulkar","MS Dhoni","Rohit Sharma","Hardik Pandya","Sanju Samson"])
style_input = st.selectbox("select style",["select...","Cricket statatics","Bank Balance","About Family","About childhood journey"])
length_input = st.selectbox("slect length",["select...","Small (1-2 paragraphs)","Medium (3-4 paragraphs)","Large (5-6 paragraphs)"])

# template 

template = PromptTemplate(
    template="""
        write the information about a "{cricketer_name}" with the following specifications:
        Title:"{style_input}"
        length:"{length_input}"
""",
input_variables=['cricketer_name','style_input','length_input'],
validate_template=True
)


# uses of prompt template i

# 1) we can also use fstring instead of prompt template but prompt template provides more features rather than fstring like suppose in prompt template there is an extra input called name and it is not passed in the input parameter of the prompt template and if we use one more parameter called 'validate_template=True' then prompt template will throw an error but if we using the fstring then it will create problem while deploying the code on website 

# 2) we can also reuse the prompt created through prompt template,we can create another file paste the prompt there and then convert a json file through that prompt which can be use everywhere.

## Creating prompt through template.json

## template = load_prompt('template.json')


prompt = template.invoke({
    'cricketer_name':cricketer_name,
    'style_input':style_input,
    'length_input':length_input
})

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)
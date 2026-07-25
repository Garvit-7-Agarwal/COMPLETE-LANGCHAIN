from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate 
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "write a detailed report on the topic {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="write a 5 line summary on the text {text}",
    input_variables=['text']
)

chain = prompt1 | model | parser | prompt2 | model | parser

# result = chain.invoke({'topic':'LBW in Cricket'})
# print(result)
chain.get_graph().print_ascii()
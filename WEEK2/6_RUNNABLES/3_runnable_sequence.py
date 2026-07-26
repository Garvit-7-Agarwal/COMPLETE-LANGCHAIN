from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence 
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template='write a joke of 1 line about {topic}',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke {joke} in 1 line',
    input_variables=['joke']
)

chain1 = RunnableSequence(prompt1,model,parser,prompt2,model,parser)
chain2 = prompt1|model|parser|prompt2|model|parser

# borh chain1 and chain2 are doing samework 
print("Chain 1 : ",chain1.invoke({'topic':'cricket'}))
print("Chain 2 : ",chain2.invoke({'topic':'cricket'}))

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
# Here i have used the genai chat model becuase it happens that free source model (Hugging face) api does not work sometimes so to avoid that i am using genai 
# Parser is used for the model who does not generate the output in structure so stroutputparser extracts the text from the output of the llms 

load_dotenv()

parser = StrOutputParser()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt1 = PromptTemplate(
    template="write a report on the topic {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template= "Write a summary on the topic {topic}",
    input_variables=['topic']
)

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic':'Black Hole'})
print(result)
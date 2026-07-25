# Structured output parser is an ouput parser in langchain that helps extract structured json data from llm responses based on predefined field schema 

# it works by defining a list of fields that the model should return, ensuring the output follows a structured format

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_classic.output_parsers import StructuredOutputParser,ResponseSchema
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

schema = [
    ResponseSchema(name='fact1',description="Fact 1 about the topic"),
    ResponseSchema(name='fact2',description="Fact 2 about the topic"),
    ResponseSchema(name='fact3',description="Fact 3 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="give 3 facts about {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({'topic':'cricket'})
print(result)

# Disadvantage 
# 1) There is not data validation 

# pydantic output parsser is a structured output parser in langchain that uses pydantic models to enforce schema validation when processing llm responses

# pydantic ouput parser = structured output parser + data validation 

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

class Person(BaseModel):
    name:str = Field("Name of the person")
    age: int = Field(gt=18,description="Age of the person")
    city: str = Field(description="name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name,age,city of a fictional {place} Person \n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions}

)

chain = template | model | parser

result = chain.invoke({'place':'american'})

print(result)



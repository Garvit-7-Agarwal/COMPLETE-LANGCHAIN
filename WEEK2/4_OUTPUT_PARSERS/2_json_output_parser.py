from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name , age and city of the fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

#1)
# prompt = template.format()
# result = model.invoke(prompt)
# print(result)

# final_result = parser.parse(result.content)
# print(final_result)

#2)
# chain = template|model|parser
# result = chain.invoke({})
# print(result)

# Now the problem of jsonoupparser is that we can enforce a schema means we can't force for a particular schema 
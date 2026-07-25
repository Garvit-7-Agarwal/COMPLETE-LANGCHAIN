from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser # This is used because we can to extract the string fron the output not that how much token and warning and all

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
parser = StrOutputParser()

template = PromptTemplate(
    template="Write all records of a player {player} in the IPL history in very short",
    input_variables=['player']
)

chain = template | model | parser

# result = chain.invoke({'Virat Kholi'})
# print(result)

chain.get_graph().print_ascii()
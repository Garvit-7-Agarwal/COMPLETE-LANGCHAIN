# Runnables in LangChain are standardized components that implement a common interface for executing a task. They take an input, perform an operation (such as prompting an LLM, formatting data, parsing output, or calling another runnable), and return an output. They can be chained together to build AI workflows.

from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI(model='gemini-2.5-flash')

prompt = PromptTemplate(
    input_variables = ['topics'],
    template="Suggest a catchy blog title about {topics}."
)

topic = input("Enter the topic")

formatted_prompt = prompt.format(topics=topic)

print("AI : ", model.invoke(formatted_prompt))
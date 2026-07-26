from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence,RunnablePassthrough,RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='write a joke in 1 line , in simple english on the {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the joke in simple english in 1 line , joke -> {text}',
    input_variables=['text']
)

joke_chain = RunnableSequence(prompt1,model,parser)

paralle_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2,model,parser)
})

final_chain = RunnableSequence(joke_chain,paralle_chain)

print(final_chain.invoke({'topic':'AI'}))
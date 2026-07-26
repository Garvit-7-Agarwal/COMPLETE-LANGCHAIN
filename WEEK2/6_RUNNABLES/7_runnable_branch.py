# RunnableBranch is used to choose one of multiple chains based on a condition.

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch, RunnableLambda

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

parser = StrOutputParser()

report_gen_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))

# Flow of the above code 

# User gives topic
#       ↓
# report_gen_chain
#       ↓
# Generate detailed report
#       ↓
# RunnableBranch checks word count
#       ↓
#    ┌───────────────┴───────────────┐
#    ↓                               ↓
# > 300 words                    ≤ 300 words
#    ↓                               ↓
# Summarize report              Return report unchanged
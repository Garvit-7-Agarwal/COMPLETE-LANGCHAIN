# Now we are going to make parallel chain in which there is a large document on some topiic and user will upload it and then parallely model will prepare the notes and model will make the quiz from that document and then we will pass both the things to model for fiinal output 

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template="Write 5 to 6 lines notes from the given text {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Make 5 to 6 MCQS from the given text {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="Merge the note and quizes into a single document , notes -> {notes} , quizes -> {quizes}",
    input_variables=['quizes','notes']
)

parallel_chain = RunnableParallel({
    'notes': prompt1 | model | parser,
    'quizes': prompt2 | model | parser
})

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain

text = """
Cricket is a globally beloved bat-and-ball sport played between two teams of eleven players on a large, meticulously maintained grass field. Originating in southeast England, the sport is governed by the International Cricket Council and spans multiple engaging formats, including thrilling T20s, one-day internationals, and traditional five-day Test matches.  At the heart of the ground lies the pitch, a strip of clay where the bowler delivers the ball toward the batsman defending the wickets, aiming to restrict runs or dismiss the batsmen to secure victory. Far more than a simple test of athletic ability, cricket demands deep strategic thinking, razor-sharp reflexes, and steadfast mental discipline. Whether played professionally in packed international stadiums or casually in neighborhood parks and narrow streets, cricket profoundly unites people across all cultures. It teaches essential life values such as cooperation, team spirit, and respect for the rules, often referred to as the "Spirit of the Game." For millions of passionate fans and young players, the sport is not just a game, but an emotional journey of camaraderie, fierce competition, and national pride. By cultivating physical fitness and strategic problem-solving, cricket continues to inspire generations who celebrate legendary players and eagerly await every major international tournament
"""
result = chain.invoke({'text':text})
print(result)
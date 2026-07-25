from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGoogleGenerativeAI(model = 'gemini-2.5-flash',temperature=0.1)


## First we will create our schema means we will use typed dict library and will create the format of output we want from the llm 

# Schema 

class Review(TypedDict):

    summary : str
    sentiment : str


structured_model = model.with_structured_output(Review)

result = structured_model.invoke('Great TV showroom with an excellent variety of high-end and budget models on display. The staff provided a thorough, professional demonstration and offered a fantastic deal on my purchase.')

print(result)
print(result['summary'])
print(result['sentiment'])



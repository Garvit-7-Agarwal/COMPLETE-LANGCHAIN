from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict,Annotated
from dotenv import load_dotenv

load_dotenv()

# Schema 
class review(TypedDict):

    summary:Annotated['str','A brief summary of the review']
    sentiment:Annotated['str','Return sentiment of the review']

# Here it might be happen that llm does not get understand by just seeing only summary and sentiment keyword , so for that we attach more description about the keyword using Annotated 
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
structured_model = model.with_structured_output(review)

result = structured_model.invoke('Great TV showroom with an excellent variety of high-end and budget models on display. The staff provided a thorough, professional demonstration and offered a fantastic deal on my purchase.')

print(result)
print(result['summary'])
print(result['sentiment'])

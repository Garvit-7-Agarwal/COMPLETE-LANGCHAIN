from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from typing import Optional,Literal

load_dotenv()


# Schema 
class Student(BaseModel):

    key_themes : list[str] = Field(description="Write down all the key themes discussed in the review.")
    summary: str = Field(description="A breif Sumarry of the review")
    sentiment: Literal["pos","neg"] = Field(description="Return sentiment of the review either negative,positive,neutral")
    pros: Optional[list[str]] = Field(default=None,description="Write all the positive points from the reviews")
    cons : Optional[list[str]] = Field(default=None,description="Write all the cons from the reviews")
    name: Optional[str] = Field(default=None,description="Write the name of the person who give the review")

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

structured_model = model.with_structured_output(Student)

review = """
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Garvit Agarwal
"""

result = structured_model.invoke(review)

print(result)

# // when we create our project in too many languages like backend is in javascript and frontend is in python then for schema we use json schema which can be use for any language
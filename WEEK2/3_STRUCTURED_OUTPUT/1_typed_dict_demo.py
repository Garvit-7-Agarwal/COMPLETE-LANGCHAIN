# in langchain structured output refers to the practice of having language models return responses in a well defined data format(from example json), rather than free-form text. This makes the model output easier to praise nd work with programmatically 
 
# why do we need structured output ?

# 1) Data extraction : we can extract data like name,title,sentiments.
# 2) API 
# 3) the output given by are free text and if we use structured output then we provide the ouput to other tools of agents 

from typing import TypedDict

class Person(TypedDict):

    name:str
    age:int

new_per : Person = {'name' : 'Garvit Agarwal','Age' : 18}

# here new_per is the dictionary only it is not the object of the class Person but in pydantic we create objects
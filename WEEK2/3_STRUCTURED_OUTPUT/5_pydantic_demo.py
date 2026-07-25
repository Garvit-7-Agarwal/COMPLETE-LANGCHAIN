
from pydantic import BaseModel

# class Student(BaseModel):

#     name:str 

# new_student = {'name':'Garvit'}

# student = Student(**new_student)
# print(student)

# # # **dictionary unpacks a dictionary into keyword arguments.

# # # Student(**new_student) is exactly the same as Student(name="Garvit").

# # # TypedDict only tells type checkers what keys and value types a dictionary should have; it remains a plain dict.

# # # BaseModel creates a real object, validates the data at runtime, and lets you access fields as attributes (e.g., student.name).

# # ############ features of pydantic librRY 
# # 1) we can set default values in class

# class Student2(BaseModel):

#     name:str = "Garvit" # default of the name is garvit 

# # # 2) Optional Fields 

from typing import Optional
# class Student(BaseModel):

#     name:str 
#     age:Optional[int] = None # By using optional here we can set the age field to None 
#     # Here the optional does not have the same meaning as in Typed dictionary 
#     # here the optional field does not mean that the field is not required like it was in typed dict , here it means that you can set the field value to none without optional we can't set it default value to none 

# # A field is simply a variable (attribute) inside a class that stores data.

# # 3) Coerce :- it means that pydantic is smart enough and suppose the field 'age' data is int but if we are passing the string the pydantic automatically will convert it into int 

# class Student3(BaseModel):

#     name:str = "Garvit" 
#     age:Optional[str] = None


# new_student2 = {
#     "name":"Garvit",
#     "age":"19"
# }

# s1 = Student3(**new_student2)
# print(s1)

# # # 4) Built in validation 

from pydantic import EmailStr

# class Student4(BaseModel):

#     name:str = "Garvit" 
#     age:Optional[int] = None
#     email:EmailStr 

# new_st = {
#     "name":"Garvit",
#     "age":12,
#     "email":"abc@gmail.com"
# }

# s2 = Student4(**new_st)

# print(s2)

#5) Field,descroption

from pydantic import Field

class Student5(BaseModel):

    name:str = "Garvit" 
    age:Optional[int] = None
    email:EmailStr 
    cgpa:float = Field(gt=0,lt=10,default = 5,description="Students college cgpa")

new_st5 = {
    "name":"Garvit",
    "age":12,
    "email":"abc@gmail.com",
    "cgpa":9.0
}

s5 = Student5(**new_st5)
print(s5)

# Conerting to json 

s5_dict = dict(s5)
print(s5_dict)
print(s5_dict['age'])
s5_json = s5.model_dump_json()
print(s5_json)

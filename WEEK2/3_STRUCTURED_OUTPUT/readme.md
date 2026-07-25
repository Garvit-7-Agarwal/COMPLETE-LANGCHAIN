we have seen three things to create structured output 
1) typed_dict -> return dictionary
2) Pydantic -> returns pydantic object 
3) Json_schema -> Returns dictionary 

now when to use what 

1) Typed_dict

1-1) You do not need validation(eg: checking numbers are positive)
1-2) You trust llm to return correct data 

2) Pydantic 

2-1) You need data validation 
2-2) you need default values if llm misses fields 
2-3) you want automatic type conversion ("100" -> 100)

3) Json_schema 

3-1) You don not want to extract extra python librart 
3-2) you need validation but don't need python objects 
3-3) You want to define structure in a standard json format
3-4) You want to same schema across to many languages 

there is also on more important point is that 

we can also define a methods when we call a function  with_structurd_output(methods)

1st method is json mode which returns json format data 
2nd method is function calling in this when we make agents then this helps most
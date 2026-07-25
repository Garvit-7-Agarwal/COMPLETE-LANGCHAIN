there are two different different thing first is static prompt ui and dynamic prompt ui
1) static prompt ui
    in this the user writes complete thing what the user want to search , and based on that the user get the output, in this it might be happen that all use get different outputs because single change in prompts gives different outputs.

2) Dynamic prompt ui
    in this the user mainly select the title and more features through drop down menu and there is fixed prompt which goes to llm and then mostly all the user gets the same output because for all use the prompt is same 


There is an difference between ChatPromptTemplate and PromptTemplate Both get import from langchain_core.prompts but PromptTemplate is used for single type of messages but ChatPromptTemplate is used to create MultipleTypeofConversation(ChatBot) 

Like if we are creating Chatbot Then we need AI message, System Message , Human Message -> (1) if we are creating just simple Not dynamic then we can make an list of history and then append the messages no need to use Prompt Template or ChatPromptTemplate 2) If we are Building chatbot with dynamic prompt then we need to use ChatPromptTemplate and passes all the Messages (In this try to use tuple and pass messages like this 

chat_template = ChatPromptTemplate([
    ('system' : .............), 
    ('human' : ........... )
])

)



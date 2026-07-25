# ### Structured Output vs Output Parsers

# **Structured Output:** Used when the LLM/model supports generating structured output directly according to a predefined schema. The model returns the response in the required structure.

# **Output Parser:** Used when the model does not natively support structured output. The model first generates a text response, and the output parser then converts/parses that response into the required structured format.

# **In short:**

# > **Structured Output → Model directly generates structured data.**
# > **Output Parser → Model generates text, and the parser converts it into structured data.**

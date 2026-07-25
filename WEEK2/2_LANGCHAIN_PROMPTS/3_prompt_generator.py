from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
        write the information about a "{cricketer_name}" with the following specifications:
        Title:"{style_input}"
        length:"{length_input}"
""",
input_variables=['cricketer_name','style_input','length_input'],
validate_template=True
)

template.save('template.json')
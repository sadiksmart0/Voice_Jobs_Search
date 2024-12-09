from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser


def is_valid_job(state):
    print("+++++++++++++++++++ VALIDATING JOB TITLE ++++++++++++++++++++")
    system = """You are a career coach and job expert. Respond with 'yes' ONLY if the input '{statement}' is a valid job title. 
    If the input is NOT a valid job title, simply return the input '{statement}' without any additional words or explanations.
    If it is a valid job title, respond with JUST 'YES' and nothing else.
    """

    
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system),
            (
                "human",
                "Respond with 'yes' only if the following is a valid job title, otherwise return the statement:\n\n{statement}"
            ),
        ]
    )
    
    llm = OllamaLLM(model="mistral:instruct", temperature=0.7)
    
    job_picker = prompt | llm | StrOutputParser()

    speech = state["speech"]
    
    response = job_picker.invoke({"statement": speech})
    print(F"Is job title really valid: {response}")

    return {"decision": response}
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser

def get_job_title(state):
    print("+++++++++++++++++++ EXTRACTING JOB TITLE ++++++++++++++++++++")
    system = """You are a career coach, helping people to figure out the best job for them. You will get a string string of sentences with a particular job stated,
    Your primary goal is to figure out what job the person said(e.g I want a junior product manager role, return just "Junior Product Manager"). 
    If it is not stated clearly or ambigous, Tell the person to state the job title he/she is pursuing to land a role"""
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system),
            (
                "human",
                "Here is the persons statement: \n\n {statement} \n return only the specified job title. No Explanation!!!",
            ),
        ]
        )
    
    llm = OllamaLLM(model="mistral:instruct", temperature=0.7)
    
    job_picker = prompt | llm | StrOutputParser()
    
    speech = state
    #speech = state["speech"]
    
    response = job_picker.invoke({"statement": speech})
    print(response)
    
    return {"title": response}
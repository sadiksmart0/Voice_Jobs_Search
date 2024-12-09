import warnings
warnings.filterwarnings("ignore")

from selenium.webdriver.remote.webdriver import WebDriver
from langgraph.graph import MessagesState
from langgraph.graph import END, StateGraph, START
from typing import List
from typing_extensions import TypedDict
from search_decision import search_decision
from play_result import play_audio

from record_prompt_and_transcribe import record_audio_until_stop
from is_job_valid import is_valid_job
from generate import generate
from show_result import show_result
from get_job_title import get_job_title

from load_login_page import load_login_page
from login import login_to_linkedin
from job_search import job_search
from find_match import find_match
from back import back


class GraphState(TypedDict):
    driver: WebDriver
    speech: str
    decision: str
    title: str
    jobs: dict
    best_fit: List[dict]
    suggested_alternatives: List[dict]
    generation: str


workflow = StateGraph(GraphState)

# NODE DEFINITION
workflow.add_node("voice_prompt", record_audio_until_stop)
workflow.add_node("get_job_title", get_job_title)
workflow.add_node("is_valid_job", is_valid_job)
workflow.add_node("load_page", load_login_page)
workflow.add_node("login", login_to_linkedin)
workflow.add_node("job_search", job_search)
workflow.add_node("find_match", find_match)
workflow.add_node("back", back)
workflow.add_node("generate", generate)
workflow.add_node("show_result", show_result)
workflow.add_node("play", play_audio)
workflow.add_node("replay", play_audio)

# BUILD GRAPH
workflow.add_edge(START, "voice_prompt")
workflow.add_edge("voice_prompt", "get_job_title")
workflow.add_edge("get_job_title", "is_valid_job")
workflow.add_conditional_edges(
    "is_valid_job",
    search_decision,  # This should be a callable function
    {
        "search": "load_page",
        "back": "back",
    },
)
workflow.add_edge("load_page", "login")
workflow.add_edge("login", "job_search")
workflow.add_edge("job_search", "find_match")
workflow.add_edge("find_match", "generate")
workflow.add_edge("back", "replay")

workflow.add_edge("replay", "voice_prompt")
workflow.add_edge("generate", "show_result")
workflow.add_edge("show_result", "play")
workflow.add_edge("play", END)

app = workflow.compile()




from pprint import pprint

# Run
inputs = {
    "driver": None,
    "speech": None,
    "decision": None,  # Initialize as an empty list or provide relevant documents
    "title": None,  # Default value
    "jobs": {},  # Default value
    "best_fit":[],
    "suggested_alternatives": [],
    "generation": None
}
for output in app.stream(inputs):
    for key, value in output.items():
        # Node
        pprint(f"Node '{key}':")
        # Optional: print full state at each node
        # pprint.pprint(value["keys"], indent=2, width=80, depth=None)
    pprint("\n--------\n")



if value["generation"] is not None:
    pprint(value["generation"])
    
pprint(value["decision"])
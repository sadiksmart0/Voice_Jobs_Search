from langchain_ollama import OllamaLLM

local_llm = OllamaLLM(model="mistral:instruct", temperature=0.7)
def generate(state):
    print("<----------------------GENERATING----------------------------->")
    best_fit = len(state["best_fit"])
    suggested_alternatives = len(state["suggested_alternatives"])
    prompt = f"Write concisely, in an enthusiastic voice based on the number of best fit jobs {best_fit} found and in an Encouraging voice for alternative jobs {suggested_alternatives} found. Emoji"
    generation = local_llm.invoke(prompt)
    
    return {"generation": generation}

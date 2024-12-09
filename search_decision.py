
def search_decision(state):
    print("+++++++++++++++++++ SEARCH DECISION ++++++++++++++++++++")
    decision = state["decision"].strip().lower()
    
    if decision == "yes":
        return "search"
    else:
        return "back"
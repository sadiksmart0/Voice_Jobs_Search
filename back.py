def back(state):
    print("+++++++++++++++++++ BACK ++++++++++++++++++++")
    decision = state["decision"]
    generation = state["generation"]
    return {"generation": generation, "decision": decision}
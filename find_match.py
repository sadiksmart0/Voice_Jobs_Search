from job_filter import filter

def find_match(state):
    print("<---------------------MATCHING------------------------------>")
    jobs = state["jobs"]
    best_fit, suggested_alternatives = [], []
    

    for title, info in jobs.items():
        fit  = filter(title, info["description"]).strip().lower()
        if fit == "no":
            print("<---Comment: Not the best for you!!------>")
            suggested_alternatives.append({title: info})
        else:
            print("<---Comment: The best fit for you ---------->")
            best_fit.append({title: info})

    return {"best_fit": best_fit, "suggested_alternatives": suggested_alternatives}

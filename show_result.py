

def show_result(state):
    generation = state["generation"]
    print("+++++++++++++++++++ JOBS ++++++++++++++++++++\n\n")
    best_fit = state["best_fit"]
    suggested_alternatives = state["suggested_alternatives"]
    
    print("Here are the Jobs that could best fit your profile\n")
    print("++++++JOB TITLE+++++++        |      ++++++JOB URL +++++++|\n\n")
    for job in best_fit:
        for title, details in job.items():
            print(f""" {title}                 | URL ==>     {details["url"]}""")

    print("Here are alternatives to your profile\n")
    print("++++++JOB TITLE+++++++        |      ++++++JOB URL +++++++|")
    for job in suggested_alternatives:
        for title, details in job.items():
            print(f"""{title}                 |      {details["url"]}""")
    return {"generation": generation}

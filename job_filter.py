from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from load_and_embed_resume import load_document, split_document, embed_docs

FILE_PATH="/Users/abubakarmuktar/Documents/Data Analyst Job Resumes/Abubakar_M_DA_Resume.pdf"
URL="https://sadiksmart0.github.io/about.html"
CHROMA_PATH="/Users/abubakarmuktar/Documents/RAG_Projects/Voice_Jobs_Search/ChromaDB"

docs = load_document(FILE_PATH)
chunks = split_document(docs)
vectore_store = embed_docs(chunks, CHROMA_PATH)




def filter(title, description):
    grader = OllamaLLM(model="mistral:instruct", temperature=0.7)

    # Correctly formatted system message
    system = """
    You are an expert recruiter. Use the job title "{title}" and job description "{description}" to assess if the job aligns well with the
    user's resume/CV: {context}, including their history of work and experiences. Provide a grade of 'Yes' if it is a good fit, or 'No' if it is not.
    Only respond with 'Yes' or 'No'; no explanations are needed.
    """

    # Prompt template with placeholders
    grade_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system),
            (
                "human",
                "Job Title: {title}\n\n"
                "Job Description: {description}\n\n"
                "Based on the user's resume/CV: {context} and work experience, is this job a good fit? Respond with 'Yes' or 'No'."
            ),
        ]
    )

    # Ensure `vector_store` and `as_retriever` are defined and accessible
    retriever = vectore_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 5},
    )

    # Construct the grader chain properly
    grader_chain = (
        grade_prompt
        | grader
        | StrOutputParser()
    )

    # Retrieve context and invoke the chain
    context = retriever.invoke(description)
    result = grader_chain.invoke(
        {"title": title, "description": description, "context": context}
    )
    
    return result
# VJS: Voice-Driven Job Search Assistant 🚀  

### What if you could search for a job with just a voice prompt?  

Welcome to **VJS (Voice Job Search)**, an AI-powered concept app that transforms your job-hunting experience. Speak your job preferences, and VJS will handle the rest—scouring LinkedIn, analyzing matches against your profile, and even narrating the results with a voice that embodies confidence and excitement (or whatever tone fits the outcome!).  

### 🔍 How Does It Work?  

1. **Speak Your Search**  
   Simply give a voice command like:  
   > *"Find me software engineer jobs in New York"*  

2. **AI Takes Charge**  
   - **Transcription**: Your voice is transcribed using the Whisper model.  
   - **Job Title Validation**: Our Ollama model checks for a valid job title and confirms it.  
   - **Search Automation**: Once validated, VJS logs into LinkedIn and performs a job search.  

3. **Find the Perfect Match**  
   - **Resume Matching**: VJS compares job results to your profile/resume using AI filtering.  
   - **Prioritized Results**: Jobs are categorized into “Best Fit” and “Alternatives.”  

4. **Hear the Outcome**  
   - Using the **Suno/Bark model**, VJS generates a vocalized summary of the results, with tone and emotion tailored to the findings.  
   - Results are printed alongside clickable job URLs for easy access.  

### 🎥 [Watch the Full Walkthrough](https://youtu.be/UejpclVWl4I)  
Check out this detailed video to see VJS in action!  

---

### 🛠️ Key Tools and Technologies  

- **[Selenium](https://www.selenium.dev/)**: Automates LinkedIn job searches.  
- **[Sounddevice](https://python-sounddevice.readthedocs.io/)**: Records voice prompts.  
- **Threading**: Keeps operations efficient with parallel processes.  
- **[Whisper Model](https://huggingface.co/)**: Converts your voice to text.  
- **[Ollama Mistral Instruct](https://ollama.com/)**: Handles job title validation, filtering, and text generation.  
- **[Suno/Bark](https://github.com/suno-ai/bark)**: Converts text to lifelike speech.  
- **[Ipython Audio](https://ipython.org/)**: Plays audio outputs.  
- **[ChromaDB](https://www.trychroma.com/)**: Stores vector embeddings of your resume/CV for efficient comparisons.  
- **[Langchain](https://www.langchain.com/)**: Orchestrates language model workflows.  
- **[LangGraph](https://langgraph.com/)**: Manages multi-agent interactions.  

---

### ⚡ Getting Started  

To run VJS on your system:  
1. Install [Ollama](https://ollama.com/) and ensure its server is running.  
2. Download the necessary transformer models for **Whisper** and **Suno/Bark**.  
3. Clone the repository:  
   ```bash  
   git clone https://github.com/sadiksmart0/Voice_Jobs_Search.git  
   cd Voice_Jobs_Search  
   ```  
4. Follow the instructions in the README for setup and execution.  

---

### 🌟 Why VJS?  

VJS doesn’t just stop at job search; it personalizes your results, saves time, and adds a human touch with voice interaction. It's like having a virtual career assistant that works tirelessly to find the perfect opportunities for you.  

Ready to make job hunting smarter, faster, and more intuitive? Try **VJS** today!  

**GitHub Repo**: [Voice_Jobs_Search](https://github.com/sadiksmart0/Voice_Jobs_Search)

import time
from IPython.display import Audio 
from IPython.display import display
from transformers import pipeline





def play_audio(state):
    generation = state["generation"]
    decision = state["decision"]
    
    """Plays the audio response from the remote graph with ElevenLabs."""
    pass
    # # Response from the agent 
    text = state["generation"]
    if text is None:
        text = state["decision"] + " You need to be clear and confident about the role/job you are looking for. I am all ears and ready to help you! Let's get started!"

    
      # Load the pipeline
    pipe = pipeline("text-to-speech", model="suno/bark-small", device=-1)
    
    # Generate the audio output
    output = pipe(text)

    display(Audio(output["audio"], rate=output["sampling_rate"], autoplay=True))
   
    
    # Wait till it finish playing
    audio_data = output["audio"]
    sample_rate = output["sampling_rate"]
    audio_duration = len(audio_data) / sample_rate  # Duration in seconds
    time.sleep(audio_duration)
    
    return {"generation":generation, "decision":decision}


    



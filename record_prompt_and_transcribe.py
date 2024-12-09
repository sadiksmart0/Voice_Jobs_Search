import sounddevice as sd
import threading
from transformers import pipeline
import numpy as np

# Load Whisper pipeline and transcribe
whisper_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-medium", device=-1)


def record_audio_until_stop(state):
    print("+++++++++++++++++++ RECORDING AUDIO ++++++++++++++++++++")
    """Records audio from the microphone until Enter is pressed, then transcribes it."""
    audio_data = []  # List to store audio chunks
    recording = True  # Flag to control recording
    sample_rate = 16000  # 16 kHz is adequate for voice

    def record_audio():
        """Continuously records audio until the recording flag is set to False."""
        nonlocal audio_data, recording
        with sd.InputStream(samplerate=sample_rate, channels=1, dtype='float32') as stream:
            print("Recording your instruction... Press Enter to stop.")
            while recording:
                audio_chunk, _ = stream.read(1024)  # Read audio data in chunks
                audio_data.append(audio_chunk)

    def stop_recording():
        """Waits for user input to stop the recording."""
        input("Press Enter to stop recording...\n")
        nonlocal recording
        recording = False

    # Start recording in a separate thread
    recording_thread = threading.Thread(target=record_audio)
    recording_thread.start()

    # Wait for user input in the main thread
    stop_recording()

    # Wait for the recording thread to complete
    recording_thread.join()

    # Stack all audio chunks into a single NumPy array
    audio_data = np.concatenate(audio_data, axis=0)

    # Ensure the audio is 1D (single-channel)
    if audio_data.ndim > 1:
        audio_data = audio_data.squeeze()


    print("Transcribing...")
    result = whisper_pipeline(inputs=audio_data)  # Pass in-memory audio file
    print("Here is the transcription:", result["text"])
    speech = result["text"]
    return {"speech": speech}

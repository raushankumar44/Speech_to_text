import speech_recognition as sr

def audio_to_text(audio_file_path):
    """
    Convert speech from an audio file to text.
    
    Args:
        audio_file_path (str): Path to the audio file (WAV, AIFF, AIFF-C, FLAC)
        
    Returns:
        str: Transcribed text
    """
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    
    try:
        # Load the audio file
        with sr.AudioFile(audio_file_path) as source:
            audio_data = recognizer.record(source)  # Read the entire audio file
            
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio_data)
        return text
        
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    # Get audio file path from user
    audio_path = input("Enter the path to your audio file: ").strip()
    
    # Convert audio to text
    result = audio_to_text(audio_path)
    
    # Print and save the result
    print("\nTranscription Result:")
    print(result)
    
    with open("transcription_result.txt", "w") as f:
        f.write(result)
    print("Result saved to 'transcription_result.txt'")
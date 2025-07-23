from pydub import AudioSegment
import speech_recognition as sr

# Convert mp3 to wav
audio = AudioSegment.from_mp3("my_voice.mp3")
audio.export("converted.wav", format="wav")

# Recognize speech
recognizer = sr.Recognizer()
with sr.AudioFile("converted.wav") as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data)

print("Transcribed Text:")
print(text)

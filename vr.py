import openai
import pyttsx3
import speech_recognition as sr
import time
import traceback

# set key and initialize text to speech engine
openai.api_key = "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"
engine = pyttsx3.init()

def transcribe_audio(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except Exception as e: 
        print("Unknown error has occured", e)

def chat_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_token=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]

def speak_response(text):
    engine.say(text)
    engine.runAndWait()

if __name__ =="__main__":
    mic = sr.Microphone()
    while True:
        print("Say 'testing' to start recording your command")
        with mic as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "testing":
                    # recorded_audio = sr.AudioFile("")
                    filename = "input.wav"
                    print("Say your question")
                    with mic as source:
                    # with recorded_audio as source:
                        # recognizer.adjust_for_ambient_noise(source)
                        # audio = recognizer.record(source)
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())
                    text = transcribe_audio(filename)
                    if text:
                        print(f"You said: {text}")
                        reply = chat_response(text)
                        print(f"GPT-3 says: {reply}")
                        file_path = "C:\\Users\\canda\\Desktop\\capstone\\files\\output.jsx" 
                        with open(file_path, "w") as file:
                            file.write(reply)
                        speak_response(reply)
            except sr.UnknownValueError:
                print("Speech not recognized. Please try again.")
            except sr.RequestError:
                print("Could not request results from the speech recognition service. Please check your internet connection.")
            except Exception as e:
                print("An error occurred: {}".format(e))






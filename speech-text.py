import openai
import speech_recognition as sr

# Set OpenAI API key
openai.api_key = "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"

# Function to transcribe audio
def transcribe_audio(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except Exception as e:
        print("Unknown error has occurred", e)

# Function to get OpenAI response
def get_openai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Function to handle user input and generate response
def handle_user_input():
    print("Enter 1 if you want to upload a file.")
    print("Enter 0 if you want to record a command.")
    choice = input("Choice: ")

    if choice == "0":
        print("Speak something...")
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            reply = get_openai_response(text)
            print("GPT-3 says:", reply)
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio. Please try again.")
        except sr.RequestError as e:
            print("ERROR: {0}".format(e))

    elif choice == "1":
        audio_file = input("Enter the path to the audio file: ")

        try:
            text = transcribe_audio(audio_file)
            print("Transcribed text:", text)
            reply = get_openai_response(text)
            print("GPT-3 says:", reply)
        except Exception as e:
            print("An error occurred:", e)

# Main loop to continuously handle user input
if __name__ == "__main__":
    while True:
        handle_user_input()

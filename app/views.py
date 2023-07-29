from app import app
from flask import render_template, request, redirect, url_for, flash
from app.speech import *


@app.route('/')
def index():
    """Render website's home page."""
    return render_template('index.html')

# Route to handle user speech input from microphone
@app.route('/process_microphone', methods=['POST'])
def process_microphone():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        reply = get_openai_response(text)
        print("GPT-3 says:", reply)
        speak_response(reply)
        return reply
    except sr.UnknownValueError:
        return "Speech recognition could not understand audio. Please try again."
    except sr.RequestError as e:
        return "ERROR: {0}".format(e)

# Route to handle user speech input from uploaded file
@app.route('/process_file', methods=['POST'])
def process_file():
    audio_file = request.files['audio']
    audio_file.save('uploaded_audio.wav')

    try:
        text = transcribe_audio('uploaded_audio.wav')
        print("Transcribed text:", text)
        reply = get_openai_response(text)
        print("GPT-3 says:", reply)
        speak_response(reply)
        return reply
    except Exception as e:
        return "An error occurred: {0}".format(e)


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)

   

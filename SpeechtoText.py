import speech_recognition as sr



choice = input("Enter 1 is you want to upload file.\n" "Enter 0 is you want to record command\n")
print(choice)
a = sr.Recognizer()
if int(choice) == 0:
    print("choice")
    with sr.Microphone() as source:
        print("Speak something...")
        # Adjust for ambient noise if necessary
        a.adjust_for_ambient_noise(source)

        # Capture the audio from the microphone
        audio = a.listen(source)

        try:
            # Use the recognizer to perform speech recognition
            text = a.recognize_google(audio)
            print("text:")
            print(text)
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio please try again")
        except sr.RequestError as e:
            print("ERROR; {0}".format(e))
 
 
if int(choice) == 1:

    audio_file = "hello.wav"  # get audio file uploaded 
    

    with sr.AudioFile(audio_file) as source:
         
        audio = a.record(source)

        try:
            text = a.recognize_google(audio)
            print("text:")
            print(text)
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio please try again")
        except sr.RequestError as e:
            print("ERROR; {0}".format(e))

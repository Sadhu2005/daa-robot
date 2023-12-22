import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f"User said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand what you said.")
            return ""
        except sr.RequestError:
            speak("Sorry, I'm having trouble accessing the speech recognition service.")
            return ""


def assistant():
    speak("Hello! I'm your voice assistant. How can I help you today?")

    while True:
        query = listen()

        if "hello" in query:
            speak("Hi there! How can I assist you?")
        elif "bye" in query or "goodbye" in query:
            speak("Goodbye! Have a great day.")
            break
        else:
            speak("I'm not sure how to help with that.")


if __name__ == "__main__":
    assistant()

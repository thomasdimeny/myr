# speech to text handler
import speech_recognition as sr

# import pyaudio
import ollama
import pyttsx3

# initialize recognizer and text to speech initialization
# recognizer = sr.Recognizer()
myrspeech = pyttsx3.init()


personality = "You are a helpful automaton named Myr, (prounounced meer). You speak in partial sentences with a robotic cadence and lack an understanding of many human sentiments."

ollama.create(model="myr", from_="phi3", system=personality)
for i, name in enumerate(sr.Microphone.list_microphone_names()):
    print(i, name)


def audioIntake():
    print("waiting for input:")
    recognizer = sr.Recognizer()

    with sr.Microphone(device_index=1) as microphone:
        recognizer.adjust_for_ambient_noise(microphone, duration=1)
        try:
            audio = recognizer.listen(microphone, timeout=5, phrase_time_limit=10)
            return recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            print("No input")
            return None
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return None

        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")
            return None


while True:

    userInput = audioIntake()

    if not userInput:
        continue

    print(userInput)
    response = ollama.chat(
        model="myr", messages=[{"role": "user", "content": userInput}]
    )
    myrspeech.say(response.message.content)
    myrspeech.runAndWait()
    # or access fields directly from the response object
    print(response.message.content)

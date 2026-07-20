# speech to text handler
import speech_recognition as sr
import pyaudio
import ollama
import pyttsx3
# from  commandhandler import intake_command
# from commandlibrary import playlist, commandLib

# initialize recognizer and text to speech initialization
# recognizer = sr.Recognizer()
myrspeech = pyttsx3.init()


personality = "You are a helpful automaton named Myr, (prounounced meer). You speak in partial sentences with a robotic cadence and lack an understanding of many human sentiments."
try:
    ollama.show("myr")
except Exception:
    ollama.create(
        model="myr",
        from_="phi3",
        system=personality,
    )
microphone = ""
for i, name in enumerate(sr.Microphone.list_microphone_names()):
    if name == "MacBook Air Microphone":
        microphone = name


def audioIntake():
    print("waiting for input:")
    recognizer = sr.Recognizer()

    with sr.Microphone() as microphone:
        recognizer.adjust_for_ambient_noise(microphone, duration=1)
        try:
            audio = recognizer.listen(microphone, timeout=None, phrase_time_limit=10)
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


loopVar = True
while loopVar == True:
    userInput = audioIntake()

    if not userInput:
        continue

    if "exit program" in userInput:
        loopVar = False
        break

    print(userInput)
    response = ollama.chat(
        model="myr", messages=[{"role": "user", "content": userInput}]
    )
    text = response.message.content
    print(text)
    myrspeech.stop()
    myrspeech.say(text)
    myrspeech.runAndWait()
    # or access fields directly from the respons

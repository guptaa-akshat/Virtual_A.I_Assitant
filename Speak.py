import pyttsx3          # pip install pyttsx3

def Say(Text):
    engine = pyttsx3.init("sapi5")         #(sapi5 is kind of microsoft speaking API)
    voices = engine.getProperty("voices")
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',170)
    print("  ")
    print(f"Jarvis: {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("  ")

import speech_recognition as sr
import pyttsx3
import webbrowser
import sinric

# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()




# Initialize Sinric Pro with your app key and secret key
sinric.init(app_key="YOUR_APP_KEY", secret_key="YOUR_SECRET_KEY")

# Define device IDs (replace with your actual device IDs)
fan_device_id = "YOUR_FAN_DEVICE_ID"
ac_device_id = "YOUR_AC_DEVICE_ID"
light_device_id = "YOUR_LIGHT_DEVICE_ID"

# Define functions to control devices
def turn_on_fan():
    sinric.send_command(fan_device_id, "turn_on")

def turn_off_fan():
    sinric.send_command(fan_device_id, "turn_off")

def turn_on_ac():
    sinric.send_command(ac_device_id, "turn_on")

def turn_off_ac():
    sinric.send_command(ac_device_id, "turn_off")

def turn_on_light():
    sinric.send_command(light_device_id, "turn_on")

def turn_off_light():
    sinric.send_command(light_device_id, "turn_off")

def processcommand(c):
    if "open fan" in c.lower():
        speak("sure")

    elif "open ac" in c.lower():
        speak("sure")

    elif "open home light" in c.lower():
        speak("sure")

    elif "play music" in c.lower():
       speak("okey...,let's play the music")
       webbrowser.open("https://www.youtube.com/watch?v=nFgsBxw-zWQ&list=RDGMEMPipJmhsMq3GHGrfqf4WIqA&start_radio=1&rv=9XXGCb4Eev8") 

    elif "what is my name" in c.lower():
        speak("your name is Umachand mandal")    
    elif command.lower() == "turn on fan":
        turn_on_fan()
    elif command.lower() == "turn off fan":
        turn_off_fan()
    elif command.lower() == "turn on ac":
        turn_on_ac()
    elif command.lower() == "turn off ac":
        turn_off_ac()
    elif command.lower() == "turn on light":
        turn_on_light()
    elif command.lower() == "turn off light":
        turn_off_light()
    else:
        print("Unknown command")

if __name__ == "__main__":
    speak("Listening...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=10, phrase_time_limit=3)
            
            word = recognizer.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yeah")
                with sr.Microphone() as source:
                    print("Active")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)
                    processcommand(command)
                    print(f"Recognized command: {command}")

        except Exception as e:
            print(f"Error: {e}")

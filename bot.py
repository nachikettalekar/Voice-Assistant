import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import requests
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import sys
import time
import pyautogui
import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


# Text to Speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# Speech to Text
def takeCommand(flag=True):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=4, phrase_time_limit=7)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
    except Exception as e:
        if flag:
            return "none"
        else:
            speak("Say that again please...")
        return "none"
    return query


music_paths = {
    'closer': 'C:\\Users\\ASUS\\OneDrive\\Desktop\\Assistant\\Music\\Closer.mp3',
    'faded': 'C:\\Users\\ASUS\\OneDrive\\Desktop\\Assistant\\Music\\Faded.mp3',
    'let me love you': 'C:\\Users\ASUS\\OneDrive\\Desktop\\Assistant\\Music\\Let Me Love You.mp3',
    'stay': 'C:\\Users\\ASUS\\OneDrive\\Desktop\\Assistant\\Music\\Stay.mp3',
    'yummy': 'C:\\Users\\ASUS\\OneDrive\\Desktop\\Assistant\\Music\\Yummy.mp3'
}


# User Greet
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good Morning")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Alex here, how can I help you?")



def TaskExecution():
    while True:
        query = takeCommand().lower()

        # Logic building for tasks
        if "open notepad" in query:
            path = "C:\\Windows\\notepad.exe"
            os.startfile(path)

        elif "close notepad" in query:
            speak("Okay, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "take note" in query or "note" in query or "points" in query:
            speak("What should I write in the note?")
            note_text = takeCommand()
            if note_text != 'none':
                with open('note.txt', 'a') as file:
                    file.write(note_text + '\n')
                speak("Note saved successfully.")

        elif "adobe reader" in query:
            path = "C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC\\Reader\\AcroRd32.exe"
            os.startfile(path)

        elif "close adobe reader" in query or "close reader" in query:
            speak("Okay, closing adobe reader")
            os.system("taskkill /f /t /im AcroRd32.exe")

        elif "open command prompt" in query:
            os.system('start cmd.exe')
            speak("Command prompt has been opened.")

        elif "close command prompt" in query:
            os.system('taskkill /f /im cmd.exe')
            speak("Command prompt has been closed.")

        elif "play music" in query:
            speak("Which song would you like me to play?")
            query = takeCommand().lower()
            if query != 'none':
                found_song = False
                for song in music_paths:
                    if query in song:
                        os.startfile(music_paths[song])
                        speak(f"Now playing {song}")
                        found_song = True
                        break
                if "random song" in query:
                    random_song = random.choice(list(music_paths.keys()))
                    os.startfile(music_paths[random_song])
                    speak(f"Now playing {random_song}")
            # Stop Music
        elif "stop music" in query:
            os.system('taskkill /f /im wmplayer.exe')
            speak("Music has been stopped.")

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP address is {ip}")

        elif "wikipedia" in query:
            speak("Searching on wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif "open youtube" in query:
            speak("What do you want to search on YouTube?")
            query = takeCommand().lower()
            if query != 'none':
                url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
                webbrowser.open(url)
                speak(f"Here are the search results for {query} on YouTube.")
            else:
                speak("Sorry, I didn't catch that.")

        elif "search" in query:
            speak("What do you want to search for?")
            query = takeCommand().lower()
            url = f"https://www.google.com/search?q={query}"
            webbrowser.get().open(url)
            speak(f"Here are the search results for {query}.")

        elif "close youtube" in query or "close google" in query:
            speak("Okay, closing your window")
            os.system("taskkill /f /im chrome.exe")

        elif "weather" in query:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
            else:
                speak(" City Not Found ")

        elif "whatsapp" in query:
            # define the dictionary of contacts
            contacts = {
                "neha": "+918767070798",
                "yojana": "+919322148058",
                "saloni": "+919022569509",
                "shubham": "+917498197506"
            }

            def get_contact_name():
                while True:
                    speak("Who do you want to send the message to?")
                    contact_name = takeCommand().lower()
                    # contact_name = input("Enter the receiver name: ")
                    if contact_name in contacts:
                        return contact_name
                    else:
                        speak("Sorry, I don't recognize that contact. Please try again.")

            def get_message():
                speak("What is the message you want to send?")
                message = takeCommand().lower()
                # message = input("Enter the message you want to send: ")
                return message

            def send_message():
                contact_name = get_contact_name()
                message = get_message()
                phone_number = contacts[contact_name]
                send_hour = int(input("Hours: "))
                send_minute = int(input("Minutes: "))
                kit.sendwhatmsg(phone_number, message, send_hour, send_minute)
                speak(f"Message sent to {contact_name}.")

            send_message()

        elif "take screenshot" in query:
            speak("Please tell me the name for this screenshot file")
            name = takeCommand().lower()
            speak("Please hold on for few seconds, I am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("I am sir, the screenshot is saved in our main folder.")

        elif "ask" in query:
            speak("Sure, what do you want to ask me?")
            question = takeCommand().lower()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)

        elif "how are you" in query:
            speak("I am fine, what about you?")

        elif "fine" in query or "I am good" in query:
            speak("That's great to hear from you")

        elif "volume up" in query:
            pyautogui.press("volume up")

        elif "volume down" in query:
            pyautogui.press("volumedown")

        elif "mute" in query or "mute" in query:
            pyautogui.press("volumemute")

        elif "shut down" in query:
            speak("Shutting down the system")
            os.system("shutdown /s /t 5")

        elif "restart" in query:
            speak("Restarting the system")
            os.system("shutdown /r /t 5")

        elif "sleep mode" in query:
            speak("Sleeping mode")
            os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")

        elif "you can sleep" in query or "sleep now" in query:
            speak("Okay, I am going to sleep. You can call me anytime.")

        elif "wake up" in query:
            speak("Alex at your service. Tell me what I have to do.")

        elif "goodbye" in query or "bye" in query:
            sys.exit()


if _name_ == "_main_":
    wish()
    while True:
        TaskExecution()
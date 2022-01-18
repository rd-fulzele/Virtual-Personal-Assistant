from email.mime import audio
from http import server
from importlib.resources import path
import pyttsx3
import speech_recognition as sr
import datetime
import os 
import webbrowser
import wikipedia
import cv2
import random
from requests import get
import pywhatkit as pw
import smtplib
import sys
import tkinter as tk
from PIL import Image, ImageTk, GifImagePlugin

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio = r.listen(source,timeout=3,phrase_time_limit=5)#no of times command can be given
    
    try:
        speak("Recognizing.....")
        query = r.recognize_google(audio, language = 'en-in') #Using google for voice recognition.
        speak(f"User said: {query}\n") 
    except Exception as e:
        print(e)
        speak("Say that again Please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rdfulzele02@gmail.com','Allnewone69@')
    server.close()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak ("Good Morning!")
    elif hour>=12 and hour<18:
        speak ("Good Afternoon!")    
    elif hour>=18 and hour<20:
        speak ("Good Evening!")
    else:
        speak("How are you doing")
    speak("Hello, How may I help you?")


def main():
    wish()

    query = takecommand().lower() #Converting user query into lower case
    
    if 'wikipedia' in query: #if wikipedia found in the query then this block will be executed
        speak("Searching wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        speak(results)
    elif 'open notepad' in query:
        speak("Opening Notepad")
        npath = "C:\\Windows\\notepad.exe"
        os.startfile(npath) 
    elif 'open command prompt' in query:
        speak("Opening command prompt")
        os.system("start cmd")
    elif 'open camera' in query:
        speak("Opening camera")
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('webcam', img)
            k = cv2.waitKey(50)
            if k==27:
                break;
        cap.release()
        cv2.destroyAllWindows()
    elif 'ip address' in query:
        speak("Getting ip address")
        ip = get('https://api.ipify.org').text
        speak("Your ip address is {ip}")
    elif 'open youtube' in query:
        speak("What do you want to play on youtube")
        yt = takecommand().lower()
        pw.playonyt(f"{yt}")
    elif 'open google' in query:
        speak("What should i search on google")
        cm = takecommand().lower()
        webbrowser.open(f"{cm}")
    elif 'open music' in query:
        speak("opening music")
        webbrowser.open("www.spotify.com")
    elif 'play music' in query:
        speak("Playing music of your choice")
        music_dir = "C:\\Users\\91976\\Music\\Another One"
        songs = os.listdir(music_dir)
        rd = random.choice(songs)
        os.startfile(os.path.join(music_dir, rd))
    elif 'open facebook' in query:
        speak("opening facebook")
        webbrowser.open("www.facebook.com")
    elif 'open stackoverflow' in query:
        speak("opening stackoverflow")
        webbrowser.open("www.stackoverflow.com")
    elif 'send message' in query:
        msg = takecommand().lower()
        pw.sendwhatmsg("+919022694674", f"{msg}", 2,25)#time in the end
    elif 'send email' in query:
        try:
            speak("what should i send")
            content = takecommand().lower()
            to = "prajaktaakhade2001@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent")
        except Exception as e:
            print(e)
            speak("Sorry, i am not able to send email")
    elif 'exit' in query:
        speak("Thank you for using my services, have a good day ahead")
        root.destroy()
        sys.exit()



root = tk.Tk()
frame = tk.Canvas(root, width=600, height=300)
frame.grid(columnspan=3,rowspan=3)

#logo
logo = Image.open('assistant.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)

def run():
    buttontxt.set("Listening...")
    main()
    
#button
buttontxt = tk.StringVar()
button = tk.Button(root, textvariable=buttontxt, command=lambda:run() ,font="Raleway",bg="#20bebe",fg="white", height=2, width=15)
buttontxt.set("Start")
button.grid(column=1,row=2)

frame = tk.Canvas(root, width=600, height=250)
frame.grid(columnspan=3)
root.mainloop()
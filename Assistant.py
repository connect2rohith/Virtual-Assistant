import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests




print('Loading your personal assistant')


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[1].id')




def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)


        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")


        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement


speak("Loading your personal assistant ")
wishMe()




if __name__=='__main__':




    while True:
        speak(" how can I help you?")
        statement = takeCommand().lower()
        if statement==0:
            continue


        if "bye" in statement or "close" in statement or "stop" in statement or "quit" in statement:
            speak('your personal assistant  is shutting down,Good bye')
            print('your personal assistant  is shutting down,Good bye')
            break






        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement =statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)


        elif 'google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google  is open now")
            time.sleep(5)


        elif 'gmail' in statement or 'mail' in statement :
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)


        elif "weather" in statement:
            api_key="8ef61edcf1c576d65d836254e11ea420"
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
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
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))


            else:
                speak(" City Not Found ")






        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")


        elif 'who are you' in statement or 'what can you do' in statement:
            speak('I am your persoanl assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome,gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather' 
                  'in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')




        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by Hesham")
            print("I was built by Hesham")


        elif "stackoverflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/login")
            speak("Here is stackoverflow")


        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")
            speak('Here are some headlines from the Google news,Happy reading')
            time.sleep(10)


        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")


        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        elif 'cricket' in statement:
            news = webbrowser.open_new_tab("https://www.cricbuzz.com")
            speak('Here are cricket scores ')
            time.sleep(6)
        elif 'sport' in statement:
            news =webbrowser.open_new_tab("https://timesofindia.indiatimes.com/sports")
            speak("here is latest news on sports")
        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        elif 'music' in statement:
            music=webbrowser.open('https://music.youtube.com')
            speak('opening music')
        elif 'location' in statement:
            music=webbrowser.open('https://mylocation.org/')
            speak('here is your location')


        elif 'map' in statement or 'maps' in statement:
            map=webbrowser.open('https://www.google.co.in/maps?hl=en&tab=ml')
            speak('opening maps')


        elif 'spec login' in statement or 'student login' in statement:
            spec=webbrowser.open('https://specexams.com/BeesErp/Login.aspx')
            speak('opening college website')


        elif 'amazon' in statement:
            spec=webbrowser.open('https://www.amazon.in')
            speak('opening amazon')


        elif 'flipkart' in  statement:
            spec=webbrowser.open('https://www.flipkart.com')
            speak('opening flipkart')


        elif 'open'  in statement:
            statement = statement.replace("open", "")
            webbrowser.open_new_tab(statement)


            time.sleep(5) 
        
        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])


time.sleep(3)

from urllib.parse import quote
import newsapi          #for getting news
import pyttsx3          #package to convert text to speech
import datetime         #for retrieving current system date and time
import speech_recognition as sr   #converts speech to text
import smtplib          #for sending emails
from secrets import email_list,senderemail,epwd,user_name
from email.message import EmailMessage, Message
import pyautogui            #to send whatsapp message
import webbrowser as wb     #for opening pages in webbrowser
from time import sleep      #for putting the program in sleep
import wikipedia            #for searching on wikipedia
import pywhatkit            #for opening youtube videos
import requests
import pyjokes
from newsapi import NewsApiClient     #for getting news
import clipboard            #for reading the selected text
import os                   #for opening applications
import time as tt
import string
import random
import psutil               #for cpu and battery usage

engine = pyttsx3.init()     #initializing pyttsx3 module for use
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

# This function converts the text to speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# This function selects one of the 2 voices available
def getvoices(voice):
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice',voices[1].id)
        speak("Hello This Is Jarvis")
        speak("From now onwards i will handle all your requests")

    if voice == 2:
        engine.setProperty('voice',voices[7].id)
        speak("Hello This Is Friday")
        speak("From now onwards i will handle all your requests")


#This function gets the current system time in the HH:MM:SS format and speaks out the time
def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak("The current time is :")
    speak(Time)

#This function gets the current system date and speaks out the date
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is :")
    speak(date)
    speak(month)
    speak(year)

#This function greets the user according to the current time
def greeting():
    hour = datetime.datetime.now().hour
    if hour>= 6 and hour < 12:
        speak("Good Morning")
    elif hour >=12 and hour < 18:
        speak("Good Afternoon")
    elif hour >=18 and hour < 24:
        speak("Good Evening !")
    else:
        speak("Good Night")

#This function wishes the user  
def wishme():
    speak("Welcome back Sir !")
    #time()
    #date()
    greeting()
    speak("Jarvis at your service , please tell me how can i help you?")

#This function take command from user using the microphone as source
def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio,language='en-IN')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please ....")
        speak("Say that again please ....")
        return "None"
    return query

#Function for sending email
def sendEmail(receiver,subject,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(senderemail,epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()

#Function for sending whatsapp message
def sendwhatsmsg(phone_no,message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(10)
    pyautogui.press('enter')

#function for searching on google
def searchgoogle():
    speak("what should i search for?")
    search = takeCommand()
    wb.open('https://www.google.co.in/search?q='+search)
    speak("Showing google search results for")
    speak(search)

#for getting news
def news():
    newsapi = NewsApiClient(api_key='71e53b65ce714ef28c14567a0d9518a5')
    print("From what topic you want news about?")
    speak("From what topic you want news about?")
    topic = takeCommand()
    data = newsapi.get_top_headlines(q=topic,
                                    language='en',
                                    page_size= 5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))
    
    speak("That's it for now....I will update you in sometime")


#Function for reading out selected text
def text2speech():
    text = clipboard.paste()
    print(text)
    speak(text)

#Fucntion for getting covid updates
def covid():
    r = requests.get('https://coronavirus-19-api.herokuapp.com/all')

    data = r.json()
    covid_data = f'Confirmed Cases : {data["cases"]} \n Deaths :{data["deaths"]} \n Recovered :{data["recovered"]}'
    print("Covid records for cases in world")
    speak("Covid records for cases in world")
    print(covid_data)
    speak(covid_data)

#Function for taking screenshot
def screenshot():
    name_img = tt.time()
    name_img = f'E:\\JARVIS 2.0\screenshot\\{name_img}.png'
    img = pyautogui.screenshot(name_img)
    img.show()

#function for password generation
def passwordgen():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passlen=8
    s=[]
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    newpass = ("".join(s[0:passlen]))
    print("The generated password Is:",newpass)
    speak("The generated password Is:")
    speak(newpass)
    
#function for flipping a coin
def flip():
    speak("Okay sir,Flipping a coin for you")
    coin = ['heads','tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = ("".join(toss[0]))
    print("I flipped the coin and you got",toss)
    speak("I flipped the coin and you got"+toss)

#function for rolling a die
def rolldie():
    speak("Okay sir,Rolling a die for you")
    die = ['1','2','3','4','5','6']
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = ("".join(roll[0]))
    print("I rolled a die and you got",roll)
    speak("I rolled a die and you got"+roll)

#funtion for cpu and battery usage
def cpu():
    usage = str(psutil.cpu_percent())
    print("CPU usage is at",usage,"percent")
    speak("CPU usage is at"+usage+'percent')
    battery = psutil.sensors_battery()
    print("Battery is at")
    speak("Battery is at")
    print(battery.percent)
    speak(battery.percent)

#main function
if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        #tells time
        if 'time' in query:
            time()

        #tells date
        elif 'date' in query:
            date()

        #switching to male voice
        elif 'switch to jarvis' in query:
            getvoices(1)

        #switching to female voice
        elif 'switch to friday' in query:
            getvoices(2)

        #for opening youtube
        elif 'open youtube' in query:
            wb.open("youtube.com")

        #for opening google
        elif 'open google' in query:
            wb.open("google.com")

        #for opening stackoverflow
        elif 'open stack overflow' in query:
            wb.open("stackoverflow.com")

        #for sending email
        elif 'email' in query:          
            try:
                speak("To whom do you want to send the email?")
                name = takeCommand()
                receiver = email_list[name]
                speak("What is the subject of the email?")
                subject = takeCommand()
                speak("What should i send ? ")
                content = takeCommand()
                sendEmail(receiver,subject,content)
                speak("Email has been successfully sent !!")
            except Exception as e:
                print(e)
                speak("Unable to send the email !!")

        #for sending whatsapp message
        elif 'whatsapp message' in query:
            try:
                speak("To whom do you want to send the whatsapp message?")
                name = takeCommand()
                phone_no = user_name[name]
                speak("What is the Message?")
                message = takeCommand()
                sendwhatsmsg(phone_no,message)
                speak("Whatsapp Message Sent Successfully!!")
            
            except Exception as e:
                print(e)
                speak("Unable to send the whatsapp message !!")

        #for searching in wikipedia
        elif 'search in wikipedia' in query:
            print("Searching on wikipedia....")
            speak("Searching on wikipedia....")
            query = query.replace("search in wikipedia","")
            result = wikipedia.summary(query,sentences = 2)
            print(result)
            speak(result)
        
        #for searching on google
        elif 'search on google' in query:
            searchgoogle()

        #for playing youtube videos
        elif 'play on youtube' in query:
            speak("What should i search for you in youtube")
            topic = takeCommand()
            pywhatkit.playonyt(topic)
            speak("Playing on Youtube")

        #for getting weather details
        elif 'weather' in query:
            speak("Which place's weather do you want to know")
            city = takeCommand()
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid=a3bffb0b50358ae12325da9c057f8e4c'
            
            res = requests.get(url)
            data = res.json()

            weather = data['weather'] [0]['main']
            temp = data['main']['temp']
            desp = data['weather'][0]['description']
            temp = round((temp-32)*5/9)
            print(weather)
            print(temp)
            print(desp)
            speak(f"Weather in {city} city is like")
            speak("Temperature : {} degree celsius".format(temp))
            speak("Weather is {} ".format(desp))

        #for playing music stored in a directory on system
        elif 'play music' in query or "play song" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "E:\\Songs"
            songs = os.listdir(music_dir)   
            random = os.startfile(os.path.join(music_dir, songs[2]))

        #for getting news
        elif 'news' in query:
            news()

        #for reading the text present on clipboard
        elif 'read selected text' in query:
            text2speech()

        #for getting covid statistics 
        elif 'covid' in query:
            covid()     

        #for opening my documents
        elif 'open my documents' in query:
            os.system('explorer C://{}'.format(query.replace('open','')))

        #for opening application vs code
        elif 'open vs code' in query:
            codepath = 'C:\\Users\\Manish\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(codepath)
            speak("Opening VS Code")

        #for opening codeblocks
        elif 'open code blocks' in query:
            codepath ='C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe'
            os.startfile(codepath)
            speak("Opening Codeblocks")
        
        #for opening mp lab
        elif 'open mp lab' in query:
            codepath ='C:\\Program Files\\Microchip\\MPLABX\\v5.45\\mplab_platform\\bin\\mplab_ide64.exe'
            os.startfile(codepath)
            speak("Opening MP Lab")

        #for getting jokes
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        #for taking screenshot
        elif 'screenshot' in query:
            screenshot()

        #for remembering details
        elif 'remember this' in query:
            speak("What should i remember")
            data = takeCommand()
            speak("You said me to remember that"+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        #for getting the things remembered
        elif 'do you remember anything' in query:
            remember = open('data.txt','r')
            speak("You told me to remember this"+remember.read())

        #for generating a random password
        elif 'generate password' in query:
            passwordgen()

        #flipping a coin
        elif 'flip a coin' in query:
            flip()

        #rolling a die
        elif 'roll a die' in query:
            rolldie()

        #for getting cpu and battery usage details
        elif 'cpu and battery usage' in query:
            cpu()

        #for searching a location on google maps
        elif "search on maps" in query:
            speak("Which place do you want me to search on google maps?")
            location = takeCommand()
            location_url = "https://www.google.com/maps/place/" + location          
            #maps_arg = '/usr/bin/open -a "/Applications/Google Chrome.app" ' + location_url
            wb.open(location_url)

        #for exiting out of program
        elif 'offline' in query:
            quit()



""" 1st project - My Shree

   author = Dheeraj jaiswal
"""
import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechrecognition
import wikipedia # pip install wikipedia
import webbrowser # in-built module
import datetime # in-built module
import os      # in-built module
import smtplib  # in-built module

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)  1 = shree and 0 = jarvis
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good morning Dheeraj jaiswal!')
    elif hour >= 12 and hour < 18:
        speak("Good afternoon Dheeraj jaiswal!")
    elif hour >= 18 and hour < 22:
        speak("Good evening Dj!")
    else:
        speak("Good night DJ!")
    speak("I am Shree . please tell me how may i help you")

# for commanding install pipwin and use of pipwin then install pyaudio
def takeCommand(): # it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:       # for safety reason khi upper ka code error na throw kr de
        print("Recognizing..")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        print("say that again please..")
        return "None"
    return query
def sendEmail(to,content): # to send mail
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("dheerajjaiswal3333@gmail.com","Dheeraj@123")
    server.sendmail("dheerajjaiswal3333@gmail.com",to,content)
    server.close()

if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia..')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2) # wikipedia se query se related 2 sentences utha lega
            speak("According to wikipedia..")
            print(results) # print ans of your query
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = "C:\\Users\\Dheer\\Music\\dj songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0])) # converted music directory in to songs and also play
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is: {strTime}")
        elif "open code" in query:
            codePath = "C:\\Users\\Dheer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" # path for open code the main thing that please enter ctrl+s
            os.startfile(codePath)
        elif "play videos" in query:
            video_dir = "C:\\Users\\Dheer\\Videos\\Captures"
            videos = os.listdir(video_dir)
            print(videos)
            os.startfile(os.path.join(video_dir,videos[1])) #for run video at 1st position
        elif "send email to sonu" in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "sonupriya912@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry my friend Dj. i am not able to send this email")
        else:
            speak("please said something to related in my dictionary, Thankyou!")



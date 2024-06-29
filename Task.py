import datetime
from Speak import Say


def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    Say(time)

def Date():
    date = datetime.date.today()
    Say(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    Say(day)


def NonInputExecution(query):
    query = str(query)
    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "day" in query:
        Day()
    

def InputExecution(tag,query):

    if "wikipedia" in tag:
        name = str(query).replace("who is"," ").replace("about","").replace("what is","").replace("wikipedia","")
        print(name)
        import wikipedia
        result = wikipedia.summary(name, sentences=1)
        Say(result)
    
    elif "google" in tag:
        s=str(query).replace("google search","").replace("google","").replace("search","")
        import webbrowser as wb
        s=s.replace(" ","+")
        url="https://www.google.com/search?q="
        a=url+s
        #chrome_path="C:\Program Files\Google\Chrome\Application/chrome.exe %s"
        #wb.get(chrome_path).open(a)
        wb.open(a)

    elif "youtube" in tag:
        yt=str(query).replace("play","").replace("play on youtube", "")
        print(yt)
        import pywhatkit
        pywhatkit.playonyt(yt)

    elif "open" in tag:
        import webbrowser as wb
        abc="https://www.youtube.com/"
        wb.open(abc)

    elif "news" in tag:
        news=str(query)
        import requests
        import json
        import numpy
        import pandas
        a=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=f6db5e88148d468aa2237314761068c5")
        b=json.loads(a.text)
        for i in range(10):
            my_data=b['articles'][i]['title']
            print ("Title:",i+1,my_data)
            Say(my_data)




from datetime import datetime
import time
import json
import requests
from win32com.client import Dispatch


def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
# time


def get_part_of_day(h):
    return (
        "morning"
        if 5 <= h <= 11
        else "afternoon"
        if 12 <= h <= 17
        else "evening"
        if 18 <= h <= 22
        else "night"
    )


# To use current hour:
part = get_part_of_day(datetime.now().hour)
print(f"Good {part}!")
speak(f"Good {part}!")


print("Welcome to the rohan News channel!")
speak("Welcome to the rohan News channel!")
a = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=API_KEY')
data = json.loads(a.content)
print('Here are the top ten news of the awesome country India\n')
speak('Here are the top ten news of the awesome country India')
for i in range(1, 11):
    print(f'{i} .', data['articles'][i]['description'], '\n')
    news = data['articles'][i]['description']
    speak(news)
    time.sleep(1)
    if i == 9:
        speak('So our last news for today is')
    elif i == 10:
        break
    else:
        speak("Moving To Our next news")
print("Thanks for listening ! Have a nice day")
speak("Thanks for listening ! Have a nice day")
time.sleep(2)
speak('Click Any Key For Exit')
input('Click Any Key For Exit: ')

# -*- coding: cp1251 -*-
from Config import *

def execute_error():
    play_voice_assistant_speech("Я не смогла. Ещё что сделать?")
def playmusic(name):
    subprocess.Popen(['start', 'D:/UWU/Songs/4.mp3'], shell = True)
def playsong(name):
    song = randint(1,14)
    songPath = "D:/UWU/Songs/"+str(song)+".mp3"
    try:
        subprocess.Popen(['start', songPath], shell = True)
        
    except:
        print("ERROR")
        play_voice_assistant_speech("Произошла Ошибка")
    
def browser(sw):
    subprocess.Popen(r"C:\Program Files (x86)\Yandex\YandexBrowser\Application\browser.exe", shell = True)

def steam(sw):
    #"D:\Steam\steam.exe"
    subprocess.Popen(r"D:\Steam\steam.exe", shell = True)
def discord(sw):
    subprocess.Popen(r"C:\Users\Алексей Злагода\AppData\Local\Discord\Update.exe", shell = True)
def turn(coms):
    turn_mas = {
        ("музыку"):playmusic,
        ("песню"):playsong,
        ("браузер"):browser,
        ("стим","steam"):steam,
        ("дискорд", "discord"):discord
    }
    for key in turn_mas.keys():
        if coms[0] in key:
            turn_mas[key](coms[1:len(coms)])
            return

    
    
    
def search_for_video_on_youtube(args):
     search_term = "".join(args[0])
     url = "https://www.youtube.com/results?search_query=" + search_term
     subprocess.Popen("explorer.exe "+ url, shell = True)
     global Active 
     Active = False


def play_farewell_and_quit(H):
    global Active 
    Active = False
    play_voice_assistant_speech(" Пока")
    subprocess.Popen(['start', 'D:/UWU/Songs/4.mp3'], shell = True)
    global On 
    On = False
#def get_weather_forecast():
 #   return
def search_for_term_on_google(args):
    search_term = ""
    search_term = "".join(args[0])
    url = "https://yandex.ru/search/?text=" + search_term
    subprocess.Popen("explorer.exe " + url, shell = True)
    global Active 
    Active = False
def execute_command_with_name(line, command_name: str, *args: list):
    commands = {
        #("гимн"):gimn,
        #("музыка"):music,
        #("Приветствую","Рад Видеть","Доброго времени суток", "привет"): play_greetings,
        ("bye", "goodbye", "quit", "exit", "stop", "пока","спокойной"): play_farewell_and_quit,
        ("search", "google", "find", "найди"): search_for_term_on_google,
        ("включи","включил","включай", "открой","открыл","открывай"):turn,
        ("video", "youtube", "watch", "видео","ютуб"): search_for_video_on_youtube,
        #("wikipedia", "definition", "about", "определение", "википедия"): search_for_definition_on_wikipedia,
        #("translate", "interpretation", "translation", "перевод", "перевести", "переведи"): get_translation,
        #("language", "язык"): change_language,
        #("weather", "forecast", "погода", "прогноз"): get_weather_forecast,
    }
    for key in commands.keys():
        if command_name in key:
            commands[key](*args)
            return 0
    return -1
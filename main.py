# -*- coding: cp1251 -*-
from random import randint
from tkinter import TRUE
import keyboard
import speech_recognition  # ������������� ���������������� ���� (Speech-To-Text)
import pyttsx3  # ������ ���� (Text-To-Speech)
import wave  # �������� � ������ ����������� ������� wav
import json  # ������ � json-������� � json-��������
import os  # ������ � �������� ��������
import random
import time, subprocess
import openai
from silero import  silero_tts
import torch
import sounddevice as sd
import time

GPT_HISTORY ="���� ����� �����. ���� ����������� ���. ������� �������"
On = True
openai.api_key = "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"
Active =True
def ACT():
    global Active
    Active = True
keyboard.add_hotkey("c", lambda: ACT() )

class VoiceAssistant:
    """
    ��������� ���������� ����������, ���������� ���, ���, ���� ����
    """
    name = "Judi"
    sex = "female"
    speech_language = "ru"
    recognition_language = "ru-RU"


def setup_assistant_voice():
    """
    ��������� ������ �� ��������� (������ ����� �������� � 
    ����������� �� �������� ������������ �������)
    """
    voices = ttsEngine.getProperty("voices")

    if assistant.speech_language == "en":
        assistant.recognition_language = "en-US"
        if assistant.sex == "female":
            # Microsoft Zira Desktop - English (United States)
            ttsEngine.setProperty("voice", voices[1].id)
        else:
            # Microsoft David Desktop - English (United States)
            ttsEngine.setProperty("voice", voices[2].id)
    else:
        assistant.recognition_language = "ru-RU"
        # Microsoft Irina Desktop - Russian
        ttsEngine.setProperty("voice", voices[0].id)


def play_voice_assistant_speech(text_to_speech):
    """
    ������������ ���� ������� ���������� ���������� (��� ���������� �����)
    :param text_to_speech: �����, ������� ����� ������������� � ����
    """

    #ttsEngine.say(str(text_to_speech))
    #ttsEngine.runAndWait()
    language = 'ru'
    model_id = 'ru_v3'
    sample_rate = 48000
    speaker = 'baya' # baya aidar kseniya xenia
    put_accent = True
    put_yo = True
    device = torch.device('cpu')
    text =str(text_to_speech)

    model, _ = silero_tts(language=language,
    speaker=model_id)
    model.to(device)
    try:
        audio = model.apply_tts(text=text,
        speaker=speaker,
        sample_rate=sample_rate,
        put_accent=put_accent,
        put_yo=put_yo)
        sd.play(audio, sample_rate)
        time.sleep(len(audio)/sample_rate+1)
        sd.stop()
    except:
        play_voice_assistant_speech("������, � ����������. ������� ����������!")



def WaitCommands():
    global Active
    Active = False
    while Active == False:
        with microphone:
            recognized_data = ""

      
            recognizer.adjust_for_ambient_noise(microphone, duration=2)

            try:
                audio = recognizer.listen(microphone, 0, 0)
            except:
                pass
            try:
                recognized_data = recognizer.recognize_google(audio, language="ru").lower()
            except:
                pass
        if recognized_data == "������":
            Active = True

def record_and_recognize_audio(*args: tuple):
   
    with microphone:
        recognized_data = ""

      
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5, 5)

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass
        except speech_recognition.RequestError:
            print("Check your Internet Connection, please")

        return recognized_data
def playmusic(name):
    subprocess.Popen(['start', 'D:/UWU/Songs/4.mp3'], shell = True)
def playsong(name):
    song = randint(1,14)
    songPath = "D:/UWU/Songs/"+str(song)+".mp3"
    try:
        subprocess.Popen(['start', songPath], shell = True)
        
    except:
        print("ERROR")
        play_voice_assistant_speech("������ "+"��������� ������")
    
def browser(sw):
    subprocess.Popen(r"C:\Program Files (x86)\Yandex\YandexBrowser\Application\browser.exe", shell = True)

def steam(sw):
    #"D:\Steam\steam.exe"
    subprocess.Popen(r"D:\Steam\steam.exe", shell = True)
def discord(sw):
    subprocess.Popen(r"C:\Users\������� �������\AppData\Local\Discord\Update.exe", shell = True)
def turn(coms):
    turn_mas = {
    ("������"):playmusic,
    ("�����"):playsong,
    ("�������"):browser,
    ("����","steam"):steam,
    ("�������", "discord"):discord
}
    for key in turn_mas.keys():
        if coms[0] in key:
            turn_mas[key](coms[1:len(coms)])
            return
    
    
def search_for_video_on_youtube(args):
     search_term = "".join(args[0])
     url = "https://www.youtube.com/results?search_query=" + search_term
     subprocess.Popen(["explorer.exe", url], shell = True)
     global Active 
     Active = False


def play_farewell_and_quit(H):
    global Active 
    Active = False
    play_voice_assistant_speech(" ����")
    subprocess.Popen(['start', 'D:/UWU/Songs/4.mp3'], shell = True)
    global On 
    On = False
#def get_weather_forecast():
 #   return
def search_for_term_on_google(args):
    search_term = ""
    search_term = "".join(args[0])
    url = "https://yandex.ru/search/?text=" + search_term
    subprocess.Popen(["explorer.exe", url], shell = True)
    global Active 
    Active = False
def execute_command_with_name(line, command_name: str, *args: list):
    for key in commands.keys():
        if command_name in key:
            commands[key](*args)
            global Active 
            Active = False
            return;
    
    ANSW = openai.Completion.create(engine="text-davinci-003", prompt=GPT_HISTORY+line, temperature=1, max_tokens=250).choices[0]['text']
    play_voice_assistant_speech(str(ANSW))
   
    


            


if __name__ == "__main__":
    commands = {
    #("����"):gimn,
    #("������"):music,
    #("�����������","��� ������","������� ������� �����", "������"): play_greetings,
   ("bye", "goodbye", "quit", "exit", "stop", "����","���������"): play_farewell_and_quit,
    ("search", "google", "find", "�����"): search_for_term_on_google,
    ("������","�������","�������", "������","������","��������"):turn,
    ("video", "youtube", "watch", "�����","����"): search_for_video_on_youtube,
    #("wikipedia", "definition", "about", "�����������", "���������"): search_for_definition_on_wikipedia,
    #("translate", "interpretation", "translation", "�������", "���������", "��������"): get_translation,
    #("language", "����"): change_language,
    #("weather", "forecast", "������", "�������"): get_weather_forecast,
}

    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()
    ttsEngine = pyttsx3.init()

    # ��������� ������ ���������� ���������
    assistant = VoiceAssistant()

    setup_assistant_voice()

    while On:
        #WaitCommands()
        #play_voice_assistant_speech("������ "+"������")
        while Active:
            #play_voice_assistant_speech("I dont understand you")
            voice_input = record_and_recognize_audio()
            print(voice_input)
            #play_voice_assistant_speech("������ "+str(voice_input))
            voice_input2 = voice_input.split(" ")
            command = voice_input2[0]
            if not(voice_input == "" or voice_input == " "):
                command_options = [str(input_part) for input_part in voice_input2[1:len(voice_input)]]
                execute_command_with_name(voice_input,command, command_options)
        

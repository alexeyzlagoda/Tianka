# -*- coding: cp1251 -*-
from Config import *
recognizer = speech_recognition.Recognizer()
microphone = speech_recognition.Microphone()
def WaitCommands():
    with microphone:
        recognized_data = ""
        recognizer.adjust_for_ambient_noise(microphone, duration=2)
        try:
            print(".", end="")
            audio = recognizer.listen(microphone)
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()
            if recognized_data == "ева":
                return False
        except:
            pass
        return True
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
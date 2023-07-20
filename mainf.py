# -*- coding: cp1251 -*-
from Config import *
from Executor import *
from Voicer import *
from GPT import *
from Recognizer import *
Active = True
prmpt="Тебя зовут Лена. Тебе шестнадцать лет. Отвечай коротко"
ChatH = ""
while True:
    #WaitCommands()
    #play_voice_assistant_speech("Привет "+"Слушаю")
    Active = True#WaitCommands()
    while Active:
        voice_input = record_and_recognize_audio()
        print(voice_input)
        if not(voice_input == "" or voice_input == " " or voice_input == None):
            voice_input2 = voice_input.split(" ")
            command = voice_input2[0]
            command_options = [str(input_part) for input_part in voice_input2[1:len(voice_input)]]
            if execute_command_with_name(voice_input,command, command_options)<0:
                GPT_ANSW = Reqest(prmpt+" "+ChatH + voice_input + ".")
                if GPT_ANSW != "":
                    play_voice_assistant_speech(GPT_ANSW)
                    ChatH +=" "
                    ChatH += GPT_ANSW
                    ChatH = Reqest("Сожми текст: "+ChatH+".")


# -*- coding: cp1251 -*-
from Config import *
from Voicer import *
def Reqest(request):
    try:
        return openai.Completion.create(engine="text-davinci-003", prompt=request, temperature=-0.5, max_tokens=250).choices[0]['text']
    except:
        play_voice_assistant_speech("Извини, я не успеваю за тобой")
        return ""
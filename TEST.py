# -*- coding: cp1251 -*-
from silero import  silero_tts
import torch
import sounddevice as sd
import time
language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'baya' # baya aidar kseniya xenia
put_accent = True
put_yo = True
device = torch.device('cpu')
text ="Привет, Миша"

model, _ = silero_tts(language=language,
speaker=model_id)
model.to(device)

audio = model.apply_tts(text=text,
speaker=speaker,
sample_rate=sample_rate,
put_accent=put_accent,
put_yo=put_yo)
sd.play(audio, sample_rate)
time.sleep(len(audio)/sample_rate)
sd.stop()
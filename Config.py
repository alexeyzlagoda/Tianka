# -*- coding: cp1251 -*-
from random import randint
from tkinter import TRUE
import keyboard
import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)
import pyttsx3  # синтез речи (Text-To-Speech)
import wave  # создание и чтение аудиофайлов формата wav
import json  # работа с json-файлами и json-строками
import os  # работа с файловой системой
import random
import time, subprocess
import openai
from silero import  silero_tts
import torch
import sounddevice as sd
import time
#GPT
openai.api_key = "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"
std_prompt = "Тебя зовут Лена. Тебе шестнадцать лет. Отвечай коротко"
#SNAKES4/silero
language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'baya' # baya aidar kseniya xenia
put_accent = True
put_yo = True
device = torch.device('cpu')

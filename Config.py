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
#GPT
openai.api_key = "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"
std_prompt = "���� ����� ����. ���� ����������� ���. ������� �������"
#SNAKES4/silero
language = 'ru'
model_id = 'ru_v3'
sample_rate = 48000
speaker = 'baya' # baya aidar kseniya xenia
put_accent = True
put_yo = True
device = torch.device('cpu')

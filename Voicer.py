# -*- coding: cp1251 -*-
from Config import *
def play_voice_assistant_speech(text_to_speech):
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
        play_voice_assistant_speech("Извини, я задумалась. Повтори пожалуйста!")
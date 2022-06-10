import gtts
import os
import miniaudio

file_save = "/tmp/tmp_save.mp3"

need_end = False

def stream_end_callback() -> None:
    global need_end
    need_end = True

def play_file(filename: str):
    global need_end
    need_end = False
    stream = miniaudio.stream_file(filename)
    stream_callback = miniaudio.stream_with_callbacks(stream, end_callback=stream_end_callback)
    next(stream_callback)
    with miniaudio.PlaybackDevice() as device:
        device.start(stream_callback)
        while need_end == False:
            continue

def say(text: str, lang: str):
    tts = gtts.gTTS(text=text, lang=lang)
    tts.save(file_save)
    play_file(file_save)
    os.remove(file_save)

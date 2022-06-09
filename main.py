#!/bin/env python3
import sys
import sounddevice
import vosk
import queue
import json

from src.plugins.open_app import plug_open
from src.plugins.play_music import plug_music
from src.plugins.change_window import plug_change_window

funcs_exe_plug = [
    plug_open,
    plug_music,
    plug_change_window
]

q = queue.Queue()

device_index = sounddevice.default.device
device = sounddevice.query_devices(device=device_index[0], kind='input')
samplerate = int(device['default_samplerate'])
blocksize = 8000

if len(sys.argv) == 1:
    lang = input("fr or en lang ? [en/fr] > ")
    if lang not in ("fr", "en"):
        print("choose fr or en")
        exit(1)
elif sys.argv[1] not in ("fr", "en"):
    print("choose fr or en")
    exit(1)
else:
    lang = sys.argv[1]
dict_choice = {
    "fr": "fr",
    "en": "en-us"
}
model = vosk.Model(lang=dict_choice[lang])

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

with sounddevice.RawInputStream(
        samplerate=samplerate,
        blocksize=blocksize,
        device=device_index[0],
        dtype='int16',
        channels=1,
        callback=callback):
    print("start recording and understanding")
    rec = vosk.KaldiRecognizer(model, samplerate)
    while True:
        data = q.get()
        if rec.AcceptWaveform(data=data):
            res = json.loads(rec.Result())
            print(res)
            print(type(res))
            for func in funcs_exe_plug:
                func(res["text"])

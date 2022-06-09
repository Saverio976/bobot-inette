import sys
import sounddevice
import vosk
import queue
import json

from src.plugins.open_app import plug_open
from src.plugins.play_music import plug_music

funcs_exe_plug = [
    plug_open,
    plug_music
]

plug_music('joue')

q = queue.Queue()

device_index = sounddevice.default.device
device = sounddevice.query_devices(device=device_index[0], kind='input')
samplerate = int(device['default_samplerate'])
blocksize = 8000

model = vosk.Model(lang='fr')
# model = vosk.Model(lang='en-us')

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

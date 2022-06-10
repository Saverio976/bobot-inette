import sys
import queue
import json
import sounddevice
import vosk
from .text_to_speech import say

q = queue.Queue()

def callback(indata, _, times, status):
    global q
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

def undertand_res(data, rec: vosk.KaldiRecognizer, funcs_exe_plug: list):
    if not rec.AcceptWaveform(data=data):
        res = rec.PartialResult()
        res = json.loads(res)
        if res["partial"].strip() != "":
            print(f"partial result : '{res['partial']}'")
    else:
        res = json.loads(rec.Result())
        for func in funcs_exe_plug:
            func(res["text"])

def main(lang: str, funcs_exe_plug: list) -> int:
    global q
    device_index = sounddevice.default.device
    device = sounddevice.query_devices(device=device_index[0], kind='input')
    samplerate = int(device['default_samplerate'])
    blocksize = 8000
    model = vosk.Model(lang=lang)

    with sounddevice.RawInputStream(
            samplerate=samplerate,
            blocksize=blocksize,
            device=device_index[0],
            dtype='int16',
            channels=1,
            callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        say("start recording", "en")
        while True:
            data = q.get()
            undertand_res(data, rec, funcs_exe_plug)
    return 0

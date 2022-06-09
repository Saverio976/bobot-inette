import sys
import queue
import json
import sounddevice
import vosk

q = queue.Queue()

def callback(indata, frames, time, status):
    global q
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

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
        print("start recording and understanding")
        while True:
            data = q.get()
            if not rec.AcceptWaveform(data=data):
                continue
            res = json.loads(rec.Result())
            for func in funcs_exe_plug:
                func(res["text"])
    return 0

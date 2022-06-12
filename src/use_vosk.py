import sys
import queue
import json
import sounddevice
import vosk

class EngineVosk:
    def __init__(self, lang: str = "en", funcs_exe_plug: list = []):
        self._lang = lang
        self._funcs_exe_plug = funcs_exe_plug
        self._q = queue.Queue()
        self._device_index = sounddevice.default.device
        self._device = sounddevice.query_devices(device=self._device_index[0], kind='input')
        self._samplerate = int(self._device['default_samplerate'])
        self._blocksize = 8000
        self._model = vosk.Model(lang=lang)

        self._rec = vosk.KaldiRecognizer(self._model, self._samplerate)

    def _callback(self, indata, _, times, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        self._q.put(bytes(indata))

    def _undertand_res(self, data):
        if not self._rec.AcceptWaveform(data=data):
            res = self._rec.PartialResult()
            res = json.loads(res)
            if res["partial"].strip() != "":
                print(f"partial result : '{res['partial']}'")
            return ""
        else:
            res = json.loads(self._rec.Result())
            print(f"text: {res['text']}")
            return res["text"]

    def get_sentence(self) -> str:
        with sounddevice.RawInputStream(
                samplerate=self._samplerate,
                blocksize=self._blocksize,
                device=self._device_index[0],
                dtype='int16',
                channels=1,
                callback=self._callback) as _:
            data = self._q.get()
            res = self._undertand_res(data)
            if res != "":
                return res
        return ""

    def end(self):
        return None

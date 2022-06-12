import speech_recognition

dict_conv = {
    "en-us": "en-US",
    "fr": "fr-FR"
}

class EngineSpeechRecognition:
    def __init__(self, lang: str = "en", funcs_exe_plug: list = []):
        self._r = speech_recognition.Recognizer()
        self._lang = lang
        self._funcs_exe_plug = funcs_exe_plug
        if lang in dict_conv.keys():
            self._lang_gg = dict_conv[lang]
        else:
            self._lang_gg = lang

    def get_sentence(self) -> str:
        with speech_recognition.Microphone() as source:
            audio = self._r.listen(source=source, timeout=2, phrase_time_limit=2)
        try:
            print("processing input")
            text = self._r.recognize_google(audio, language=self._lang_gg)
        except Exception as _:
            print("input not recognized")
            return ""
        print(f"text: {text}")
        return text

    def end(self):
        return None

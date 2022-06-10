import speech_recognition
from .text_to_speech import say

dict_conv = {
    "en-us": "en-US",
    "fr": "fr-FR"
}

def main(lang: str, funcs_exe_plug: list) -> int:
    r = speech_recognition.Recognizer()
    print(r.energy_threshold)
    if lang in dict_conv.keys():
        lang_gg = dict_conv[lang]
    else:
        lang_gg = lang
    say("start recording", "en")
    while True:
        with speech_recognition.Microphone() as source:
            audio = r.listen(source=source, timeout=2, phrase_time_limit=2)
        try:
            print("processing input")
            text = r.recognize_google(audio, language=lang_gg)
        except Exception as _:
            print("input not recognized")
            continue
        print(text)
        for func in funcs_exe_plug:
            func(text)
    return 0

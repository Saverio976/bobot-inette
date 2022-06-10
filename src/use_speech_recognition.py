import sys
import speech_recognition

dict_conv = {
    "en-us": "en-US",
    "fr": "fr-FR"
}

def main(lang: str, funcs_exe_plug: list) -> int:
    r = speech_recognition.Recognizer()
    print(r.energy_threshold)
    if lang in dict_conv.keys():
        lang = dict_conv[lang]
    print("start recording and understanding")
    while True:
        with speech_recognition.Microphone() as source:
            audio = r.listen(source=source, timeout=2, phrase_time_limit=2)
        try:
            print("processing input")
            text = r.recognize_google(audio, language=lang)
        except Exception as e:
            print("input not recognized")
            continue
        print(text)
        for func in funcs_exe_plug:
            func(text)
    return 0

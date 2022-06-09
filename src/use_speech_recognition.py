import sys
import speech_recognition

def main(lang: str, funcs_exe_plug: list) -> int:
    r = speech_recognition.Recognizer()
    print("start recording and understanding")
    while True:
        with speech_recognition.Microphone() as source:
            audio = r.listen(source=source)
        try:
            text = r.recognize_google(audio, language=lang)
        except Exception as e:
            print(f"ERROR: {e}", file=sys.stderr)
            exit(1)
        print(text)
        for func in funcs_exe_plug:
            func(text)
    return 0

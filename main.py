#!/bin/env python3

# change cwd to where the file here
import sys
import os

from src.handle_text import handle_text_mic
file_path = os.path.realpath(__file__)
path = os.path.dirname(file_path)
os.chdir(path)

# parse args
import argparse

# engine
from src.use_vosk import EngineVosk
from src.use_speech_recognition import EngineSpeechRecognition
from src.use_text_input import EngineTextInput
dict_choice_engine = {
    "vosk": EngineVosk,
    "speechrecognition": EngineSpeechRecognition,
    "text": EngineTextInput
}

# plugins
from src.plugins.open_app import plug_open
from src.plugins.play_music import plug_music
from src.plugins.change_window import plug_change_window
from src.plugins.quit_window import plug_quit_window
from src.plugins.jarvis import plug_jarvis
funcs_exe_plug = [
    plug_open,
    plug_music,
    plug_change_window,
    plug_quit_window,
    plug_jarvis
]

# lang correspond
dict_choice_lang = {
    "fr": "fr",
    "en": "en-us"
}

def quit_this_if_list():
    """
    check if need to print all engines or all lang availible
    and if yes, print it and exit(0)
    else just return None
    """
    in_list = False
    if "--list-engine" in sys.argv:
        for e in dict_choice_engine.keys():
            print(e)
        in_list = True
    if "--list-lang" in sys.argv:
        for e in dict_choice_lang.keys():
            print(e)
        in_list = True
    if in_list:
        exit(0)

def parse_args() -> argparse.Namespace:
    """
    parse arguments argv and return the values
    """
    parser = argparse.ArgumentParser(
        description='tool to recognize default action by speech'
    )
    parser.add_argument("--list-lang", action="store_const",
        const=True, default=False,
        help="get list of availible lang"
    )
    parser.add_argument("--list-engine", action="store_const",
        const=True, default=False,
        help="get list of availible engine"
    )
    parser.add_argument( "--lang", dest="lang",
        type=str, nargs=1, required=False, default=["en"],
        help="specify the language"
    )
    parser.add_argument("--engine", dest="engine",
        type=str, nargs=1, required=False, default=["vosk"],
        help="specify the speech recognition engine"
    )
    args = parser.parse_args()
    if args.lang[0] not in dict_choice_lang:
        parser.error(f"{args.lang[0]} not availible (see --list-lang)")
    if args.engine[0] not in dict_choice_engine:
        parser.error(f"{args.engine[0]} not availible (see --list-engine)")
    return args

def main() -> int:
    quit_this_if_list()
    args = parse_args()
    lang = dict_choice_lang[args.lang[0]]
    engine_class = dict_choice_engine[args.engine[0]]
    engine = engine_class(lang=lang, funcs_exe_plug=funcs_exe_plug)
    while True:
        sentence = engine.get_sentence()
        handle_text_mic(sentence, funcs_exe_plug, engine)
    engine.end()
    return 0

if __name__ == "__main__":
    ret_code = main()
    exit(ret_code)

#!/bin/env python3
import sys
import os

file_path = os.path.realpath(__file__)
path = os.path.dirname(file_path)
os.chdir(path)

import argparse

from src import use_vosk
from src import use_speech_recognition

from src.plugins.open_app import plug_open
from src.plugins.play_music import plug_music
from src.plugins.change_window import plug_change_window

funcs_exe_plug = [
    plug_open,
    plug_music,
    plug_change_window
]
dict_choice_lang = {
    "fr": "fr",
    "en": "en-us"
}
dict_choice_engine = {
    "vosk": use_vosk.main,
    "speechrecognition": use_speech_recognition.main
}

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

parser = argparse.ArgumentParser(description='tool to recognize default action by speech')
parser.add_argument(
    "--list-lang",
    action="store_const",
    const=True,
    default=False,
    help="get list of availible lang"
)
parser.add_argument(
    "--list-engine",
    action="store_const",
    const=True,
    default=False,
    help="get list of availible engine"
)
parser.add_argument(
    "--lang",
    dest="lang",
    type=str,
    nargs=1,
    required=False,
    default=["en"],
    help="specify the language"
)
parser.add_argument(
    "--engine",
    dest="engine",
    type=str,
    nargs=1,
    required=False,
    default=["vosk"],
    help="specify the speech recognition engine"
)

res = parser.parse_args()
if res.lang[0] not in dict_choice_lang:
    print(f"{res.lang[0]} not availible (see --list-lang)", file=sys.stderr)
    exit(1)
lang = dict_choice_lang[res.lang[0]]
if res.engine[0] not in dict_choice_engine:
    print(f"{res.engine[0]} not availible (see --list-engine)")
    exit(1)
engine = dict_choice_engine[res.engine[0]]
engine(lang=lang, funcs_exe_plug=funcs_exe_plug)

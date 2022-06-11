import gtts
import os
import miniaudio

file_save = "/tmp/tmp_save.mp3"

need_end = False

def stream_end_callback() -> None:
    global need_end
    need_end = True

def play_file(filename: str):
    """
    play a file with the speakers
    """
    global need_end
    need_end = False
    stream = miniaudio.stream_file(filename)
    stream_callback = miniaudio.stream_with_callbacks(stream, end_callback=stream_end_callback)
    next(stream_callback)
    with miniaudio.PlaybackDevice() as device:
        device.start(stream_callback)
        while need_end == False:
            continue

def say(text: str, lang: str):
    """
    say a text in the lang
    lang format:
        'af': 'Afrikaans',
        'ar': 'Arabic',
        'bg': 'Bulgarian',
        'bn': 'Bengali',
        'bs': 'Bosnian',
        'ca': 'Catalan',
        'cs': 'Czech',
        'cy': 'Welsh',
        'da': 'Danish',
        'de': 'German',
        'el': 'Greek',
        'en': 'English',
        'eo': 'Esperanto',
        'es': 'Spanish',
        'et': 'Estonian',
        'fi': 'Finnish',
        'fr': 'French',
        'gu': 'Gujarati',
        'hi': 'Hindi',
        'hr': 'Croatian',
        'hu': 'Hungarian',
        'hy': 'Armenian',
        'id': 'Indonesian',
        'is': 'Icelandic',
        'it': 'Italian',
        'iw': 'Hebrew',
        'ja': 'Japanese',
        'jw': 'Javanese',
        'km': 'Khmer',
        'kn': 'Kannada',
        'ko': 'Korean',
        'la': 'Latin',
        'lv': 'Latvian',
        'mk': 'Macedonian',
        'ms': 'Malay',
        'ml': 'Malayalam',
        'mr': 'Marathi',
        'my': 'Myanmar (Burmese)',
        'ne': 'Nepali',
        'nl': 'Dutch',
        'no': 'Norwegian',
        'pl': 'Polish',
        'pt': 'Portuguese',
        'ro': 'Romanian',
        'ru': 'Russian',
        'si': 'Sinhala',
        'sk': 'Slovak',
        'sq': 'Albanian',
        'sr': 'Serbian',
        'su': 'Sundanese',
        'sv': 'Swedish',
        'sw': 'Swahili',
        'ta': 'Tamil',
        'te': 'Telugu',
        'th': 'Thai',
        'tl': 'Filipino',
        'tr': 'Turkish',
        'uk': 'Ukrainian',
        'ur': 'Urdu',
        'vi': 'Vietnamese',
        'zh-CN': 'Chinese',
        'zh-TW': 'Chinese (Mandarin/Taiwan)',
        'zh': 'Chinese (Mandarin)'
    """
    tts = gtts.gTTS(text=text, lang=lang)
    tts.save(file_save)
    play_file(file_save)
    os.remove(file_save)

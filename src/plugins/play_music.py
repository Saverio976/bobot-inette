import pyautogui
import webbrowser
from youtubesearchpython import VideosSearch

ok_text = ["play", "joue"]

def open_music() -> bool:
    music = pyautogui.prompt("Enter music name")
    if music == None:
        return False
    res = VideosSearch(music, 1)
    if res == None:
        return False
    result = res.result()
    if isinstance(result, str) or len(result['result']) == 0:
        return False
    link = result['result'][0]['link']
    print(link)
    webbrowser.open_new(link)
    return True

def plug_music(text: str):
    splits = text.split()
    if len(splits) == 0:
        return (False, False)
    for tex in splits:
        xd_ok = False
        for to_check in ok_text:
            if tex.startswith(to_check):
                xd_ok = True
        if xd_ok:
            res = open_music()
            return (True, res)
    return (False, False)

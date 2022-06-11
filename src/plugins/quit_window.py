import os
import signal
import pyautogui
from xdo import Xdo

ok_text = ["quit", "quitte"]

def quit_window() -> bool:
    x = Xdo()
    win = x.get_active_window()
    name = x.get_window_name(win)
    confirm = pyautogui.confirm(f"Close {name}.")
    if confirm != "OK":
        return False
    pid = x.get_pid_window(win)
    os.kill(pid, signal.SIGQUIT)
    return True

def plug_quit_window(text: str):
    splits = text.split()
    if len(splits) == 0:
        return (False, False)
    for tex in splits:
        xd_ok = False
        for to_check in ok_text:
            if tex.startswith(to_check):
                xd_ok = True
        if xd_ok:
            res = quit_window()
            return (True, res)
    return (False, False)

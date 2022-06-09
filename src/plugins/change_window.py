import os
import pyautogui
# import xdoctl
# import subprocess
# import shlex

ok_text = ["go to", "va"]

# def exec_return_ouput_list(li: list) -> list:
#     try:
#         ret = subprocess.check_output(li, timeout=2)
#     except subprocess.TimeoutExpired:
#         return []
#     return (ret.decode('utf-8')).splitlines()
#
# def exec_return_ouput(command: str) -> list:
#     return exec_return_ouput_list(shlex.split(command))
#
# def change_window() -> bool:
#     app = pyautogui.prompt("Which application do you want to go ?")
#     if app == None:
#         return False
#     print(f"app : {app}")
#     win_ids = exec_return_ouput(f"xdotool search --sync --onlyvisible --maxdepth 2 --name {app}")
#     print(f"win_ids : {win_ids}")
#     if len(win_ids) == 0 or win_ids[0] == "":
#         return False
#     exec_return_ouput(f"xdotool windowactivate {win_ids[0]}")
#     print("xddd")
#     return True

# def change_window() -> bool:
#     app = pyautogui.prompt("Which application do you want to go ?")
#     if app == None:
#         return False
#     res = xdoctl.window.search(app ,sync=True, only_visible=True, match_all=True)
#     if res == None or len(res) == 0:
#         return False
#     xdoctl.window.window_focus(res[0], sync=True)
#     return True

def change_window() -> bool:
    return False

def plug_change_window(text: str):
    splits = text.split()
    if len(splits) == 0:
        return (False, False)
    for tex in splits:
        xd_ok = False
        for to_check in ok_text:
            if tex.startswith(to_check):
                xd_ok = True
        if xd_ok:
            res = change_window()
            return (True, res)
    return (False, False)

import pyautogui
from xdo import Xdo

ok_text = ["go to", "va"]

def change_window() -> bool:
    app: str = pyautogui.prompt("Which application do you want to go ?")
    if app == None:
        return False
    x = Xdo()
    nb_deskt = x.get_number_of_desktops()
    cur_deskt = x.get_current_desktop()
    for i in range(1, nb_deskt + 1):
        x.set_current_desktop(i)
        res = x.search_windows(bytes(app, 'utf-8'), only_visible=True, max_depth=2, require=True)
        if res != None and len(res) != 0:
            print(res)
            x.activate_window(res[-1])
            return True
    x.set_current_desktop(cur_deskt)
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

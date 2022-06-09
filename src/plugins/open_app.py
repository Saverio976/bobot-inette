import os
import pyautogui

ok_text = ["open", "ouvre"]

def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)
    fpath, _ = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file
    return None

def open_app() -> bool:
    app = pyautogui.prompt("Which application do you want to open ?")
    if app == None:
        return False
    prog = which(app)
    if prog == None:
        print(f"OPEN: cannot find {app}")
        return False
    process = os.fork()
    if process > 0:
        return True
    else:
        os.execlp(app, app)
    exit(0)

def plug_open(text: str):
    splits = text.split()
    if len(splits) == 0:
        return (False, False)
    for tex in splits:
        xd_ok = False
        for to_check in ok_text:
            if tex.startswith(to_check):
                xd_ok = True
        if xd_ok:
            res = open_app()
            return (True, res)
    return (False, False)

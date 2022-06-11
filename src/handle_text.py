def handle_text_mic(text: str, funcs_exe_plug: list) -> tuple:
    """
    call each function of funcs_exe_plug with text
    """
    ret1, ret2 = False, False
    for func in funcs_exe_plug:
        ret1, ret2 = func(text)
    return ret1, ret2

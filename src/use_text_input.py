class EngineTextInput:
    def __init__(self, lang: str = "en", funcs_exe_plug: list = []):
        self._lang = lang
        self._funcs_exe_plug = funcs_exe_plug

    def get_sentence(self) -> str:
        text = ""
        try:
            text = input("enter input: ")
        except Exception as _:
            return text
        return text

    def end(self):
        return None

def get_engine():
    return EngineTextInput

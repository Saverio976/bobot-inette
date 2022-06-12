from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

from ..text_to_speech import say

ok_text = ["jarvis"]

class Jarvis:
    def __init__(self, model: str = "microsoft/DialoGPT-small"):
        say("Creation of me", "en")
        self._model = AutoModelForCausalLM.from_pretrained(model)
        self._tokenizer = AutoTokenizer.from_pretrained(model)
        self._chat_history = None
        self._count = 0
        say("I can talk and understand only in english", "en")

    def generate_response(self, inp: str):
        new_inp_ids = self._tokenizer.encode(inp + self._tokenizer.eos_token, return_tensors='pt')
        bot_inp_ids = torch.cat([self._chat_history, new_inp_ids], dim=-1) if self._count > 0 else new_inp_ids
        self._chat_history = self._model.generate(bot_inp_ids, max_length=1250, pad_token_id=self._tokenizer.eos_token_id)
        message = self._tokenizer.decode(self._chat_history[:, bot_inp_ids.shape[-1]:][0], skip_special_tokens=True)
        say(message, "en")

def bring_jarvis(engine):
    not_end = True
    jarvis = Jarvis("microsoft/DialoGPT-large")
    say("say quit to stop talk to me", "en")
    while not_end == True:
        text: str = engine.get_sentence()
        not_end = not text.endswith("quit")
        if not_end == False:
            continue
        jarvis.generate_response(text)
    say("Bye, see ya", "en")

def plug_jarvis(text: str, engine):
    splits = text.split()
    if len(splits) == 0:
        return (False, False)
    for tex in splits:
        xd_ok = False
        for to_check in ok_text:
            if tex.startswith(to_check):
                xd_ok = True
        if xd_ok:
            res = bring_jarvis(engine)
            return (True, res)
    return (False, False)

from dp.phonemizer import Phonemizer
from cached_path import cached_path
from num2words import num2words
import re
class OpenPhonemizer:
    def __init__(self, model_checkpoint=None):
        if not model_checkpoint:
            model_checkpoint = str(cached_path('hf://openphonemizer/ckpt-001-alpha/prelim_ckpts/model_step_20k_fixed.pt'))
        self.phonemizer = Phonemizer.from_checkpoint(model_checkpoint)
        self.pattern = re.compile(r'\d+')
    def _num_process(self, text):
        matches = self.pattern.findall(text)
        for match in matches:
            word_equivalent = num2words(int(match))
            text = text.replace(match, word_equivalent)
        return text
    def __call__(self, text):
        return self.phonemizer(self._num_process(text), lang='en_us')
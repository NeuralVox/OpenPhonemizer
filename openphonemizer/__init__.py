from dp.phonemizer import Phonemizer
from cached_path import cached_path

class OpenPhonemizer:
    def __init__(self, model_checkpoint=str(cached_path('https://public-asai-dl-models.s3.eu-central-1.amazonaws.com/DeepPhonemizer/en_us_cmudict_ipa_forward.pt'))):
        self.phonemizer = Phonemizer.from_checkpoint(model_checkpoint)
    def __call__(self, text):
        return self.phonemizer(text, lang='en_us')
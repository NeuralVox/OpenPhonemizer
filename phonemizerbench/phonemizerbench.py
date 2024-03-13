from dp.phonemizer import Phonemizer
from rapidfuzz import fuzz
from tqdm import tqdm
from random import sample
from cached_path import cached_path

phnphonemizer = Phonemizer.from_checkpoint(
    str(
        cached_path(
            "https://public-asai-dl-models.s3.eu-central-1.amazonaws.com/DeepPhonemizer/en_us_cmudict_ipa_forward.pt"
        )
    )
)
import phonemizer

global_phonemizer = phonemizer.backend.EspeakBackend(
    language="en-us",
    preserve_punctuation=True,
    with_stress=True,
    words_mismatch="ignore",
)


def phonemizerfunc(text):
    text = text.strip()
    text = text.replace('"', "")
    ps = global_phonemizer.phonemize([text])[0]
    return ps


from collections.abc import Iterable
from gruut import sentences


def gruut(text):
    phonemized = []
    for sent in sentences(text, lang="en-us"):
        for word in sent:
            if isinstance(word.phonemes, Iterable):
                phonemized.append("".join(word.phonemes))
            elif isinstance(word.phonemes, str):
                phonemized.append(word.phonemes)
    phonemized_text = " ".join(phonemized)
    return phonemized_text


with open("phrases.txt") as f:
    text = sample(f.read().strip().splitlines(), 100)
x = []
for t in tqdm(text):
    # x.append(fuzz.ratio(phonemizerfunc(t), phnphonemizer.phonemize(t)))
    x.append(fuzz.ratio(phonemizerfunc(t), gruut(t)))

print("Avg score:", sum(x) / len(x))

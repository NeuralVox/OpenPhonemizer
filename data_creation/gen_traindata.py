import phonemizer
from tqdm import tqdm
global_phonemizer = phonemizer.backend.EspeakBackend(language='en-us', preserve_punctuation=True, with_stress=True, words_mismatch='ignore')
def phonemize(text):
    text = text.strip()
    text = text.replace('"', '')
    ps = global_phonemizer.phonemize([text])
    return ps[0].strip()
with open('en.txt') as f:
    words = f.read().strip().splitlines()
with open('out.txt', 'w') as f:
    for word in tqdm(words):
        f.write(word + "\t" + phonemize(word) + "\n")
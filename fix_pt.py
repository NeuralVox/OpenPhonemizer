MODEL_PATH = 'model_step_20k_fixed.pt'
import torch
from cached_path import cached_path
x = torch.load(MODEL_PATH)
with open(str(cached_path('https://huggingface.co/datasets/mrfakename/ipa-phonemes-word-pairs/raw/main/out.tsv'))) as f:
    lines = [l.replace(' ', '').replace('\n', '') for l in f.readlines()]
splits = [l.split('\t') for l in lines]
# for z in splits:
#     x['phoneme_dict']['en_us'][z[0]] = z[1]
x['phoneme_dict']['en_us']['a']='ɐ'
print(x['phoneme_dict']['en_us'])
torch.save(x, 'model_step_20k_fixed.pt')
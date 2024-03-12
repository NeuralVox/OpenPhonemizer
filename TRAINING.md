# Training

(Some code borrowed from DeepPhonemizer)

Assuming you're using Jupyter:

```
!pip install deep-phonemizer
```

```python
!wget https://huggingface.co/datasets/mrfakename/ipa-phonemes-word-pairs/raw/main/out.tsv
with open('eng_latn_us_broad.tsv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

lines = [l.replace(' ', '').replace('\n', '') for l in lines]
splits = [l.split('\t') for l in lines]
train_data = [('en_us', s[0], s[1]) for s in splits if len(s)==2]
for d in train_data[:10000:1000]:
    print(d)
```

```python
from dp.utils.io import read_config, save_config
import dp
import os

config_file = 'training/config.yml'
config = read_config(config_file)
config['training']['epochs'] = 100
config['training']['warmup_steps'] = 100
config['training']['generate_steps'] = 500
config['training']['validate_steps'] = 500
save_config(config, 'config.yaml')
for k, v in config.items():
    print(f'{k} {v}')
```

```
%load_ext tensorboard
%tensorboard --logdir /content/checkpoints
```

```python
from dp.preprocess import preprocess
from dp.train import train
preprocess(config_file='config.yaml', train_data=train_data)
train(config_file='config.yaml')
```

```python
from dp.phonemizer import Phonemizer

phonemizer = Phonemizer.from_checkpoint('/content/checkpoints/best_model.pt')
result = phonemizer('Phonemizing an English text is imposimpable!', lang='en_us')

print(result)
```

```python
result = phonemizer.phonemise_list(['This is a test'], lang='en_us')

for word, pred in result.predictions.items():
    print(f'{word} {pred.phonemes} {pred.confidence}')
```
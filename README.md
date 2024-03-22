# OpenPhonemizer

**[Audio Samples](https://neuralvox.github.io/OpenPhonemizer/) / [Models](https://huggingface.co/openphonemizer/ckpt) / [Live Demo](https://huggingface.co/spaces/openphonemizer/PhonemizerHub) / [Dataset](https://huggingface.co/datasets/mrfakename/ipa-phonemes-word-pairs)**

A permissively licensed, open sourced, local IPA Phonemizer (G2P) powered by deep learning. This Phonemizer attempts to replicate the `espeak` Phonemizer while remaining permissively-licensed.

OpenPhonemizer is heavily based on the amazing [DeepPhonemizer](https://github.com/as-ideas/DeepPhonemizer). The main changes are the model checkpoints, which more closely resembles `espeak`'s phonemizer.

Optional GPL-licensed portions are available [here](https://github.com/NeuralVox/OpenPhonemizer-GPL).

## Features

* Permissively licensed & open source
* Fast & efficient
* Works well with TTS models that depend on phonemizer or espeak
* Automatic GPU acceleration (CUDA/MPS) if available

## Project

* Project status: Alpha
* Supported languages: English (more coming soon! What languages do you want? Let me know!)

## Installation

Easily install OpenPhonemizer:

```bash
pip install -U openphonemizer
```

Or, install the latest version from Git:

```bash
pip install -U "openphonemizer @ git+https://github.com/NeuralVox/OpenPhonemizer"
```

## Usage

### OpenPhonemizer

```python
from openphonemizer import OpenPhonemizer
phonemizer = OpenPhonemizer()
# Or specify a custom checkpoint path: OpenPhonemizer('model.pt')
phonemizer('test')
phonemizer('hello this is a test')
```

Please note that by default, OpenPhonemizer loads a built-in dictionary of words/phonemes. Because storage is quite inefficient, the model is ~100MB larger and uses more memory, however it is _much_ faster. If you're low on VRAM, you can either run the model exclusively on CPU (`disable_gpu=True`) or load a model without a dictionary.

**Load without dictionary:**

```python
from cached_path import cached_path
from openphonemizer import OpenPhonemizer
phonemizer = OpenPhonemizer(str(cached_path('hf://openphonemizer/ckpt/best_model_no_optim.pt'))) # add disable_gpu=True to run on CPU only
phonemizer('test')
phonemizer('hello this is a test')
```

**[NEW] Use autoregressive model:**

NEW: An autoregressive model is now available. The autoregressive model is more accurate but slightly slower. To use the autoregressive model:

```python
OpenPhonemizer(str(cached_path('hf://openphonemizer/autoreg-ckpt/best_model.pt')))
```

## Evaluation

We introduce PhonemizerBench, a benchmark to evaluate the similarity of alternate Phonemizers to `espeak` (this benchmark measures against `espeak`, assuming it's score is 100).

**Run 1**

| Phonemizer | Score |
| --- | --- |
| Gruut | 75.08 |
| DeepPhonemizer | 85.24 |
| G2P_EN | 86.16 |
| OpenPhonemizer | 93.64 |
| OpenPhonemizer Autoregressive | **93.74** |

**Run 2**

| Phonemizer | Score |
| --- | --- |
| Gruut | 75.54 |
| DeepPhonemizer | 85.03 |
| G2P_EN | 86.28 |
| OpenPhonemizer | 93.54 |
| OpenPhonemizer Autoregressive | **93.59** |

**Run 3**

| Phonemizer | Score |
| --- | --- |
| Gruut | 73.72 |
| DeepPhonemizer | 84.64 |
| G2P_EN | 85.74 |
| OpenPhonemizer | 93.38 |
| OpenPhonemizer Autoregressive | **93.67** |

## Todo

- [x] Train autoregressive model
- [x] Allow disabling GPU usage
- [ ] Multilingual support (any requests?)

## License

OpenPhonemizer is open source software. You may use it under the BSD-3-Clause Clear license found in the LICENSE file.

Please note that OpenPhonemizer depends on software under different licenses, it is your responsibility when redistributing or modifying OpenPhonemizer to comply with these licenses (notably LGPL).

*By contributing to this repository, you grant the author the permission to change the license in the future at their sole discretion or offer different licenses to other individuals.*

**NOTE:** Model weights may be licensed under different licenses. Please make sure to check all model weights for licenses.

## Credits

Special thanks to [Christian Schäfer](https://github.com/cschaefer26), who created [Deep Phonemizer](https://github.com/as-ideas/DeepPhonemizer), on which OpenPhonemizer relies. OpenPhonemizer uses [num2words](https://github.com/savoirfairelinux/num2words) to read out large numbers and [cached_path](https://github.com/allenai/cached_path) from Allen AI for caching models.

OpenPhonemizer was created by [mrfakename](https://twitter.com/realmrfakename).

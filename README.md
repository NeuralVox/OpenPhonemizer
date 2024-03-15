# OpenPhonemizer

**[Audio Samples](https://neuralvox.github.io/OpenPhonemizer/) / [Live Demo](https://huggingface.co/spaces/openphonemizer/PhonemizerHub)**

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
pip install openphonemizer
```

Or, install the latest version from Git:

```bash
pip install "openphonemizer @ git+https://github.com/NeuralVox/OpenPhonemizer"
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

## Evaluation

We introduce PhonemizerBench, a benchmark to evaluate the similarity of alternate Phonemizers to `espeak`.

**Run 1**

| Phonemizer | Score |
| --- | --- |
| Gruut | 75.08 |
| DeepPhonemizer | 85.24 |
| OpenPhonemizer | 93.64 |

**Run 2**

| Phonemizer | Score |
| --- | --- |
| Gruut | 75.54 |
| DeepPhonemizer | 85.03 |
| OpenPhonemizer | 93.54 |

**Run 3**

| Phonemizer | Score |
| --- | --- |
| Gruut | 73.72 |
| DeepPhonemizer | 84.64 |
| OpenPhonemizer | 93.38 |

## Todo

- [ ] Train autoregressive model
- [ ] Allow disabling GPU usage

## License

OpenPhonemizer is open source software. You may use it under the BSD-3-Clause Clear license found in the LICENSE file.

*By contributing to this repository, you grant the author the permission to change the license in the future at their sole discretion.*

**NOTE:** Model weights may be licensed under different licenses. Please make sure to check all model weights for licenses.

## Credits

Special thanks to [Christian Schäfer](https://github.com/cschaefer26), who created [Deep Phonemizer](https://github.com/as-ideas/DeepPhonemizer), on which OpenPhonemizer relies.

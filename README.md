# OpenPhonemizer

A permissively licensed, open sourced, local IPA Phonemizer (G2P) powered by deep learning. This Phonemizer attempts to replicate the `espeak` Phonemizer while remaining permissively-licensed.

## Project

* Project status: Alpha
* Supported languages: English (more coming soon!)

## Usage

**Coming soon**

## Evaluation

Coming soon: evaluation on accuracy (% of `espeak` accuracy)

## Credits

Parts of OpenPhonemizer are based on [Deep Phonemizer](https://github.com/as-ideas/DeepPhonemizer).

## Evaluation

We introduce PhonemizerBench, a benchmark to evaluate the similarity of alternate Phonemizers to `espeak`.

**Run 1**

| Phonemizer | Score |
| --- | --- |
| Gruut | 75.08 |
| Deep Phonemizer | 93.6 |

**Run 2**

| Phonemizer | Score |
| --- | --- |
| Gruut | 75.54 |
| Deep Phonemizer | 93.47 |

**Run 3**

| Phonemizer | Score |
| --- | --- |
| Gruut | 73.72 |
| Deep Phonemizer | 93.68 |

## License

OpenPhonemizer is open source software. You may use it under the BSD-3-Clause Clear license found in the LICENSE file.

**Please note** that certain tools provided with OpenPhonemizer are licensed under the GNU General Public License, version 3.0, as certain parts of OpenPhonemizer rely on the `phonemizer` library. These components have been isolated and are not linked by the rest of the software. Unless otherwise specified in a README file, all other components of OpenPhonemizer are licensed under the BSD-3-Clause Clear license.

*By contributing to this repository, you grant the author the permission to change the license in the future at their sole discretion.*

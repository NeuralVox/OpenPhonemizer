# OpenPhonemizer
# 
# Copyright (c) 2024 mrfakename, NeuralVox, OpenPhonemizer Contributors
# All rights reserved.
# 
# The Clear BSD License

# Redistribution and use in source and binary forms, with or without
# modification, are permitted (subject to the limitations in the disclaimer
# below) provided that the following conditions are met:

#  * Redistributions of source code must retain the above copyright notice,
# this list of conditions and the following disclaimer.

#  * Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.

#  * Neither the name of the copyright holder nor the names of its
# contributors may be used to endorse or promote products derived from this
# software without specific prior written permission.

# NO EXPRESS OR IMPLIED LICENSES TO ANY PARTY'S PATENT RIGHTS ARE GRANTED BY
# THIS LICENSE. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND
# CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
# PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
# IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from dp.phonemizer import Phonemizer
from cached_path import cached_path
from num2words import num2words
import re, torch
class OpenPhonemizer:
    def __init__(self, model_checkpoint=None):
        device = 'cpu'
        if torch.cuda.is_available(): device = 'cuda'
        if torch.backends.mps.is_available(): device = 'mps'
        if not model_checkpoint:
            model_checkpoint = str(cached_path('hf://openphonemizer/ckpt/best_model.pt'))
        self.phonemizer = Phonemizer.from_checkpoint(model_checkpoint, device=device)
        self.pattern = re.compile(r'\d+')
    def _num_process(self, text):
        matches = self.pattern.findall(text)
        for match in matches:
            word_equivalent = num2words(int(match))
            text = text.replace(match, word_equivalent)
        return text
    def __call__(self, text, stress=True):
        out = self.phonemizer(self._num_process(text.replace(' .', '.').replace('.', ' .')), lang='en_us')
        if not stress:
            out = out.replace('ˈ', '')
        return out

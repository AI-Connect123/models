# Copyright 2023 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""TensorFlow Models NLP Libraries."""

from official.nlp import tasks
from official.nlp.configs import encoders
from official.nlp.modeling import *
from official.nlp.serving import serving_modules
mport googletrans
from googletrans import Translator 
# To detect and translate text

import speech_recognition as sr 
# To recognize speech

from gtts import gTTS.nlp.modeling import * 
# Google speech-to-Speech to convert recording audio to audio

import os 
# To work with files
import googletrans
We import the googletrans module.
print(googletrans.LANGUAGES)
We print the googletrans.LANGUAGES variable.
$ languages.py
{'arabic': 'english', ... }

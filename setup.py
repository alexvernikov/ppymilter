#!/usr/bin/env python
# $Id: setup.py 22 2008-08-08 18:44:33Z codewhale $
# ==============================================================================
# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from distutils.core import setup

setup(name='ppymilter',
      version='0.1',
      description='Pure Python Milter Library',
      author='Eric DeFriez',
      author_email='codewhale@gmail.com',
      url='http://code.google.com/p/ppymilter',
      package_dir={'ppymilter': 'lib'},
      packages=['ppymilter'],
      scripts=['lib/ppymilterserver.py'])

"""
 *  discordlists.py: A simple API wrapper for botblock.org providing server count posting to all bot lists and fetching
 *   bot information from all.
 *  <https://github.com/MattIPv4/discordlists.py/>
 *  Copyright (C) 2019 Matt Cowley (MattIPv4) (me@mattcowley.co.uk)
 *
 *  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
 *   documentation files (the "Software"), to deal in the Software without restriction, including without limitation
 *   the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and
 *   to permit persons to whom the Software is furnished to do so, subject to the following conditions:
 *
 *  The above copyright notice and this permission notice shall be included in all copies or substantial portions of
 *   the Software.
 *
 *  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
 *   THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 *   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
 *   CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
 *   IN THE SOFTWARE.
 *
 *   <https://github.com/MattIPv4/discordlists.py/blob/master/LICENSE>
"""

from setuptools import setup

__title__ = 'discordlists.py'
__author__ = 'MattIPv4 & HexCodeFFF'
__version__ = '2.0'

if not __title__:
    raise RuntimeError('title is not set')
if not __author__:
    raise RuntimeError('author is not set')
if not __version__:
    raise RuntimeError('version is not set')

with open("requirements.txt", "r") as f:
    requirements = f.readlines()

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name=__title__,
    author=__author__,
    url="https://github.com/HexCodeFFF/discordlists.py/",
    version=__version__,
    packages=['discordlists'],
    python_requires=">= 3.5",
    include_package_data=True,
    install_requires=requirements,
    description="simple fork of discordlists.py which uses nextcord",
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="api wrapper discord bot bots stats statistics botblock server guild count list lists get post botlist "
             "nextcord",
    classifiers=(
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ),
    project_urls={
        'Source': 'https://github.com/HexCodeFFF/discordlists.py/',
    },
)

# How2Ship:tm:
# 1. Update version in discordlists/__init__.py
# 2. Run python3 setup.py sdist bdist_wheel bdist_egg
# 3. Run python3 -m twine upload dist/*

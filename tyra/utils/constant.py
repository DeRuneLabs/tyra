# MIT License
#
# Copyright (c) 2024 DeRuneLabs
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import platform
import os

MAJOR_VERSION: str = "1"
MINOR_VERSION: str = "0"
PATCH_VERSION: str = "0"

LICENSE_LIST: list = ["MIT", "GNU", "APACHE", "UNLINCENSE"]
NEWLINE: str = "\n"


def show_system_information() -> None:
    print(f"Operating System: {platform.system()}")
    print(f"User: {platform.node()}")
    print(f"OS ver: {platform.version()}")
    print(f"proc info: {platform.processor()}")
    print(f"architecture: {platform.architecture()}")
    print(f"python version: {platform.python_version()}")
    print(f"python interpreter path: {os.__file__}")
    print(f"Tyra project automator version {MAJOR_VERSION}.{MINOR_VERSION}.{PATCH_VERSION}")

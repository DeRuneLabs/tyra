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

import os
import tyra.utils.constant as constant


def list_information_license(directory: str) -> None:
    """
    Print list all license information

    Paramter:
        directory(str): directory name of list of license
    """
    data_list = [os.path.splitext(file)[0] for file in os.listdir(directory) if file.endswith(".txt")]
    print("List License Information")
    for list_license in data_list:
        print(list_license)


def open_license_file(filename: str) -> str:
    """
    Open license TXT files

    Parameter:
        filename(str): name of file

    Return:
        str: string contains license each license text 
    """
    if filename.upper() in constant.LICENSE_LIST:
        try:
            with open(f"utils/license_dat/{filename.lower()}.txt", "r") as license_file:
                file_content: str = license_file.read()
            return file_content
        except Exception as error_opening_file:
            raise error_opening_file


if __name__ == "__main__":
    list_information_license("license_dat")

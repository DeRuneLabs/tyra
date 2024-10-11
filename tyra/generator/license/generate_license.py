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

import tyra.utils.constant as constant
import tyra.generator.license.license as license_desc
from string import Template

license_name: object = Template(license_desc)
data_license: list = [data for data in constant.LICENSE_LIST]


def _validate_input(license_name: str, author_name: str, year: int) -> None:
    """
    Validate input

    Parameter:
        license_name(str): license name must be string data types
        author_name(st): author name must be string data types
        year(int): year must be integer

    Throws:
        TypeError: if license_name, author_name, year wrong data types
    """
    if not (isinstance(license_name, str) and isinstance(author_name, str) and isinstance(year, str)):
        raise TypeError(f"{constant.RED}license_name and author_name must be str, and year must be str{constant.RESET}")


def _write_license_to_file(content: str) -> None:
    """
    Writing license to files

    Parameter:
        content(str): content to writing and create LICENSE
    """
    with open("LICENSE", "w") as generate_license:
        generate_license.write(content)
    print(f"{constant.GREEN}Success generate license...!{constant.RESET}")


def generate(license_name: str, author_name: str, year: int) -> None:
    """
    Generate license and write to file called name LICENSE

    Parameter:
        license_name(str): license name
        author_name(str): author name
        year(int): license year
    """
    _validate_input(license_name, author_name, year)
    license_name_upper_text = license_name.upper()
    if license_name_upper_text not in constant.LICENSE_LIST:
        print(f"{constant.RED}License not found{constant.RESET}")
        return
    license_template = license_desc.open_license_file(license_name_upper_text)
    license_name_info = f"{constant.GREEN}Generating {license_name.capitalize()} License... {constant.RESET}"
    print(license_name_info)

    templated_licenses = {"MIT", "APACHE", "ISC", "BSD3-CLAUSE"}
    if license_name_upper_text in templated_licenses:
        license_template = Template(license_template).safe_substitute(year=str(year), author=author_name)
    _write_license_to_file(license_template)

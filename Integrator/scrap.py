#!/usr/bin/generic python
# -*- coding: utf-8 -*-

"""
    Description: Script to obtain fundamental analysis information registered
    in the site http://www.fundamentus.com.br/ and to insert a database for
    consultation of the scripts and execution of the calculations.
"""

import requests
import re

class Stickers:
    if __name__ == "__main__":
        print("Python module!")
    else:
        def __init__(self, url):
            self.response = requests.get(url)
            self.page_content = str(self.response.text)
            self.fundamentalist_data = re.findall(r'\d+,\d+', self.page_content)

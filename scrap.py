#!/usr/bin/generic python
# -*- coding: utf-8 -*-

"""
    Description: Script to obtain fundamental analysis information registered
    in the site http://www.fundamentus.com.br/ and to insert a database for
    consultation of the scripts and execution of the calculations.
"""

__author__ = "Jean Ruffato"
__email__ = "jean.ruffato@gmail.com"
__version__ = "1.0.0"
__date__ = "2018/02/27"


import requests
from html.parser import HTMLParser


def ambev():
    # Function to perform scraping of Ambev's stock information
    response = requests.get('http://www.fundamentus.com.br/detalhes.php?papel=ABEV3&x=48&y=9')
    analyzer_base = str(response.content)

    class Response_analyzer(HTMLParser):
        # Function to generate elegant error messages
        def error(self, message):
            pass

        # Function to extract data from Abev's information page
        def handle_data(self, data):
            print("Data:", data, HTMLParser.getpos(self))

    # Code that pass html content to Response analyzer execute your job
    Response_analyzer().feed(analyzer_base)


def bancobrasil():
    pass


print(ambev())

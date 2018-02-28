#!/usr/bin/generic python
# -*- coding: utf-8 -*-

"""
    Descrição: Script para obter informações de análise fundamentalista
    registradas no site http://www.fundamentus.com.br/ e inserir em um
    banco de dados para consulta dos scripts e execução dos calclos
"""

__author__ = "Jean Ruffato"
__email__ = "jean.ruffato@gmail.com"
__version__ = "1.0.0"
__date__ = "2018/02/27"


import requests
# from bs4 import BeautifulSoup


def ambev():
    # Função para realizar scrapping das informações das ações da Ambev
    response = requests.get('http://201.82.5.94:8080')


def bancobrasil():
    pass

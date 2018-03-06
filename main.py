#!/usr/bin/generic python
# -*- coding: utf-8 -*-

"""
    Description: Script python para calcular lucro de um investimento no mercado de ações
"""

__author__ = "Jean Ruffato"
__email__ = "jean.ruffato@gmail.com"
__version__ = "1.0.0"
__date__ = "2018/02/27"


from scrap import Stickers


ambev = Stickers('http://www.fundamentus.com.br/detalhes.php?papel=ABEV3&x=37&y=19')
print(ambev.fundamentalist_data[0])

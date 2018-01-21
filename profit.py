# -*- coding: utf-8 -*-
"""
    Responsável: Jean Ruffato
    Data: 21/01/2018
    Descrição: Script python para calcular lucro de um investimento no mercado de ações
"""
import os, time

i = 0
while i < 1:

    # Desenho do cabeçalho da tabela
    os.system('cls' if os.name == 'nt' else 'clear')
    print('', '\033[34m' + '-' * 59 + '\033[0;0m')
    print('\033[34m'+'|    Ticker', '  |    Quantidade', '    |   Valor', '   |  Varição % |'+'\033[0;0m ')
    print('', '\033[34m' + '-' * 59 + '\033[0;0m')

    # Corpo da tabela com os dados da ações
    print('|\033[32m'+'     ABEV3F'+'\033[0;0m', ' |         19', '       | R$8418,00', ' |  +2,28%', '   |')
    print('', '\033[34m' + '-' * 59 + '\033[0;0m')
    print('|\033[32m'+'     PETR4F'+'\033[0;0m', ' |         10', '       | R$8418,00', ' |  +2,28%', '   |')
    print('', '\033[34m' + '-' * 59 + '\033[0;0m')
    print('|\033[32m'+'     BBAS3F'+'\033[0;0m', ' |         25', '       | R$8418,00', ' |  +2,28%', '   |')
    print('', '\033[34m' + '-' * 59 + '\033[0;0m')
    print('|\033[32m'+'     EMBR3F'+'\033[0;0m', ' |         13', '       | R$8418,00', ' |  +2,28%', '   |')
    print('', '\033[34m' + '-' * 59 + '\033[0;0m')
    time.sleep(2)


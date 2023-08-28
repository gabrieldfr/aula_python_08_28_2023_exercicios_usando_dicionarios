# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:11:07 2023

@author: logonrmlocal
"""

import random
paises = {'Brasil': 'Brasília', 'EUA': 'Washington', 'França': 'Paris'}
capital = random.choice(list(paises.keys()))
user = str(input(f'Qual a capital do país {capital}'))
capital
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:38:11 2023

@author: logonrmlocal
"""

translation = {'home': 'casa', 'porta': 'door', 'Monday': 'segunda'}
palavra = str(input('Digite uma palavra: '))
print(f'{translation.get(palavra, "Tradução não encontrada")}')
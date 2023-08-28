# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:45:28 2023

@author: logonrmlocal
"""

cidades = {'New York': 8623000, 'Los Angeles': 3990000, 'Chicago': 2716000}
cidade = str(input('Digite o nome da cidade: '))
populacao = cidade.get(cidade, "Cidade não encontrada")
print(populacao)
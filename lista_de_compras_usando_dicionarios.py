# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:49:28 2023

@author: logonrmlocal
"""
produtos = {'maça': 1.25, 'Banana': 0.75, 'Laranja': 0.90}
shopping_list = str(input('Digite os produtos da lista (separados por vírgula): ')).strip().split(',')
total_cost = sum(produtos[item] for item in shopping_list if item in produtos)
print(f'o custo total é: R${total_cost:.2f}')
# for item in shopping_list:
#     if item in produtos:
#         total_cost += produtos[item]
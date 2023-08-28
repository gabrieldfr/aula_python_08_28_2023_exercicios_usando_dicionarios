# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 11:06:16 2023

@author: logonrmlocal
"""
contatos = {}
while True:
    print('1. Adicionar contato\n2. Remover contato\n3. Buscar contato\4. Sair')
    choice = str(input('Escolha uma opção: ')).strip()
    match choice:
        case '1':
            nome = str(input('Nome do contato: '))
            numero = str(input('Número do contato: '))
            contatos['nome'] = numero
        case '2':
            
print('dicio_2')
dicio_2 = {'primeiro': 1, 'segundo': 2, 'terceiro': 3}
print(dicio_2)

print('dicio')
dicio = dict(primeiro = 1, segundo = 2, terceiro = 3)
print(dicio)

print('dicio_3')
dicio_3 = dict(zip(['primeiro', 'segundo', 'terceiro'], [1,2,3]))

print('dicio_6')
dicio_6 = {name: idx + 1 for idx, name in enumerate(('primeiro', 'segundo', 'terceiro'))}
print(dicio_6)

# Conferir a foto no celular
print(dicio_6.get('peso', 'Chave não encontrada'))

computador = {'CPU': 'Intel', 'RAM': '8gb', 'SSD': '250gb'}
print('Chaves do dicionário computador')
print(computador.keys())

notas = {'Mat': 10, 'Port': 8, 'Hist': 9}
print('Valores do dicionário notas')
print(notas.values())

#Verificando se a chave existe
dicio_cores = {'amarelo': 10, 'vermelho': 2, 'cinza': 55}
if 'amarelo' in dicio_cores:
    print('A cor amarelo existe')
    
#Verificando se o valor existe
if 10 in dicio_cores.values():
    print('O valor 10 existe')
    
dicio_7 = {'nome': 'Erick'}

#Atualiza o elemento da chave 'nome'
dicio_7.update({'nome': 'Matheus'})

#Cria os elementos de chave 'idade' e 'tamanho'
dicio_7.update({'idade': 18})
dicio_7

dicio_8 = {'nome', 'idade', 'peso'}
value = 0
dicio_8 = dict.fromkeys(dicio_8, value)
print((dicio_8))
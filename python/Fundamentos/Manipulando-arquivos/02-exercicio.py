"""
    try:
    counter = 0
    quantity = int(input('Quantas linhas deseja retornar: '))
    with open ('02-exercicio.txt', 'r', encoding='utf-8') as file:
        for line in file:
            #Pula a linha, caso seja so uma quebra
            if not line.rstrip():
                continue
            print(line.rstrip())
            counter += 1
            if counter == quantity:
                break
except ValueError:
    print('Valor invalido')
except FileNotFoundError:
    print("Erro: O arquivo '02-exercicio.txt' não foi encontrado.")
"""
from itertools import islice
try:
    quantity = int(input('Quantas linhas deseja retornar: '))
    with open ('02-exercicio.txt', 'r', encoding='utf-8') as file:
        for line in islice(file, quantity + 1):
            #Pula a linha, caso seja so uma quebra
            if not line.rstrip():
                continue
            print(line.rstrip())
except ValueError:
    print('Valor invalido')
except FileNotFoundError:
    print("Erro: O arquivo '02-exercicio.txt' não foi encontrado.") 
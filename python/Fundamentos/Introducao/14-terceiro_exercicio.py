'''
Cálculo da Distância

Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,35 para viagens mais longas.

Aumento salário funcionário

Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
'''


#Exercicio 1:
distancia = float(input('Qual a distância em km: '))
if distancia > 200.0:
    price = distancia*0.35
    print(f'O preço é: R${price}')
elif distancia > 0 and distancia <= 200.0:
    price = distancia*0.5
    print(f'O preço é: R${price}')
else:
    print('informação invalida!')

#Segundo exercicio:

salary = float(input('Qual o seu salário: '))

if salary > 1250.00:
    salary *= 1.1
    print(f'Seu novo salário é: R$ {salary}')
elif salary > 0 and salary <= 1250.00:
    salary *= 1.15
    print(f'Seu novo salário é: R$ {salary}')
else:
    print('Salário invalido!')
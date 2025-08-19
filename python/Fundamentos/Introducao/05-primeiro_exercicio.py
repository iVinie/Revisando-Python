'''
Antecessor e Sucessor de um número

Escreva um programa em Python que leia um número e represente o número antecessor e sucessor desse número que foi lido, utilizando operadores de atribuição.

Média de 4 notas

Escreva um programa em Python que leia quatro números e calcule a média entre esses números
'''

#Antecessor e Sucessor de um número:

num = int(input('Digite um número: '))

print (f'Sucessor: {num + 1}\nAntecessor: {num - 1}')

#Média de 4 notas

media = 0.0
for i in {1, 2, 3, 4}:
    nota = float(input(f'Digite a {i}º nota:'))
    media += nota

media /= 4
print (f'Sua média foi {media}')
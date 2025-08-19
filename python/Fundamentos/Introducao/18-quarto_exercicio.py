'''
Contagem Regressiva

Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, …, 1, 0 e disparar um “beep”.

Tabuada

Faça um programa que calcule a tabuada de um número, com valores iniciais e finais informados pelo usuário
'''
import winsound

numberList = [i for i in range (11)]
numberList.sort(reverse = True)
for i in numberList:
    print (i)
    if i == 0:
        print('beep')
        winsound.Beep(2500, 500)
        
        
number = int(input('Qual número quer calcular a tabuada: '))
numberEnd = int(input('Até que número quer calcular: '))

for i in range(numberEnd + 1):
    print(f'{number} x {i} = {i*number}')
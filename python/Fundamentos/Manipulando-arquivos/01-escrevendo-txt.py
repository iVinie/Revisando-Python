# r - leitura
# w - escrita
# a - append

name = input('Digite o seu nome: ')

#Obs.: Se usar o open direto no arquivo, precisamos usar o file.close()
#Ex.: file = open('nome do arquivo', 'r')
with open ('primeiro-txt.txt', 'w') as file:
    file.write(name)


#Para atualizar:
names = ['Pedro', 'Rodrigo', 'Hugo']
with open('primeiro-txt.txt', 'a') as file:
    for nome in names:
        file.write(f'\n{nome}')


#Leitura:
with open('primeiro-txt.txt', 'r', encoding='utf-8') as file:
    for line in file:
        #O .rstrip() remove o /n
        print(line.rstrip())

nomes = []
#Ordenando valores
with open('primeiro-txt.txt', 'r', encoding='utf-8') as file:
    for line in file:
        nomes.append(line.rstrip())
print (f'\n')
for i in sorted(nomes):
    print(i)
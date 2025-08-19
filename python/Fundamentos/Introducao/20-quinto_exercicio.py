'''
Conta letras maiúsculas e minúsculas

Escreva uma função Python que receba uma string e conte o número de letras maiúsculas e minúsculas desta string.

Lista números pares e ímpares de uma lista

Escreva uma função Python para imprimir os números pares e ímpares em duas listas separadas para cada uma.
'''
# Primeiro:


def contar_letras_maiusculas_minusculas(texto):

    contagem = {"maiusculas": 0, "minusculas": 0}
    for caractere in texto:
        if caractere.isupper():
            contagem["maiusculas"] += 1
        elif caractere.islower():
            contagem["minusculas"] += 1
    return contagem


string_exemplo = "Olá Mundo! Este é um Teste de Python."
resultado = contar_letras_maiusculas_minusculas(string_exemplo)

print(f"String original: '{string_exemplo}'")
print(f"Número de letras maiúsculas: {resultado['maiusculas']}")
print(f"Número de letras minúsculas: {resultado['minusculas']}")


#Segundo

listaPares = []
listaImpares = []

aux = 0
while aux != -1:
    aux = int(input('Digite o número  (-1 para parar): '))
    if aux % 2 == 0:
        listaPares.append(aux)
    elif aux % 2 != 0:
        listaImpares.append(aux)

print (f'{listaPares}\n{listaImpares}')
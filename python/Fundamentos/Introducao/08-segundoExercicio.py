'''
Substituindo caractere repetido

Escreva um programa Python para obter uma string de uma determinada string em que todas as ocorrências de seu primeiro caractere foram alteradas para '$', exceto o próprio primeiro caractere

Ex:

fifa 23 → fi#a 23

restart→ resta#t

Substituindo caractere repetido

Escreva um programa Python para obter uma única string de duas strings fornecidas, separadas por um espaço e troque os dois primeiros caracteres de cada string.

Ex:

abc xyz → xyc abz
'''

#Primeiro exercicio 
string = input('Digite a string: ')
primeira = string[0]
string = string.replace(primeira, '$')
string = primeira + string[1:]
print (string)

#Segundo Exercicio

string1 = input('Digite a primeira string: ')
string2 = input('Digite a segunda string: ')
str1 = string1[0:2]
str2 = string2[0:2]
str3 = f'{str2 + string1[2:] } + {str1 + string2[2:]}'
print (str3)
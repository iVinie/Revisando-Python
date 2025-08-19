gameName = 'fifa 23'
gameDescription = '''
Fifa 23 é um jogo de futebol, desenvolvido pela EA Sports
Que possibilita jogar localmente ou online
'''

print(gameName.upper()) #Deixa tudo maisculo 
print(gameName.lower()) #Deixa tudo minusculo 
print(gameName.capitalize()) #Deixa a primeira letra maiscula 
print(gameName.title()) #Deixa a primeira letra maiscula 
print(gameName.center(10, ' ')) #centraliza, quantidade de caractere e o que será usado pra completar
print(gameName.find('f')) #retorna a posição que ele encontrar esse caractere
print(gameDescription.count('f')) #conta o caractere
print(gameName.replace('fifa', 'pes')) # Altera um valor na string
print(gameDescription.split(',')) #quebra a string pelo item determinado OBS.:Extremamente útil em dados

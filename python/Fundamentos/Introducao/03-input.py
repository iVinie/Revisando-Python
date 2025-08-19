#utilizando o comentario
'''
pode ser assim também
'''

name = input('Qual nome do jogo:\n ')
yearLaunch = int(input('Qual o ano de lançamento:\n'))
gamePrice = float(input('Preço do jogo:\n'))
planIncluded = bool(input('Ta incluso no plano:\n'))

print(f'Nome do jogo: {name}\nAno de lançamento: {yearLaunch}\nPreço: {gamePrice}\nIncluso no plano: {planIncluded}')

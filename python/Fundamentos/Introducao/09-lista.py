gameFifa = ['Fifa 23', 2022, 90.50, True]
print (gameFifa)

gameList = ['Resident Evil 4', 'Minecraft', 'Green Hell', 'RDR2']

#Buscar os dois primeiros itens da lista
print(gameList[0:2])

#Buscar o ultimo item da lista
print(gameList[-1])

#Buscas jogos até uma determinada posição
print(gameList[:3])

#Buscas jogos de uma posição em diante
print(gameList[1:])

#Alguns métodos de lista:

#Tamanho da lista
print(len(gameList))

#Retornar o indice a partir do nome
print(gameList.index('Minecraft'))

#Adicionar no final da lista
gameList.append('GTA V')

#Ordenar a lista
gameList.sort() #Crescente ou alfabetica

#Copiar os itens de uma lista para outra
gameReset = gameList.copy()

#Removendo da lsta
gameReset.remove('Minecraft')

#remove todos os itens da lista
gameFifa.clear()
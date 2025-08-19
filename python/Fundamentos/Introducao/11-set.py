gamesSet = {'Fifa 23', 'RDR 2', 'Minecraft', 'Green Hell'}

#Tamanho do Set
print(len(gamesSet))

#True e 1 são considerados o mesmo valor, não pode repetir valores
exempleSet = {'Fifa 23', True, 1, 90.5}
print(exempleSet)

#Adiciona item de outro set
gamesSet.update(exempleSet)
print (gamesSet)

#Remover um item do set
gamesSet.remove(True)
gamesSet.remove(90.50)

#Não possibilita retornar valores via fatiamento ou slice
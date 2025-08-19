gameList = ['Fifa', 'Minecraft', 'The Forest', 'GTA V', 'RDR 2']

#iterando valores de uma lista
for game in gameList:
    print(game)

#Quando a condição for atendida o loop será encerrado
for game in gameList:
    if game == 'Minecraft':
        print(game)
        break

#Quando a condição for atendida o loop vai para proxima iteração
for game in gameList:
    if game == 'Minecraft':
        continue
    print(game)

print('++++++++++++++++++++++++++++++')
# função range:
for i in range (3):
    print(gameList[i])
#Vai do 0 a (x-1)
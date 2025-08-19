gameFifa = {
    'name': 'Fifa 23',
    'yearLaunch': '2022',
    'gamePrice': 90.50,
    'classification': 8.5,
    'genre': ['Esporte', 'Família']
}
print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

#Retornar valor de um dicionário
print(gameFifa['genre']) #ou qualquer outro
print(gameFifa.get('classification'))
print(gameFifa['gamePrice'])

#Retornar a chave
print(f'{gameFifa.keys()} AQUI')

#Valores das chaves
print(gameFifa.values())

#Os dois, obs.: retorno em tupla
print(gameFifa.items())

#adicionar itens no dicionario
gameFifa['players'] = 2
print(gameFifa)
#Atualizar itens
gameFifa.update({'players': 1})

#Remover itens
gameFifa.pop('players')

#Dicionários dentro de dicionários
gameDict = {
    'resident evil 4': {
            'yearLaunch': '2023',
            'classification': 9.8,
            'genre': ['Ação', 'aventura']
    },
    'mario odyssey': {
            'yearLaunch': '2017',
            'classification': 10.0,
            'genre': ['3d', 'aventura']
    },
    'donkey kong country': {
            'yearLaunch': '1995',
            'classification': 9.5,
            'genre': ['plataforma', 'aventura']
    }
}
print(gameDict)

#Buscar informação dentro de um dicionário
print(gameDict['mario odyssey']['genre'])

#Adicionar novo item
gameDict['mario odyssey']['players'] = 1

#excluir um dicionario
del gameDict['resident evil 4']


items = list(gameFifa.items())
for i in range(len(items)):
    key, value = items[i]
    print(f'{i+1}- {key}: {value}')
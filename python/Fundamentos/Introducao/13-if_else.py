name = input('Digite o nome do jogo: ')
yearLaunch = float(input('Qual o ano de lançamento do jogo: '))
classfication = float(input('Qual a nota de classificação do jogo: '))

if classfication > 8.0:
    print(f'O jogo {name} é bom. recomendo o jogo')
elif classfication <= 8 and classfication >= 5:
    print(f'o jogo {name} tem uma classificação média')
else:
    print(f'O jogo {name} não é bem avaliado!!!')

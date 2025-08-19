'''
Gerenciamento de Jogadores e Times

Escreva um programa em python que realize o gerenciamento de jogadores. Ele deve atender aos seguintes requisitos:

Adicionar um time
Remover um time
Listar times
Adicionar jogador em um time
Remover jogador de um time
Listar jogadores de um time
A opção de listar os times deve mostrar o índice, o nome e a quantidade de jogadores do time.
A opção de adicionar um time deve pedir um nome para o time que será cadastrado.
A opção de remover um time deve pedir o índice específico do time que foi cadastrado para fazer a sua exclusão.
A opção de adicionar um jogador em um time deve pedir um índice do time que foi cadastrado e associar com o nome do jogador que será adicionado.
A opção de remover um jogador em um time deve pedir um índice do time que foi cadastrado e utilizar esse índice para remover o jogador que fora cadastrado no time.
A opção de listar os jogadores de um time deve ser informado o índice de um time e listar os jogadores que foram associados a ele.
Este é o exercício de revisão do módulo, então aproveite para utilizar todos os recursos vistos até agora, como os funções, condições, loop, listas, etc
'''
times = {}
def adicionar_time():
    nome_time = input('Digite o nome do time: ')
    if nome_time in times:
        print(f'Time: {nome_time} já existe')
    else:
        times[nome_time] = []
        print(f'Time: {nome_time} adicionado com sucesso.')


def listar_times():
    itens = list(times.items())
    for i in range(len(itens)):
        key, value = itens[i]
        if len(value) > 1:
            print(f'{i+1} - {key}: {len(value)} jogadores')
        else:
            print(f'{i+1} - {key}: {len(value)} jogador')

def remover_time():
    nome_time = input('Digite o nome do time que deseja remover: ')
    if nome_time in times:
        times.pop(nome_time)
        print(f'Time: {nome_time} removido com sucesso!')
    else:
        print(f'Não existe {nome_time} na lista de times')

def adicionar_jogador():
    nome_time = input('Digite o nome do time que deseja adicionar jogador: ')
    if nome_time in times:
        nome_jogador = input('Qual nome do jogador: ')
        times[nome_time].append(nome_jogador)
        print(f'Jogador: {nome_jogador} adicionado ao time: {nome_time}')
    else:
        print(f'Não existe {nome_time} na lista de times')

def remover_jogador():
    nome_time = input('Digite o nome do time que deseja remover jogador: ')
    if nome_time in times:
        nome_jogador = input('Qual nome do jogador: ')
        if nome_jogador in times[nome_time]:
            times[nome_time].remove(nome_jogador)
            print(f'Jogador: {nome_jogador} removido do time: {nome_time}')
        else:
            print(f'Não existe {nome_jogador} na lista de jogadores')    
    else:
        print(f'Não existe {nome_time} na lista de times')

def listar_jogador():
    nome_time = input('Digite o nome do time que deseja listar os jogadores: ')
    if nome_time in times:
        jogadores = times[nome_time]
        print(f'\nJogadores do time {nome_time}:')
        for i, jogador in enumerate(jogadores):
            print(f'{i+1} - {jogador}')
    else:
        print(f'O time "{nome_time}" não foi encontrado.')


def main():
    opcao = int(input(f'Digite a opção que deseja seguir:\n1.Adicionar um time.\n2.Listar os times.\n3.Remover um time.\n4.Adicionar jogador a um time.\n5.Remover jogador de um time.\n6.Listar jogadores de um time\n7.Sair\n'))
    while opcao != 7:
        if opcao == 1:
            adicionar_time()
        elif opcao == 2:
            listar_times()
        elif opcao == 3:
            remover_time()
        elif opcao == 4:
            adicionar_jogador()
        elif opcao == 5:
            remover_jogador()
        elif opcao == 6:
            listar_jogador()
        else:
            opcao = int(input(f'Opção invalida.\nDigite a opção que deseja seguir:\n1.Adicionar um time.\n2.Listar os times.\n3.Remover um time.\n4.Adicionar jogador a um time.\n5.Remover jogador de um time.\n6.Listar jogadores de um time\n7.Sair\n'))
        opcao = int(input(f'Digite a opção que deseja seguir:\n1.Adicionar um time.\n2.Listar os times.\n3.Remover um time.\n4.Adicionar jogador a um time.\n5.Remover jogador de um time.\n6.Listar jogadores de um time\n7.Sair\n'))
    print ('Encerrando programa!')
if __name__ == '__main__':
    main()
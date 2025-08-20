'''
Crie duas funções em python para agendar o desligamento do computador em uma hora e meia hora.
E depois cancelar o desligamento
'''
import os

# Funções de agendamento
def agendar_30min():
    os.system('shutdown /s /t 1800')  # 30 minutos

def agendar_1h30():
    os.system('shutdown /s /t 5400')  # 1 hora e 30 minutos

# Função para cancelar desligamento
def cancelar():
    os.system('shutdown -a')

def main():
    opcao = input(f'Escolha uma opção:\n1 - Agendar desligamento em 30 minutos\n2 - Agendar desligamento em 1 hora e 30 minutos\n3 - Cancelar agendamento de desligamento')

    if opcao == '1':
        agendar_30min()
        print('Desligamento agendado para daqui a 30 minutos.')
    elif opcao == '2':
        agendar_1h30()
        print('Desligamento agendado para daqui a 1 hora e 30 minutos.')
    elif opcao == "3":
        cancelar()
        print('Agendamento de desligamento cancelado.')
    else:
        print('Opção inválida.')

if __name__ == '__main__':
    main()
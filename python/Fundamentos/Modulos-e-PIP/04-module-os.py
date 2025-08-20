import os

'''
COnsulta as funcionalidades do modulo
help('os')
'''

#1 - Retorna o caminho da pasta atual
print(os.getcwd())

#2 - Lista os arquivos da pasta
print(os.listdir())

#3 - Apresenta a versão do sistema operacional
os.system('ver')
'''
OBS.:Podemos executar um comando do terminal dentro da aspas também
exemplo: os.system('dir') #retorna os arquivos da pasta
'''
#3.1 retorna a configuração da máquina
os.system('systeminfo')
#3.2 limpar o terminal
os.system('cls')
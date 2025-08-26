"""
Avaliação e Média da Nota de Filmes

Desenvolva novas funcionalidades para complementar o nosso gerenciamento da classe Filmes. Segue o escopo das funcionalidades:

Uma das funcionalidades requeridas é que o usuário possa realizar a avaliação de um filme passando uma nota com parâmetro e que essa nota seja salva no atributo específico da classe.

Assim que uma avaliação for realizada, deve ser incrementado o total de avaliadores daquele filme. Obs: Considere criar um atributo específico para esse fim.

Para cada filme ter uma nota de avaliação média que consiste na divisão do total de avaliação pelo total de avaliadores.
"""

class Movie():
    def __init__ (self, name, yearLaunch):
        self.name = name
        self.yearLaunch = yearLaunch
        self.amountNotes = 0
        self.note = []
        self.noteMean = 0

    def technical_sheet (self):
        print(f'###Dados do Filme###\n-Nome do filme: {self.name}\n-Ano de lançamento: {self.yearLaunch}\n-Nota: {self.noteMean}\n\n')
    
    def rate (self, note):
        self.note.append(note)
        self.amountNotes += 1
        self.noteMean = sum(self.note)/self.amountNotes
        
mario = Movie("Super Mario", 2023)
maverick = Movie("Top Gun Maverick", 2022)

maverick.rate(5)
maverick.rate(5)

mario.rate(4)
mario.rate(5)


mario.technical_sheet()
maverick.technical_sheet()
class Movie:
    #Configuração inicial na classe, caso não passe os valores irá da erro
    def __init__(self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
    def __str__(self):
        return f"Filme: {self.name}"
        
mario = Movie("Super Mario Bros", 2023, False, 5.0, 130)

print(f"Nome do filme: {mario.name}\n Ano de lançamento: {mario.yearLaunch}\nIncluso no plano: {mario.includedPlan}\nNota: {mario.note}\nDuração: {mario.durationMinutes}")
class Movie:
    def __init__ (self, name, yearLaunch, includedPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includedPlan
        self.note = note
        self.durationMinutes = durationMinutes
    
    def __str__(self):
        return f"Nome do filme: {self.name}"
    
    def technical_sheet (self):
        print(f'###Dados do Filme###\n-Nome do filme: {self.name}\n-Ano de lançamento: {self.yearLaunch}\n-Nota: {self.note}\n-Duração: {self.durationMinutes}')
        
mario = Movie("Super Mario", 2023, False, 10.0, 120)
maverick = Movie("Top Gun Maverick", 2022, False, 9.0, 140)

mario.technical_sheet()
maverick.technical_sheet()
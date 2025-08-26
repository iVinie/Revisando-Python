class Movie:
    name = ""
    yearLaunch = 0
    includedPlan = False
    note = 0
    durationMinutes = 0

# Primeiro Filme #
mario = Movie()
mario.name = "Super Mario Bros"
mario.yearLaunch = 2023
mario.includedPlan = False
mario.note = 5.0
mario.durationMinutes = 130

print(f"Nome do filme: {mario.name}\n Ano de lançamento: {mario.yearLaunch}\nIncluso no plano: {mario.includedPlan}\nNota: {mario.note}\nDuração: {mario.durationMinutes}")

#Obs.: Com a classe podemos instanciar varios filmes, ela serve de modelo

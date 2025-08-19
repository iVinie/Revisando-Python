def wellcome():
    print("Hello World")

def sum():
    return 5 + 4 #no caso do return, ele só vai retornar o resultado, mas não vai printar

def create_game():
    name = input("Digite o nome do jogo \\n")
    yearLaunch = int(input("Digite o ano de lançamento\\n"))
    gamePrice = float(input("Digite o preço do jogo\\n"))
    noteRating = float(input("Digite a nota de avaliação do jogo\\n"))
    print(name)
    print(yearLaunch)
    print(gamePrice)
    print(noteRating)

#wellcome()
#create_game()


#Funções com argumento
def full_name(fname, lname):
    print(f"{fname} {lname}")

def sum(a, b):
    print(a + b)

def address(country="Brasil"): #por padrão vai Brasil
    print(f"Eu moro no {country}")

full_name("Rodrigo", "Macedo")
sum(20, 10)
#address()
#address("Canadá")

def rating_game(qtdRating):
    game_name = input("Digite o nome do jogo\\n")
    sum = 0
    for i in range(qtdRating):
        note = float(input("Digite a nota para o jogo \\n"))
        sum += note
    print(f"Média de avaliação do jogo {game_name} é: {sum/qtdRating}")

rating = int(input("Digite quantas avaliações deseja fazer no jogo\\n"))
#rating_game(rating)

#Obs.: é de bom tom, deixar as funções todas no inicio do programa ou em pag separada


#Função recursiva
"""
3 -> 3 * 2 * 1
5 -> 5 * 4 * 3 * 2 * 1
"""
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num-1))

number = int(input("Digite o número para fatorial\\n"))
print(f"O fatorial de {number} é: {factorial(number)}")

"""
3 -> 3 + 2 + 1
5 -> 5 + 4 + 3 + 2 + 1
"""

def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + total_sum(num - 1))

num = int(input("Digite um número para soma \\n"))
print(f"A soma total do {num} é: {total_sum(num)}")

#Funções com argumentos especiais

"""
*args: Utilizamos ele quando não temos a certeza de quantos
argumentos vamos ter dentro de uma função. Ao utilizá-lo, 
deixamos essa informação dinâmica e variável.
- Os argumentos são passados como uma tupla.

**kwargs: Além dos valores, podemos passar também as respectivas
chaves para cada argumento.
- Os argumentos são passados como um dicionário.
"""
def sum(*num):
    sum_total = 0
    
    for n in num:
        sum_total = sum_total + n

    print(f"Soma é: {sum_total}")
sum(7)
sum(8, 7)
sum(4, 5, 9)
sum(6, 8, 3, 1)

def presentation(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print("######Curso######")
presentation(name="Python", category="Backend", level="Iniciante")

#Função Lambda

power = lambda num: num ** 2
pair = lambda x: x%2==0
divNum = lambda x,y : x/y
reverse = lambda s: s[::-1]

print(power(5))
print(power(9))
print(pair(27))
print(pair(30))
print(divNum(10,2))
print(divNum(7,2))
print(reverse("Função"))
print(reverse("Tecnologia"))

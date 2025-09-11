"""
with open('primeiro-csv.csv', 'r', encoding='utf-8') as file:
    for line in file:
#        lines = line.rstrip().split(';')
#        print(f'{lines[0]}: {lines[1]}')
        language, category = line.rstrip().split(';')
        print(f'{language}: {category}')
"""

#Lendo e criando um dicionário 
"""courses = []
with open("primeiro-csv.csv", encoding="utf-8") as file:
    for line in file:
        name, category = line.rstrip().split(";")
        course = {}
        course["name"] = name
        course["category"] = category
        courses.append(course)
print(courses)

for course in courses:
    print(f"{course["name"]} -{course["category"]}")"""

#Podemos também usar o módulo CSV
"""import csv
cursos = []
with open('primeiro-csv.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        cursos.append({'language': row["language"], "category": row['category']})
for i in cursos:
    print (i)"""
    
#Escrevendo em CSV
import csv
name = input('Informe o nome da linguagem: ')
category = input('Qual o objetivo dessa linguagem: ')

with open('primeiro-csv.csv', 'a', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';', lineterminator='\n')
    writer.writerow([name, category])
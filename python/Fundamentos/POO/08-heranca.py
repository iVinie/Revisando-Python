class Animal:
    name = ''
    size = ''
    color = ''
    
    def eat(self):
        print('Animal se alimentando')
        
class Horse(Animal):
    race = ''
    def escape(self):
        print('Cavalo fugindo')

class Lion(Animal):
    mane = True
    
    def hunt(self):
        print('Leão caçando')
        
        
        
h = Horse()
h.name = 'Carpeado'
h.color = 'Black'
h.escape()
h.eat()
#h.hunt() #Daria error, por não existir

l = Lion()
l.name = 'Simba'
l.color = 'Marrom'
l.hunt()
l.eat()
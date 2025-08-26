"""
Classe Produto e método desconto

Desenvolva uma classe em Python para atender as seguintes especificidades de um Produto:

Cada produto deve ter um preço e um nome.

A classe deve ter um método construtor e o método dundle str.

A classe deve ter um método para desconto. O método deve receber o desconto em percentual e realizar o cálculo de quanto ficaria o preço final com o desconto.
"""

class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.discount = 0.0
        self.valor = 0
    def __str__(self):
        return f"Nome: {self.name}\nPreço: {self.price}\nDesconto: {self.discount*100}%\n"
    
    def apply_discount(self, percentage):
        self.discount = percentage
        self.valor = self.discount*self.price
        self.price -= self.valor

monitor = Product("Monitor Samsung", 2000)
monitor.apply_discount(0.5)
print(monitor)
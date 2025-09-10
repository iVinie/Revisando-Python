class Product:
    # A variável de classe é compartilhada por todos os objetos
    taxa_cambio = 5.25  

    def __init__(self, name, price_brl):
        self.name = name
        self.price_brl = price_brl

    # Método de classe para criar um produto a partir de um preço em dólar
    @classmethod
    def from_usd(cls, name, price_usd):
        # Acessa a variável de classe 'taxa_cambio'
        price_brl = price_usd * cls.taxa_cambio
        # Retorna uma nova instância da classe usando o construtor padrão
        return cls(name, price_brl)

    def __str__(self):
        return f"Produto: {self.name} | Preço: R$ {self.price_brl:.2f}"


# Criando um produto da forma normal
monitor = Product("Monitor", 1500.00)

# Usando o método de classe para criar um produto de forma alternativa
livro = Product.from_usd("Livro de Python", 20.00)

print(monitor)
print(livro)
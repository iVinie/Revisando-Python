class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Nome: {self.name}\nPreço: {self.price}\n"

    # Método estático para validar se um preço é válido
    @staticmethod
    def is_valid_price(price):
        if price <= 0:
            return False
        return True

# --- Exemplo de uso ---

# Usando o método estático para validar um preço antes de criar um objeto
price_to_check = 100.00
if Product.is_valid_price(price_to_check):
    print(f"O preço {price_to_check} é válido.")
    new_product = Product("Livro", price_to_check)
    print(new_product)
else:
    print(f"O preço {price_to_check} não é válido.")

# Você pode chamar o método diretamente na classe, sem precisar de uma instância
invalid_price = -10.00
if Product.is_valid_price(invalid_price):
    print(f"O preço {invalid_price} é válido.")
else:
    print(f"O preço {invalid_price} não é válido.")
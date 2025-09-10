class Phone:
    def __init__(self, brand, model_name, price):
        self._brand = brand
        self._model_name = model_name
        self._price = price
    
    def __str__(self):
        return f'{self._brand}{self._model_name}'
    
    @staticmethod
    def make_a_call(phone_num):
        print(f'Ligando para: {phone_num}')



class SmartPhone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        super().__init__(brand, model_name, price)
        
        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera

moto = Phone('Moto', 'G7', 1000)
print(moto)

moto.make_a_call(999999999)
print(f'Valor do {moto._brand}{moto._model_name}{moto._price}')


Iphone = SmartPhone('Iphone','13',7000,'4GB','128GB','25MP')
print(Iphone)
Iphone.make_a_call(32142342)
print(f"Valor do {Iphone._brand}{Iphone._model_name} {Iphone._price}")
print(vars(Iphone))
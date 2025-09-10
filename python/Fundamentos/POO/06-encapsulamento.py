class ContaBancaria:
    def __init__(self, saldo_inicial):
        # O saldo é um atributo "privado"
        self.__saldo = saldo_inicial
        
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")
        else:
            print("Valor de saque inválido ou saldo insuficiente.")

    def ver_saldo(self):
        return self.__saldo

# --- Exemplo de uso ---
minha_conta = ContaBancaria(1000)

# Acesso e modificação via métodos (forma correta e segura)
minha_conta.depositar(500)
minha_conta.sacar(200)

print(f"Saldo atual: R$ {minha_conta.ver_saldo():.2f}")

# Tentativa de acessar o saldo diretamente (forma incorreta)
# Isso causaria um erro ou não funcionaria como esperado
# print(minha_conta.__saldo) # Causa um AttributeError
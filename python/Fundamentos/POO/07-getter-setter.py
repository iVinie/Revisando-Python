class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial

    @property  # O Getter
    def saldo(self):
        return self.__saldo

    @saldo.setter  # O Setter
    def saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo
            print("Saldo atualizado com sucesso.")
        else:
            print("Erro: O saldo não pode ser um valor negativo.")

# --- Exemplo de uso ---
minha_conta = ContaBancaria(1000)

# Acessando o saldo como um atributo (o Getter é chamado por trás)
print(f"Saldo inicial: R$ {minha_conta.saldo:.2f}")

# Modificando o saldo como um atributo (o Setter é chamado por trás)
minha_conta.saldo = 1500
print(f"Novo saldo: R$ {minha_conta.saldo:.2f}")
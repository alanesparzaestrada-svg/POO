class BankAccount:

    # Atributo de clase

    bank = "Banco Central"



    def __init__(self, saldo):

        self.saldo = saldo



    # Método de instancia

    def show_balance(self):

        print(f"El saldo del cliente es: ${self.saldo:.2f}")



    # Método de clase

    @classmethod

    def show_bank(cls):

        print(f"El nombre del banco es: {cls.bank}")



    # Método estático

    @staticmethod

    def convert_currency(valor):

        tipo_cambio = 20.0 # Tipo de cambio fijo de ejemplo

        pesos = valor * tipo_cambio

        print(f"${valor} USD equivalen a ${pesos:.2f} pesos.")



# Ejemplo de uso:

cuenta1 = BankAccount(1250.00)

cuenta1.show_balance()



# Llamar al método de clase

BankAccount.show_bank()



# Llamar al método estático

BankAccount.convert_currency(50) 


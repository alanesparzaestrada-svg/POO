class BankAccount: #este es el nombre de la clase en este caso es el molde para crear las cuentas bancarias

    bank = "Central Bank"  #bank es el nombre de la variable de la clase y central bank es el texto que se le asigna a la variable de la clase
    #Es decir:
    #"Todas las cuentas de esta clase pertenecen al banco Central Bank”

    def __init__(self, balance): #metodo constructor se ejecuta cuando se crea un objeto de la clase, ejemplo cuando se crea una cuenta bancaria, el metodo constructor se ejecuta y se le asigna un saldo inicial ala cuenta bancaria
        self.balance = balance  #guarda el valor que recibio y lo guarda en la cuenta bancaria
#balance es el valor que recibe la función cuando creo una cuenta, y self.balance es 
# donde guardo ese valor dentro del objeto. Por ejemplo, si creo una cuenta con 100 dólares, self.balance guarda esos 100 dólares

    def show_balance(self):
        print("Client balance:", self.balance, "dollars")
#Esta función sirve para mostrar el saldo de la cuenta. self representa la cuenta actual y self.balance obtiene el saldo que guardamos 
# cuando creamos la cuenta. Después, print muestra ese saldo en pantalla

    @classmethod
    def show_bank(cls):
        print("Bank:", cls.bank)
#Aquí utilizo @classmethod porque quiero trabajar con información que pertenece a la clase y no a una cuenta específica. 
#cls representa a la clase BankAccount. Entonces cls.bank busca la variable bank que tenemos dentro de la clase, que en este caso tiene el valor Central Bank
#Como no necesito una cuenta específica para saber cuál es el banco, puedo llamar directamente a BankAccount.show_bank()

    @staticmethod
    def convert_currency(value):
        exchange_rate = 18.50
        pesos = value * exchange_rate
        print("Pesos:", pesos)


#Crear una cuenta
account = BankAccount(100)

#Debe mostrar el saldo del cliente
account.show_balance()

#muestra el nombre del barco
BankAccount.show_bank()

#Convertir dólares a pesos
BankAccount.convert_currency(100)
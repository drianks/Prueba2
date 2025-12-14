class Cuenta:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.movimientos = []

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
            self.movimientos.append(f"DEPÓSITO {monto}")
            return True
        return False

    def retirar(self, monto):
        raise NotImplementedError()

    def info(self):
        return f"{self.numero} - {self.titular} -> ${self.saldo}"
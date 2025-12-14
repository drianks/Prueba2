from Vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self, codigo, marca, modelo, año, cc):
        super().__init__(codigo, marca, modelo, año)
        self.cc = cc
#Se define las clases respectiva de la motocicleta.
    def tipo(self):
        return "Moto"

    def consumo(self, km):
        base = km / 30
        if self.cc > 400:
            base *= 1.12
        return round(base, 2)
#Se define el consumo de la motocicleta.
from Automovil import Automovil
from Motocicleta import Motocicleta
from Camion import Camion
from Flota import Flota

def main():
        flota = Flota()
        flota.agregar(Automovil("A1", "BMW", "Alto", 2019, 17))
        flota.agregar(Motocicleta("M1", "Ninja", "H2", 2015, 300))
        flota.agregar(Camion("C1", "Jeep", "Avenger", 2022, 10))

        print("\nVehículos registrados:")
        flota.listar()

        km = 120
        print(f"\nConsumos para {km} km:")
        for v in flota.items:  
            print(f"{v.codigo}: {v.consumo(km)} L")

        print("\nConsumo total:", flota.consumo_total(km), "L")  
if __name__ == "__main__":
    main()

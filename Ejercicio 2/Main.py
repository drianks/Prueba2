from Vendedor import Vendedor
from Gerente import Gerente
from Practicante import Practicante
from Empresa import Empresa

def main():
    empresa = Empresa()
    empresa.agregar(Vendedor("Lilian", "17.871.561-1", 2330000, 12300000, 0.04))
    empresa.agregar(Gerente("Benjamin", "22.472.652-2", 1420000, 4500000))
    empresa.agregar(Practicante("Edgard", "18.263.983-3", 60, 4500))

    print("\nTrabajadores activos:")
    for t in empresa.activos():
        print(t.resumen())

    print("\nGasto total mensual:", empresa.total_sueldos())

if __name__ == "__main__":
    main()
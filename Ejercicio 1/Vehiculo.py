class Vehiculo:
    def __init__(self, codigo, marca, modelo, año):
        self.codigo = codigo
        self.marca = marca
        self.modelo = modelo
        self.año = año
#Se describe el vehiculo con los respectivos requisitos. 
    def descripcion(self):
        return f"{self.codigo} -> {self.marca} {self.modelo} ({self.año})"
# Se define las definiciones de objeto a un codigo de vehiculo.
    def tipo(self):
        return "Vehículo"
    
    def consumo(self, km):
        raise NotImplementedError()
#Se define que puede ser un vehiculo, tambien con su consumo respectivo.
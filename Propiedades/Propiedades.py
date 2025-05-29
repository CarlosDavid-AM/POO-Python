class Persona():
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    
dalto = Persona("Lucas", 20)

nombre = dalto.nombre
print(nombre)

dalto.nombre = "pepe"

nombre = dalto.nombre
print(nombre)
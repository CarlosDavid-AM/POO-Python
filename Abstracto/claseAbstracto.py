from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self._nombre = nombre
        self._edad = edad
        self._sexo = sexo
        self._acticidad = actividad

    @abstractmethod
    def trabajar(self):
        pass

    def presentarse(self):
        print(f"Soy {self._nombre} y tengo {self._edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def trabajar(self):
        print(f"Estoy estudiando {self._acticidad}")

dalto = Estudiante("Lucas", 21, "M", "Programador")

dalto.trabajar()
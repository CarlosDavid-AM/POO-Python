class Persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"{self.nombre} está hablando.")

class Empleado(Persona):
    def __init__(self, trabajo, salario):
        super().__init__(trabajo, salario,)
        self.trabajo = trabajo
        self.salario = salario

robert = Empleado("Robert", 30, "Colombiano")
print(f"Nombre: {robert.nombre}, Edad: {robert.edad}, Nacionalidad: {robert.nacionalidad}")
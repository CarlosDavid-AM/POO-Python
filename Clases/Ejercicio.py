class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"{self.nombre} está estudiando en el grado {self.grado}.")


nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))
grado = input("Ingrese el grado del estudiante: ")

estudiante1 = Estudiante(nombre, edad, grado)
print(f"Nombre: {estudiante1.nombre}, Edad: {estudiante1.edad}, Grado: {estudiante1.grado}")

continua = True
while continua:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
        estudiante1.estudiar()
        continua = False
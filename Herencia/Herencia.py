class Persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def hablar(self):
        print(f"{self.nombre} está hablando.")


class Artista():
    def __init__(self, habilidad):
        self.habilidad = habilidad
    def mostrarHabilidad(self):
        print(f'La habilidad es: {self.habilidad}')

class EmpleadoArtista(Persona, Artista):
    def __init__(self, *args, habilidad, salario, empresa):
        Persona.__init__(self, *args)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa

    def presentarse(self):
        return f'{super().mostrarHabilidad()}'

roberto = EmpleadoArtista('Roberto', 30, 'Española', habilidad='Pintura', salario=3000, empresa='Arte S.A.')

roberto.presentarse()
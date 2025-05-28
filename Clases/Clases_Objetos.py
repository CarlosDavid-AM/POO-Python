class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self, numero):
        print(f'Llamando... al numero {numero}')

    def cortar(self):
        print("Cortando llamada...")

celular1 = Celular("Samsung", "Galaxy S21", "108 MP")
celular2 = Celular("Apple", "iPhone 13", "12 MP")

print(celular1.llamar(123456789))
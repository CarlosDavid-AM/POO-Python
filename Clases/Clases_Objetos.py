class Celular:
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

celular1 = Celular("Samsung", "Galaxy S21", "108 MP")
celular2 = Celular("Apple", "iPhone 13", "12 MP")

print(celular1.modelo)
print(celular2.modelo)
import pickle

# Definir la clase Vehículo
class Vehículo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return f"Vehículo: {self.marca} {self.modelo}"

# Crear un objeto de la clase Vehículo
vehiculo = Vehículo("Toyota", "Corolla")

# Guardar el objeto en un archivo utilizando pickle
with open("vehiculo.pickle", "wb") as archivo:
    pickle.dump(vehiculo, archivo)

# Cargar el objeto desde el archivo
with open("vehiculo.pickle", "rb") as archivo:
    vehiculo_cargado = pickle.load(archivo)

# Imprimir el objeto cargado
print(vehiculo_cargado)

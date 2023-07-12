# Crear archivo.txt y escribir en él dos veces

# Crear el archivo
with open("archivo.txt", "w") as archivo:
    # Escribir en el archivo por primera vez
    archivo.write("Este es el primer texto escrito en el archivo.\n")

# Abrir el archivo en modo de adición (append)
with open("archivo.txt", "a") as archivo:
    # Escribir en el archivo por segunda vez
    archivo.write("Este es el segundo texto escrito en el archivo.\n")

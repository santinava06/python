import sqlite3

conexion = sqlite3.connect('alumnos.db')
cursor = conexion.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Alumnos
                  (id INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT)''')
alumnos = [
    (1, 'Juan', 'Pérez'),
    (2, 'María', 'García'),
    (3, 'Pedro', 'López'),
    (4, 'Ana', 'Martínez'),
    (5, 'Carlos', 'Rodríguez'),
    (6, 'Laura', 'Fernández'),
    (7, 'Miguel', 'Torres'),
    (8, 'Sara', 'Gómez')
]
cursor.executemany('INSERT INTO Alumnos VALUES (?, ?, ?)', alumnos)
conexion.commit()
nombre_busqueda = input("Ingresa el nombre del alumno a buscar: ")
cursor.execute('SELECT * FROM Alumnos WHERE nombre = ?', (nombre_busqueda,))
alumno_encontrado = cursor.fetchone()
if alumno_encontrado:
    print("Datos del alumno encontrado:")
    print("ID:", alumno_encontrado[0])
    print("Nombre:", alumno_encontrado[1])
    print("Apellido:", alumno_encontrado[2])
else:
    print("No se encontró ningún alumno con ese nombre.")
conexion.close()

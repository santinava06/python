import tkinter as tk
from tkinter import messagebox

def reiniciar():
    # Reiniciar la selección del RadioButton
    seleccion.set(None)
    # Mostrar un mensaje de reinicio exitoso
    messagebox.showinfo("Reinicio", "La selección ha sido reiniciada con exito.")

def mostrar_seleccion():
    # Obtener la opción seleccionada
    opcion_seleccionada = seleccion.get()
    # Mostrar la opción seleccionada en la consola
    print("Marca Seleccionada:", opcion_seleccionada)

# Crear la ventana
ventana = tk.Tk()

# Variable para almacenar la selección del RadioButton
seleccion = tk.StringVar()

# Crear los botones de opción
rb_opcion1 = tk.Radiobutton(ventana, text="Ferrari", variable=seleccion, value="Ferrari")
rb_opcion1.pack()

rb_opcion2 = tk.Radiobutton(ventana, text="Toyota", variable=seleccion, value="Toyota")
rb_opcion2.pack()

rb_opcion3 = tk.Radiobutton(ventana, text="Mazda", variable=seleccion, value="Mazda")
rb_opcion3.pack()

# Botón de reinicio
boton_reinicio = tk.Button(ventana, text="Reiniciar seleccionado", command=reiniciar)
boton_reinicio.pack()

# Botón para mostrar la selección
boton_mostrar = tk.Button(ventana, text="Mostrar seleccionado", command=mostrar_seleccion)
boton_mostrar.pack()

# Iniciar el bucle de eventos
ventana.mainloop()

import tkinter as tk

def mostrar_seleccion():
    # Obtener el índice del elemento seleccionado
    indice_seleccionado = lista.curselection()
    # Obtener el texto del elemento seleccionado
    texto_seleccionado = lista.get(indice_seleccionado)
    # Actualizar el texto del label con la selección
    label_texto.config(text="Elemento seleccionado: " + texto_seleccionado)

# Crear la ventana
ventana = tk.Tk()

# Crear el label
label_texto = tk.Label(ventana, text="Elemento seleccionado: ")
label_texto.pack()

# Crear la lista de elementos seleccionables
lista = tk.Listbox(ventana)
lista.pack()

# Agregar elementos a la lista
elementos = ["Manzana", "Naranja", "Pera", "Banana"]
for elemento in elementos:
    lista.insert(tk.END, elemento)

# Crear el botón para mostrar la selección
boton_mostrar = tk.Button(ventana, text="Mostrar selección", command=mostrar_seleccion)
boton_mostrar.pack()

# Iniciar el bucle de eventos
ventana.mainloop()

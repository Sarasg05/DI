import tkinter as tk

def mostrar_selecciones():
    seleccion = listbox.curselection()
    elementos = [listbox.get(i) for i in seleccion]
    etiqueta.config(text=f"Seleccionaste: {', '.join(elementos)}")

#Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 6")
root.geometry("300x300")

# Crear una lista de opciones
opciones = ["Manzana","Banana","Naranja"]

# Crear Listbox
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
for opcion in opciones:
    listbox.insert(tk.END, opcion)
listbox.pack(pady=10)

# Botón para mostrar selecciones
boton = tk.Button(root, text="Mostrar selección", command=mostrar_selecciones)
boton.pack(pady=5)

# Etiqueta para mostrar las selecciones
etiqueta = tk.Label(root, text="Seleccionaste: Ninguno")
etiqueta.pack(pady=10)

# Ejecutar el bucle principal
root.mainloop()

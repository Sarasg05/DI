import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 3")
root.geometry("300x200")

def saludar():
    etiqueta.config(text=f"Hola, {entrada.get()}")


#Crear widgets

etiqueta = tk.Label(root, text="Escribe tu nombre: ")
etiqueta.pack(pady=5)

entrada = tk.Entry(root)
entrada.pack(pady=5)

boton = tk.Button(root, text="Saludar", command=saludar)
boton.pack(pady=5)

root.mainloop()

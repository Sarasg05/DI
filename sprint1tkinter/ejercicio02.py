import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 2: Button")
root.geometry("300x200")


def mensaje():
    etiqueta.config(text="Este es el ejercicio 2")

def cerrar():
    root.quit()

# Crear widgets
etiqueta = tk.Label(root, text="")
etiqueta.pack(pady=5)

boton1 = tk.Button(root, text="Mostrar mensaje", command=mensaje)
boton1.pack(pady=5)

boton2 = tk.Button(root, text="Cerrar", command=cerrar)
boton2.pack(pady=5)

# Ejercutar el bucle principal
root.mainloop()

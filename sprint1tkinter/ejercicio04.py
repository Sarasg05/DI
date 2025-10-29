import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 4: Checkbutton")
root.geometry("300x200")

def actualizar():
    seleccionadas = []
    if var_leer.get() == 1:
        seleccionadas.append("Leer")
    if var_deporte.get() == 1:
        seleccionadas.append("Deporte")
    if var_musica.get() == 1:
        seleccionadas.append("Música")

    if seleccionadas:
        etiqueta.config(text="Aficiones: " + ", ".join(seleccionadas))
    else:
        etiqueta.config(text="No has seleccionado ninguna afición")

# Crear variables para los Checkbutton
var_leer = tk.IntVar()
var_deporte = tk.IntVar()
var_musica = tk.IntVar()

# Crear Checkbutton
check_leer = tk.Checkbutton(root, text="Leer", variable=var_leer, command=actualizar)
check_leer.pack(pady=5)

check_deporte = tk.Checkbutton(root, text="Deporte", variable=var_deporte, command=actualizar)
check_deporte.pack(pady=5)

check_musica = tk.Checkbutton(root, text="Música", variable=var_musica, command=actualizar)
check_musica.pack(pady=5)

# Etiqueta para mostrar el estado
etiqueta = tk.Label(root, text="No has seleccionado ninguna afición")
etiqueta.pack(pady=10)

# Ejecutar el bucle principal
root.mainloop()


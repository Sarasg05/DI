import tkinter as tk

def cambiar_color():
    seleccion = color_var.get()
    root.config(bg=color_var.get())
    etiqueta.config(text=f"Seleccionaste: {seleccion.capitalize()}")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 5: Radiobutton")
root.geometry("300x200")

# Crear una variable para los Radiobuttons
color_var = tk.StringVar()
color_var.set("white")   # Color por defecto

#Crear Radiobuttons
rb_rojo = tk.Radiobutton(root, text="Rojo",
                        variable=color_var, value="red",
                        command=cambiar_color)
rb_rojo.pack(pady=5)

rb_verde = tk.Radiobutton(root, text="Verde",
                        variable=color_var, value="green",
                        command=cambiar_color)
rb_verde.pack(pady=5)

rb_azul = tk.Radiobutton(root, text="Azul",
                        variable=color_var, value="blue",
                        command=cambiar_color)
rb_azul.pack(pady=5)

# Etiqueta para mostrar la selección
etiqueta = tk.Label(root, text="Seleccionaste: Ninguno")
etiqueta.pack(pady=10)

# Ejecutar el bucle principal
root.mainloop()
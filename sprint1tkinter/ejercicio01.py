import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 1: Label")
root.geometry("300x200")  # tamaño de la ventana

# Primera etiqueta: mensaje de bienvenida
label_bienvenida = tk.Label(root, text="¡Bienvenida a mi programa!", font=("Arial", 12))
label_bienvenida.pack(pady=10)

# Segunda etiqueta: nombre completo
label_nombre = tk.Label(root, text="Sara Silva González", font=("Arial", 12, "bold"))
label_nombre.pack(pady=10)

# Tercera etiqueta: texto que cambiará
label_cambio = tk.Label(root, text="Texto original", font=("Arial", 12))
label_cambio.pack(pady=10)

# Función que cambiará el texto de la tercera etiqueta
def cambiar_texto():
    label_cambio.config(text="¡El texto ha cambiado!")

# Botón que llama a la función anterior
boton = tk.Button(root, text="Cambiar texto", command=cambiar_texto)
boton.pack(pady=10)

# Mantener la ventana abierta
root.mainloop()



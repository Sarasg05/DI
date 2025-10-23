import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejercicio 1 - Labels en Tkinter")
ventana.geometry("300x200")  # tamaño de la ventana

# Primera etiqueta: mensaje de bienvenida
label_bienvenida = tk.Label(ventana, text="¡Bienvenida a mi programa!", font=("Arial", 12))
label_bienvenida.pack(pady=10)

# Segunda etiqueta: nombre completo
label_nombre = tk.Label(ventana, text="Sara Silva González", font=("Arial", 12, "bold"))
label_nombre.pack(pady=10)

# Tercera etiqueta: texto que cambiará
label_cambio = tk.Label(ventana, text="Texto original", font=("Arial", 12))
label_cambio.pack(pady=10)

# Función que cambiará el texto de la tercera etiqueta
def cambiar_texto():
    label_cambio.config(text="¡El texto ha cambiado!")

# Botón que llama a la función anterior
boton = tk.Button(ventana, text="Cambiar texto", command=cambiar_texto)
boton.pack(pady=10)

# Mantener la ventana abierta
ventana.mainloop()



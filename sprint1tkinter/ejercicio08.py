import tkinter as tk

def mostrar_texto():
    texto = entrada.get()
    etiqueta_mensaje.config(text=texto)

def borrar_texto():
    entrada.delete(0, tk.END)
    etiqueta_mensaje.config(text="")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 8: Frame")
root.geometry("300x200")

# Crear dos frame
frame_superior = tk.Frame(root, bg="lightgrey", bd=2, relief="sunken")
frame_superior.pack(padx=20, pady=20, fill="both", expand=True)

frame_inferior = tk.Frame(root, bg="lightgrey", bd=2, relief="sunken")
frame_inferior.pack(padx=20, pady=20, fill="both", expand=True)

# Widgets del frame superior
etiqueta1 = tk.Label(frame_superior, text="Escribir:", bg="lightgrey")
etiqueta1.grid(row=0, column=0, padx=5, pady=5)

etiqueta2 = tk.Label(frame_superior, text="Resultado:", bg="lightgrey")
etiqueta2.grid(row=1, column=0, padx=5, pady=5)

entrada = tk.Entry(frame_superior)
entrada.grid(row=0, column=1, padx=5, pady=5)

# Widgets del frame inferior
boton_mostrar = tk.Button(frame_inferior, text="Mostrar", bg="lightgrey", command=mostrar_texto)
boton_mostrar.grid(row=0, column=0, padx=10, pady=10)

boton_borrar = tk.Button(frame_inferior, text="Borrar", bg="lightgrey", command=borrar_texto)
boton_borrar.grid(row=0, column=1, padx=10, pady=10)

etiqueta_mensaje = tk.Label(frame_superior, text="", bg="lightgrey", fg="blue")
etiqueta_mensaje.grid(row=1, column=0, columnspan=2, pady=5)

# Ejecutar el bucle principal
root.mainloop()


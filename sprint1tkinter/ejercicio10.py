import tkinter as tk

def insertar_texto():
    for i in range(1, 101):
        cuadro_texto.insert(tk.END, f"Línea {i}\n")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 10: Scrollbar")
root.geometry("300x300")

# Crear un Frame para contener el Text y las Scrollbars
frame = tk.Frame(root)
frame.pack(fill='both', expand=True)

# Crear el Text
cuadro_texto= tk.Text(frame, wrap='none')
cuadro_texto.grid(row=0, column=0, sticky='nsew')

# Crear Scrollbar vertical
scroll_vert = tk.Scrollbar(frame, orient='vertical', command=cuadro_texto.yview)
scroll_vert.grid(row=0, column=1, sticky='ns')
cuadro_texto.config(yscrollcommand=scroll_vert.set)

# Ajustar el tamaño del Frame y el Text al tamaño de la ventana
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

insertar_texto()

# Ejecutar el bucle principal
root.mainloop()
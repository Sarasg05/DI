import tkinter as tk

# Función para dibujar el rectángulo
def dibujar_rectangulo():
    try:
        x1 = int(entry_x1.get())
        y1 = int(entry_y1.get())
        x2 = int(entry_x2.get())
        y2 = int(entry_y2.get())
        canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
    except ValueError:
        etiqueta_error.config(text="Introduce números válidos")

# Función para dibujar el círculo
def dibujar_circulo():
    try:
        x = int(entry_cx.get())
        y = int(entry_cy.get())
        r = int(entry_radio.get())
        canvas.create_oval(x - r, y - r, x + r, y + r, fill="red")
    except ValueError:
        etiqueta_error.config(text="Introduce números válidos")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 7: Canvas")
root.geometry("400x500")

# Crear Canvas
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack(pady=20)

# Entradas para el rectángulo
frame_rect = tk.Frame(root)
frame_rect.pack(pady=5)
tk.Label(frame_rect, text="Rectángulo x1:").grid(row=0, column=0)
entry_x1 = tk.Entry(frame_rect, width=5)
entry_x1.grid(row=0, column=1)
tk.Label(frame_rect, text="y1:").grid(row=0, column=2)
entry_y1 = tk.Entry(frame_rect, width=5)
entry_y1.grid(row=0, column=3)
tk.Label(frame_rect, text="x2:").grid(row=1, column=0)
entry_x2 = tk.Entry(frame_rect, width=5)
entry_x2.grid(row=1, column=1)
tk.Label(frame_rect, text="y2:").grid(row=1, column=2)
entry_y2 = tk.Entry(frame_rect, width=5)
entry_y2.grid(row=1, column=3)
tk.Button(frame_rect, text="Dibujar Rectángulo", command=dibujar_rectangulo).grid(row=2, column=0, columnspan=4, pady=5)

# Entradas para el círculo
frame_circ = tk.Frame(root)
frame_circ.pack(pady=5)
tk.Label(frame_circ, text="Círculo centro x:").grid(row=0, column=0)
entry_cx = tk.Entry(frame_circ, width=5)
entry_cx.grid(row=0, column=1)
tk.Label(frame_circ, text="y:").grid(row=0, column=2)
entry_cy = tk.Entry(frame_circ, width=5)
entry_cy.grid(row=0, column=3)
tk.Label(frame_circ, text="Radio:").grid(row=1, column=0)
entry_radio = tk.Entry(frame_circ, width=5)
entry_radio.grid(row=1, column=1)
tk.Button(frame_circ, text="Dibujar Círculo", command=dibujar_circulo).grid(row=2, column=0, columnspan=4, pady=5)

# Etiqueta para errores
etiqueta_error = tk.Label(root, text="", fg="red")
etiqueta_error.pack()

# Ejecutar el bucle principal
root.mainloop()

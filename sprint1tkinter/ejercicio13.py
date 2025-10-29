import tkinter as tk

def dibujar_circulo(event):
    x, y = event.x, event.y
    radio = 20  # Radio del círculo
    canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill="blue")

def limpiar_canvas(event):
    canvas.delete("all")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 13: Eventos de teclado y ratón (nuevo)")
root.geometry("400x400")

# Canvas
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

canvas.bind("<Button-1>", dibujar_circulo)  # Click izquierdo del ratón
root.bind("c", limpiar_canvas)              # Presionar tecla "c"

# Ejecutar el bucle principal
root.mainloop()
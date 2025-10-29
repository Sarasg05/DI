import tkinter as tk
from tkinter import messagebox

def nueva_ventana():
    messagebox.showinfo("Abrir","Abrir archivo")

def salir_aplicacion():
    root.quit()

def mostrar_ayuda():
    messagebox.showinfo("Acerca de", "Esta es una aplicacion para el ejercicio 9.")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 9: Menu")
root.geometry("300x200")

# Crear la barra de menú
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

# Crear un submenú "Archivo"
menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir", command=nueva_ventana)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=salir_aplicacion)

# Crear un submenú "Ayuda"
menu_ayuda = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Ayuda", menu=menu_ayuda)
menu_ayuda.add_command(label="Acerca de", command=mostrar_ayuda)

# Ejecutar el bucle principal
root.mainloop()

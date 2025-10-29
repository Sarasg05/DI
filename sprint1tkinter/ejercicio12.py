import tkinter as tk
from tkinter import messagebox

def añadir_usuario():
    nombre = entry_nombre.get().strip()
    edad = scale_edad.get()
    genero = var_genero.get()

    if not nombre:
        messagebox.showwarning("Aviso", "El nombre no puede estar vacío.")
        return

    usuario = f"{nombre} - {edad} años - {genero}"
    listbox_usuarios.insert(tk.END, usuario)

    # Limpiar campo de nombre y restablecer valores por defecto
    entry_nombre.delete(0, tk.END)
    scale_edad.set(0)
    var_genero.set("Masculino")


def eliminar_usuario():
    seleccion = listbox_usuarios.curselection()
    if not seleccion:
        messagebox.showwarning("Aviso", "Selecciona un usuario para eliminar.")
        return
    listbox_usuarios.delete(seleccion)


def guardar_lista():
    messagebox.showinfo("Guardar Lista", "Función de guardar lista aún no implementada.")


def cargar_lista():
    messagebox.showinfo("Cargar Lista", "Función de cargar lista aún no implementada.")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 11: Scale")
root.geometry("450x500")

# Menú
menu_principal = tk.Menu(root)
root.config(menu=menu_principal)

menu_archivo = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Guardar Lista", command=guardar_lista)
menu_archivo.add_command(label="Cargar Lista", command=cargar_lista)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)

# Widgets

# Nombre
tk.Label(root, text="Nombre:").pack(anchor="w", padx=10, pady=5)
entry_nombre = tk.Entry(root, width=30)
entry_nombre.pack(anchor="w", padx=10)

# Edad (Scale)
tk.Label(root, text="Edad:").pack(anchor="w", padx=10, pady=5)
scale_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
scale_edad.pack(anchor="w", padx=10)

# Género (Radiobutton)
tk.Label(root, text="Género:").pack(anchor="w", padx=10, pady=5)
var_genero = tk.StringVar(value="Masculino")
frame_genero = tk.Frame(root)
frame_genero.pack(anchor="w", padx=10)
tk.Radiobutton(frame_genero, text="Masculino", variable=var_genero, value="Masculino").pack(side="left")
tk.Radiobutton(frame_genero, text="Femenino", variable=var_genero, value="Femenino").pack(side="left")
tk.Radiobutton(frame_genero, text="Otro", variable=var_genero, value="Otro").pack(side="left")

# Botón Añadir
tk.Button(root, text="Añadir", command=añadir_usuario, bg="lightgreen").pack(pady=10)

# Listbox con Scrollbar
frame_listbox = tk.Frame(root)
frame_listbox.pack(fill="both", expand=True, padx=10, pady=10)

listbox_usuarios = tk.Listbox(frame_listbox)
listbox_usuarios.pack(side="left", fill="both", expand=True)

scroll_vert = tk.Scrollbar(frame_listbox, orient="vertical", command=listbox_usuarios.yview)
scroll_vert.pack(side="right", fill="y")

listbox_usuarios.config(yscrollcommand=scroll_vert.set)

# Botones Eliminar y Salir
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

tk.Button(frame_botones, text="Eliminar", command=eliminar_usuario, bg="salmon").pack(side="left", padx=5)
tk.Button(frame_botones, text="Salir", command=root.quit, bg="lightgray").pack(side="left", padx=5)

# Ejecutar el bucle principal
root.mainloop()
import tkinter as tk
from tkinter import messagebox

class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Usuarios")
        self.root.geometry("450x500")

        # Menú
        menu_principal = tk.Menu(root)
        root.config(menu=menu_principal)

        menu_archivo = tk.Menu(menu_principal, tearoff=0)
        menu_principal.add_cascade(label="Archivo", menu=menu_archivo)
        menu_archivo.add_command(label="Guardar Lista", command=self.guardar_lista)
        menu_archivo.add_command(label="Cargar Lista", command=self.cargar_lista)
        menu_archivo.add_separator()
        menu_archivo.add_command(label="Salir", command=self.salir)

        # Widgets

        # Nombre
        tk.Label(root, text="Nombre:").pack(anchor="w", padx=10, pady=5)
        self.entry_nombre = tk.Entry(root, width=30)
        self.entry_nombre.pack(anchor="w", padx=10)

        # Edad (Scale)
        tk.Label(root, text="Edad:").pack(anchor="w", padx=10, pady=5)
        self.scale_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
        self.scale_edad.pack(anchor="w", padx=10)

        # Género (Radiobutton)
        tk.Label(root, text="Género:").pack(anchor="w", padx=10, pady=5)
        self.var_genero = tk.StringVar(value="Masculino")
        frame_genero = tk.Frame(root)
        frame_genero.pack(anchor="w", padx=10)
        tk.Radiobutton(frame_genero, text="Masculino", variable=self.var_genero, value="Masculino").pack(side="left")
        tk.Radiobutton(frame_genero, text="Femenino", variable=self.var_genero, value="Femenino").pack(side="left")
        tk.Radiobutton(frame_genero, text="Otro", variable=self.var_genero, value="Otro").pack(side="left")

        # Botón Añadir
        tk.Button(root, text="Añadir", command=self.añadir_usuario, bg="lightgreen").pack(pady=10)

        # Listbox con Scrollbar
        frame_listbox = tk.Frame(root)
        frame_listbox.pack(fill="both", expand=True, padx=10, pady=10)

        self.listbox_usuarios = tk.Listbox(frame_listbox)
        self.listbox_usuarios.pack(side="left", fill="both", expand=True)

        scroll_vert = tk.Scrollbar(frame_listbox, orient="vertical", command=self.listbox_usuarios.yview)
        scroll_vert.pack(side="right", fill="y")

        self.listbox_usuarios.config(yscrollcommand=scroll_vert.set)

        # Botones Eliminar y Salir
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Eliminar", command=self.eliminar_usuario, bg="salmon").pack(side="left", padx=5)
        tk.Button(frame_botones, text="Salir", command=self.salir, bg="lightgray").pack(side="left", padx=5)

    # Métodos
    def añadir_usuario(self):
        nombre = self.entry_nombre.get().strip()
        edad = self.scale_edad.get()
        genero = self.var_genero.get()

        if not nombre:
            messagebox.showwarning("Aviso", "El nombre no puede estar vacío.")
            return

        usuario = f"{nombre} - {edad} años - {genero}"
        self.listbox_usuarios.insert(tk.END, usuario)

        # Limpiar campo de nombre y restablecer valores por defecto
        self.entry_nombre.delete(0, tk.END)
        self.scale_edad.set(0)
        self.var_genero.set("Masculino")

    def eliminar_usuario(self):
        seleccion = self.listbox_usuarios.curselection()
        if not seleccion:
            messagebox.showwarning("Aviso", "Selecciona un usuario para eliminar.")
            return
        self.listbox_usuarios.delete(seleccion)

    def guardar_lista(self):
        messagebox.showinfo("Guardar Lista", "Función de guardar lista aún no implementada.")

    def cargar_lista(self):
        messagebox.showinfo("Cargar Lista", "Función de cargar lista aún no implementada.")

    def salir(self):
        self.root.quit()

# Crear la instancia
root = tk.Tk()
app = RegistroApp(root)
root.mainloop()
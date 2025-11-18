import customtkinter as ctk
import tkinter

class MainView:
    def __init__(self, master):
        self.master = master

        # --- Barra de menú ---
        self.menubar = tkinter.Menu(master)
        master.config(menu=self.menubar)
        self.menu_archivo = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Archivo", menu=self.menu_archivo)

        # --- Layout principal: dos columnas ---
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=2)

        # Recuadro "Usuario"
        self.frame_usuarios = ctk.CTkFrame(master, corner_radius=10)
        self.frame_usuarios.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.frame_usuarios.grid_rowconfigure(1, weight=1)

        self.label_usuarios = ctk.CTkLabel(self.frame_usuarios, text="Usuario", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_usuarios.grid(row=0, column=0, pady=5)

        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame(self.frame_usuarios)
        self.lista_usuarios_scrollable.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

        self.btn_add_usuario = ctk.CTkButton(self.frame_usuarios, text="Añadir Usuario")
        self.btn_add_usuario.grid(row=2, column=0, pady=5)

        # Recuadro "Detalles del usuario"
        self.frame_detalles = ctk.CTkFrame(master, corner_radius=10)
        self.frame_detalles.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.frame_detalles.grid_rowconfigure(4, weight=1)

        self.label_detalles_titulo = ctk.CTkLabel(self.frame_detalles, text="Detalles del Usuario", font=ctk.CTkFont(size=16, weight="bold"))
        self.label_detalles_titulo.grid(row=0, column=0, pady=5)

        self.label_nombre = ctk.CTkLabel(self.frame_detalles, text="Nombre: ")
        self.label_nombre.grid(row=1, column=0, sticky="w", padx=5, pady=2)

        self.label_edad = ctk.CTkLabel(self.frame_detalles, text="Edad: ")
        self.label_edad.grid(row=2, column=0, sticky="w", padx=5, pady=2)

        self.label_genero = ctk.CTkLabel(self.frame_detalles, text="Género: ")
        self.label_genero.grid(row=3, column=0, sticky="w", padx=5, pady=2)

        self.avatar_label = ctk.CTkLabel(self.frame_detalles, text="")
        self.avatar_label.grid(row=4, column=0, sticky="n", pady=10)

    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):
        # Limpia lista previa
        for widget in self.lista_usuarios_scrollable.winfo_children():
            widget.destroy()
        for i, usuario in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.lista_usuarios_scrollable,
                text=usuario.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            btn.pack(fill="x", padx=5, pady=2)

    def mostrar_detalles_usuario(self, usuario, avatar_image=None):
        self.label_nombre.configure(text=f"Nombre: {usuario.nombre}")
        self.label_edad.configure(text=f"Edad: {usuario.edad}")
        self.label_genero.configure(text=f"Género: {usuario.genero}")
        if avatar_image:
            self.avatar_label.configure(image=avatar_image, text="")
        else:
            self.avatar_label.configure(image="", text="No hay avatar")



class AddUserView:
    def __init__(self, master, avatar_options):
        self.window = ctk.CTkToplevel(master)
        self.window.title("Añadir Nuevo Usuario")
        self.window.geometry("300x400")
        self.window.grab_set()  # Modal

        ctk.CTkLabel(self.window, text="Nombre:").pack(pady=5)
        self.nombre_entry = ctk.CTkEntry(self.window)
        self.nombre_entry.pack(pady=5)

        ctk.CTkLabel(self.window, text="Edad:").pack(pady=5)
        self.edad_entry = ctk.CTkEntry(self.window)
        self.edad_entry.pack(pady=5)

        ctk.CTkLabel(self.window, text="Género:").pack(pady=5)
        self.genero_entry = ctk.CTkEntry(self.window)
        self.genero_entry.pack(pady=5)

        ctk.CTkLabel(self.window, text="Avatar:").pack(pady=5)
        self.avatar_var = ctk.StringVar(value=avatar_options[0])
        self.avatar_menu = ctk.CTkOptionMenu(self.window, values=avatar_options, variable=self.avatar_var)
        self.avatar_menu.pack(pady=5)

        self.guardar_button = ctk.CTkButton(self.window, text="Guardar")
        self.guardar_button.pack(pady=20)

    def get_data(self):
        return {
            "nombre": self.nombre_entry.get(),
            "edad": self.edad_entry.get(),
            "genero": self.genero_entry.get(),
            "avatar": self.avatar_var.get()
        }

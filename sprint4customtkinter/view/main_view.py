import customtkinter as ctk
from PIL import Image

class MainView(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Registro de Usuarios")
        self.geometry("500x400")

        # Panel izquierdo: lista de usuarios
        self.frame_lista = ctk.CTkFrame(self)
        self.frame_lista.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        self.lista_usuarios = ctk.CTkTextbox(self.frame_lista, width=200)
        self.lista_usuarios.pack(fill="both", expand=True)

        # Panel derecho: previsualización
        self.frame_previsualizacion = ctk.CTkFrame(self)
        self.frame_previsualizacion.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.label_previsualizacion = ctk.CTkLabel(self.frame_previsualizacion, text="Selecciona un usuario")
        self.label_previsualizacion.pack(pady=20)

        # Botones
        self.boton_agregar = ctk.CTkButton(self, text="Añadir")
        self.boton_agregar.pack(side="bottom", pady=10)

        self.boton_eliminar = ctk.CTkButton(self, text="Eliminar")
        self.boton_eliminar.pack(side="bottom", pady=5)


class AltaUsuarioModal(ctk.CTkToplevel):
    def __init__(self, master, on_guardar_callback):
        super().__init__(master)
        self.title("Añadir Usuario")
        self.geometry("300x400")
        self.grab_set()  # Modal
        self.on_guardar = on_guardar_callback

        # Nombre
        ctk.CTkLabel(self, text="Nombre:").pack(pady=5)
        self.entry_nombre = ctk.CTkEntry(self)
        self.entry_nombre.pack(pady=5)

        # Edad
        ctk.CTkLabel(self, text="Edad:").pack(pady=5)
        self.scale_edad = ctk.CTkSlider(self, from_=0, to=100, number_of_steps=100)
        self.scale_edad.pack(pady=5)

        # Género
        ctk.CTkLabel(self, text="Género:").pack(pady=5)
        self.var_genero = ctk.StringVar(value="Masculino")
        frame_genero = ctk.CTkFrame(self)
        frame_genero.pack(pady=5)
        for g in ["Masculino", "Femenino", "Otro"]:
            ctk.CTkRadioButton(frame_genero, text=g, variable=self.var_genero, value=g).pack(anchor="w")

        # Selección de avatar
        ctk.CTkLabel(self, text="Avatar:").pack(pady=5)
        self.avatar_seleccionado = ctk.StringVar()
        frame_avatar = ctk.CTkFrame(self)
        frame_avatar.pack(pady=5)

        self.ctk_images = []  # Guardar referencia
        avatars = ["assets/avatar1.png", "assets/avatar2.png", "assets/avatar3.png"]
        for path in avatars:
            img = ctk.CTkImage(Image.open(path), size=(64, 64))
            self.ctk_images.append(img)
            btn = ctk.CTkButton(frame_avatar, image=img, text="", width=70, height=70,
                                command=lambda p=path: self.seleccionar_avatar(p))
            btn.pack(side="left", padx=5)

        # Botón Guardar
        ctk.CTkButton(self, text="Guardar", command=self.guardar).pack(pady=10)

    def seleccionar_avatar(self, path):
        self.avatar_seleccionado.set(path)

    def guardar(self):
        nombre = self.entry_nombre.get().strip()
        edad = int(self.scale_edad.get())
        genero = self.var_genero.get()
        avatar = self.avatar_seleccionado.get()

        if not nombre:
            ctk.CTkLabel(self, text="Nombre obligatorio", text_color="red").pack()
            return
        if not avatar:
            ctk.CTkLabel(self, text="Selecciona un avatar", text_color="red").pack()
            return

        # Llamar callback del controlador
        self.on_guardar(nombre, edad, genero, avatar)
        self.destroy()
from model.usuario_model import GestorUsuarios, Usuario
from view.main_view import MainView
import customtkinter as ctk
from tkinter import simpledialog

class AppController:
    def __init__(self):
        self.gestor = GestorUsuarios()
        self.vista = MainView()

        # Conectar botones
        self.vista.boton_agregar.configure(command=self.alta_usuario)
        self.vista.boton_eliminar.configure(command=self.eliminar_usuario)

        # Inicializar lista
        self.refrescar_lista()

        self.vista.mainloop()

    def alta_usuario(self):
        nombre = simpledialog.askstring("Nombre", "Ingresa el nombre:")
        if not nombre:
            return
        edad = simpledialog.askinteger("Edad", "Ingresa la edad (0-100):", minvalue=0, maxvalue=100)
        if edad is None:
            return
        genero = simpledialog.askstring("Género", "Ingresa género (masculino/femenino/otro):").lower()
        if genero not in ["masculino", "femenino", "otro"]:
            return

        usuario = Usuario(nombre, edad, genero)
        try:
            self.gestor.añadir(usuario)
            self.refrescar_lista()
        except ValueError as e:
            ctk.CTkMessageBox.show_error("Error", str(e))

    def eliminar_usuario(self):
        # Por simplicidad eliminamos el último de la lista por ahora
        if self.gestor.listar():
            self.gestor.eliminar(len(self.gestor.listar()) - 1)
            self.refrescar_lista()

    def refrescar_lista(self):
        self.vista.lista_usuarios.delete("0.0", "end")
        for u in self.gestor.listar():
            self.vista.lista_usuarios.insert("end", f"{u.nombre} - {u.edad} - {u.genero}\n")

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

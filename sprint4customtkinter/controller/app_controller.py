from view.main_view import MainView, AddUserView
from model.usuario_model import Usuario, GestorUsuarios
from tkinter import messagebox
from pathlib import Path
from PIL import Image, ImageTk

class AppController:
    def __init__(self, master):
        self.master = master
        self.model = GestorUsuarios()
        self.view = MainView(master)

        # Directorio assets y caché de imágenes
        self.BASE_DIR = Path(__file__).resolve().parent.parent
        self.ASSETS_PATH = self.BASE_DIR / "assets"
        self.avatar_images = {}

        # Conectar botón "Añadir usuario"
        self.view.btn_add_usuario.configure(command=self.abrir_ventana_añadir)

        # Cargar datos de ejemplo y refrescar lista
        self.refrescar_lista_usuarios()

    def refrescar_lista_usuarios(self):
        usuarios = self.model.listar()
        self.view.actualizar_lista_usuarios(usuarios, self.seleccionar_usuario)

    def seleccionar_usuario(self, indice):
        usuario = self.model.listar()[indice]
        avatar_image = None
        avatar_path = self.ASSETS_PATH / usuario.avatar
        if avatar_path.exists():
            img = Image.open(avatar_path).resize((100, 100))
            avatar_image = ImageTk.PhotoImage(img)
            self.avatar_images[usuario.nombre] = avatar_image  # Mantener referencia
        self.view.mostrar_detalles_usuario(usuario, avatar_image)

    def abrir_ventana_añadir(self):
        avatar_options = [f.name for f in self.ASSETS_PATH.glob("*.png")]
        self.add_view = AddUserView(self.master, avatar_options)
        self.add_view.guardar_button.configure(command=lambda: self.añadir_usuario(self.add_view))

    def añadir_usuario(self, add_view):
        data = add_view.get_data()
        try:
            edad = int(data["edad"])
        except ValueError:
            messagebox.showerror("Error", "Edad debe ser un número entero")
            return

        nuevo_usuario = Usuario(
            nombre=data["nombre"],
            edad=edad,
            genero=data["genero"],
            avatar=data["avatar"]
        )
        self.model.agregar_usuario(nuevo_usuario)
        self.refrescar_lista_usuarios()
        add_view.window.destroy()

import customtkinter as ctk

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

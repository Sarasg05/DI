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

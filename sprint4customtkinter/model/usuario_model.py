import csv
from pathlib import Path


class Usuario:
    def __init__(self, nombre, edad, genero, avatar=None):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar  # Ruta de la imagen


class GestorUsuarios:
    def __init__(self):
        self._usuarios = []
        self._cargar_datos_de_ejemplo()

    def _cargar_datos_de_ejemplo(self):
        self._usuarios.append(Usuario("Ana", 25, "Femenino", "assets/avatar1.png"))
        self._usuarios.append(Usuario("Luis", 30, "Masculino", "assets/avatar2.png"))
        self._usuarios.append(Usuario("Marta", 22, "Femenino", "assets/avatar3.png"))

    def listar(self):
        return self._usuarios

    def añadir_usuario(self, usuario):
        self._usuarios.append(usuario)

    def eliminar_usuario(self, indice):
        if 0 <= indice < len(self._usuarios):
            self._usuarios.pop(indice)

    def guardar_csv(self, ruta):
        ruta = Path(ruta)
        with open(ruta, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Nombre", "Edad", "Genero", "Avatar"])
            for u in self._usuarios:
                writer.writerow([u.nombre, u.edad, u.genero, u.avatar])

    def cargar_csv(self, ruta):
        ruta = Path(ruta)
        self._usuarios.clear()
        try:
            with open(ruta, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)  # Saltar cabecera
                for fila in reader:
                    try:
                        nombre, edad, genero, avatar = fila
                        self._usuarios.append(Usuario(nombre, int(edad), genero, avatar))
                    except Exception:
                        continue  # Ignora filas corruptas
        except FileNotFoundError:
            pass

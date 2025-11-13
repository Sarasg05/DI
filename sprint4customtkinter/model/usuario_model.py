class Usuario:
    def __init__(self, nombre: str, edad: int, genero: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero

class GestorUsuarios:
    def __init__(self):
        self._usuarios = []

    def listar(self):
        return list(self._usuarios)

    def añadir(self, usuario: Usuario):
        if not usuario.nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not (0 <= usuario.edad <= 100):
            raise ValueError("Edad fuera de rango.")
        if usuario.genero.lower() not in ["masculino", "femenino", "otro"]:
            raise ValueError("Género inválido.")
        self._usuarios.append(usuario)

    def eliminar(self, indice: int):
        if 0 <= indice < len(self._usuarios):
            del self._usuarios[indice]
        else:
            raise IndexError("Índice fuera de rango.")

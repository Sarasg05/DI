import tkinter as tk
from tkinter import PhotoImage, messagebox
import random

opciones = ["Piedra", "Papel", "Tijera"]

# Puntuaciones iniciales
puntuacion_jugador = 0
puntuacion_maquina = 0

def bloquear_botones():
    boton_piedra.config(state="disabled")
    boton_papel.config(state="disabled")
    boton_tijera.config(state="disabled")

def iniciar_partida():
    global puntuacion_jugador, puntuacion_maquina
    puntuacion_jugador = 0
    puntuacion_maquina = 0
    marcador.config(text="Puntuación → Jugador: 0 | Máquina: 0")
    etiqueta.config(text="")
    boton_piedra.config(state="normal")
    boton_papel.config(state="normal")
    boton_tijera.config(state="normal")
    boton_iniciar.config(state="disabled")

def jugar(eleccion_jugador):
    global puntuacion_jugador, puntuacion_maquina

    eleccion_maquina = random.choice(opciones)

    if eleccion_jugador == eleccion_maquina:
        resultado = "Empate"
    elif (eleccion_jugador == "Piedra" and eleccion_maquina == "Tijera") or \
            (eleccion_jugador == "Papel" and eleccion_maquina == "Piedra") or \
            (eleccion_jugador == "Tijera" and eleccion_maquina == "Papel"):
        resultado = f"{eleccion_jugador} gana a {eleccion_maquina}"
        puntuacion_jugador += 1
    else:
        resultado = f"{eleccion_maquina} gana a {eleccion_jugador}"
        puntuacion_maquina += 1

    etiqueta.config(text=f"Tú elegiste: {eleccion_jugador}\n"
                         f"La máquina eligió: {eleccion_maquina}\n"
                         f"Resultado: {resultado}")

    marcador.config(
        text=f"Puntuación → Jugador: {puntuacion_jugador} | Máquina: {puntuacion_maquina}"
    )

    # Verificar si alguien llegó a 3 puntos
    if puntuacion_jugador == 3 or puntuacion_maquina == 3:
        if puntuacion_jugador == 3:
            ganador = "¡Ganaste la partida!"
        else:
            ganador = "La máquina ganó la partida"

        messagebox.showinfo("Fin del juego", ganador)

        bloquear_botones()

def nuevo_juego():
    global puntuacion_jugador, puntuacion_maquina
    puntuacion_jugador = 0
    puntuacion_maquina = 0
    marcador.config(text="Puntuación → Jugador: 0 | Máquina: 0")
    etiqueta.config(text="")
    boton_piedra.config(state="disabled")
    boton_papel.config(state="disabled")
    boton_tijera.config(state="disabled")
    boton_iniciar.config(state="normal")

# Crear la vetana principal
root = tk.Tk()
root.title("Piedra-Papel-Tijera")
root.geometry("500x500")

imagenPiedra = PhotoImage(file="piedra.png")
imagenPapel = PhotoImage(file="papel.png")
imagenTijera = PhotoImage(file="tijera.png")

# Crear frame del jugador1
frame_jugador = tk.Frame(root, bg="lightgrey", bd=2, relief="sunken")
frame_jugador.pack(padx=20, pady=20, fill="both", expand=True)

# Crear los botones
boton_piedra = tk.Button(frame_jugador, image=imagenPiedra, command=lambda: jugar("Piedra"))
boton_piedra.grid(row=0, column=0, padx=5, pady=5)

boton_papel = tk.Button(frame_jugador, image=imagenPapel, command=lambda: jugar("Papel"))
boton_papel.grid(row=0, column=1, padx=5, pady=5)

boton_tijera = tk.Button(frame_jugador, image=imagenTijera, command=lambda: jugar("Tijera"))
boton_tijera.grid(row=0, column=2, padx=5, pady=5)

boton_piedra.config(state="disabled")
boton_papel.config(state="disabled")
boton_tijera.config(state="disabled")

boton_iniciar = tk.Button(root, text="Iniciar partida", command=iniciar_partida)
boton_iniciar.pack(pady=5)


# Etiqueta para mostrar resultado
etiqueta = tk.Label(root, text="", font=("Arial", 14))
etiqueta.pack(pady=10)

# Etiquetas para resultado y puntución
marcador = tk.Label(root, text="Puntuación → Jugador: 0 | Máquina: 0", font=("Arial",12))
marcador.pack(pady=10)

boton_nuevo = tk.Button(root, text="Nuevo juego", command=nuevo_juego)
boton_nuevo.pack(pady=5)

boton_salir = tk.Button(root, text="Salir", command=root.destroy)
boton_salir.pack(pady=5)

# Ejecutar el bucle principal
root.mainloop()


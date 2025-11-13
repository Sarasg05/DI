# Importamos las funciones desde operaciones.py
from operaciones import suma, resta, multiplicacion, division

def pedir_numeros():
    while True:
        try:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            return a, b
        except ValueError:
            print("Por favor ingresa números válidos.")

def calculadora():
    while True:
        a, b = pedir_numeros()

        print("\nSelecciona la operación:")
        print("1 - Suma")
        print("2 - Resta")
        print("3 - Multiplicación")
        print("4 - División")

        opcion = input("Ingresa el número de la operación: ")

        if opcion == "1":
            resultado = suma(a, b)
        elif opcion == "2":
            resultado = resta(a, b)
        elif opcion == "3":
            resultado = multiplicacion(a, b)
        elif opcion == "4":
            resultado = division(a, b)
        else:
            print("Opción inválida.")
            continue

        print(f"Resultado: {resultado}")

        repetir = input("¿Quieres hacer otra operación? (s/n): ").lower()
        if repetir != "s":
            print("¡Gracias por usar la calculadora!")
            break

# Este bloque hace que el programa se ejecute solo si lo corremos directamente
if __name__ == "__main__":
    calculadora()

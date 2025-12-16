"""
Punto de entrada del programa Gestor de Gastos Personales.

Aplica los principios del Zen de Python:
- Simple es mejor que complejo
- Legible es mejor que ilegible
"""

from colorama import Fore, Style, init
from app.gastos import agregar_gasto, listar_gastos, resumen_por_categoria
from app.storage import cargar_gastos

init(autoreset=True)


def mostrar_menu() -> None:
    """Muestra el menú principal del programa."""
    print(Fore.CYAN + "\n--- GESTOR DE GASTOS ---")
    print("1. Agregar gasto")
    print("2. Listar gastos")
    print("3. Resumen por categoría")
    print("4. Salir")


def main() -> None:
    """Función principal del programa."""
    gastos = cargar_gastos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                agregar_gasto(gastos)
            elif opcion == "2":
                listar_gastos(gastos)
            elif opcion == "3":
                resumen_por_categoria(gastos)
            elif opcion == "4":
                print(Fore.GREEN + "Hasta luego 👋")
                break
            else:
                print(Fore.RED + "Opción inválida")
        except Exception as error:
            print(Fore.RED + f"Ocurrió un error: {error}")


if __name__ == "__main__":
    main()

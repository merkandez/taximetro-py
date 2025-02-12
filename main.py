# 📌 Taxímetro Digital en Python - Proyecto Introductorio
TARIFA_MOVIMIENTO = 0.05
TARIFA_PARADO = 0.02

historial_trayectos = []

def mostrar_bienvenida():
    """Muestra mensaje de bienvenida y explica el funcionamiento del taxímetro"""
    print("\n🚕 Bienvenido al Taxímetro digital en py 🚕")
    print("Este programa calcula la tarifa de un trayecto en función del tiempo.")
    print(f"🔹 {TARIFA_PARADO * 100:.0f} céntimos por segundo cuando está detenido. ")
    print(f"🔹 {TARIFA_MOVIMIENTO * 100:.0f} céntimos por segundo cuando está detenido. ")
    print("¡COMENCEMOS!\n")

def calcular_tarifa(segundos, en_movimiento):
    """Calcula la tarifa según el tiempo y el estado del taxi."""
    tarifa = TARIFA_MOVIMIENTO if en_movimiento else TARIFA_PARADO
    return segundos * tarifa


def iniciar_trayecto():
    """Inicia un trayecto y permite al usuario ingresar manualmente el tiempo transcurrido."""
    total = 0
    en_movimiento = False
    print("\n🛑 Trayecto iniciado. Escribe 'm' para moverte, 'p' para pararte, 'f' para finalizar.")

    while True:
        accion = input("Escribe 'm' (moverse), 'p' (parar) o 'f' (finalizar): ").strip().lower()

        if accion in ['m', 'p']:
            try:
                segundos = int(input("⌚ Ingresa el tiempo transcurrido en segundos: "))
                if segundos < 0:
                    print("⛔ El tiempo no puede ser negativo.")
                    continue
            except ValueError:
                print("⛔ Debes ingresar un número entero válido.")
                continue

            total += calcular_tarifa(segundos, en_movimiento)
            en_movimiento (accion == 'm')
            estado= "en movimiento" if en_movimiento else "detenido"
            print(f"🚕 Trayecto en {estado}. Tarifa acumulada: {total:.2f} céntimos.")
        elif accion == 'f':
            print(f"\n🏁 Trayecto finalizado. Tarifa total: {total:.2f} céntimos.")
            historial_trayectos.append(total)
            break
        else:
            print("⛔ Debes escribir 'm' (moverse), 'p' (parar) o 'f' (finalizar).")
def mostrar_historial():
    """Muestra el historial de trayectos finalizados."""
    print("\n📜 Historial de trayectos:")
    if not historial_trayectos:
        print("No hay trayectos registrados aún en el historial.")
    else:
        print("Historial de trayectos:")
        for i, total in enumerate(historial_trayectos, start=1):
            print(f"Trayecto {i}: {total:.2f} céntimos")
        print()
def main():
    """Función principal del programa."""
    mostrar_bienvenida()
    
    while True:
        print("\n📌 Menú Principal:")
        print("1️⃣ Iniciar un nuevo trayecto")
        print("2️⃣ Ver historial de trayectos")
        print("3️⃣ Salir")
        
        opcion = input("Selecciona una opción (1, 2 o 3): ").strip()

        if opcion == "1":
            iniciar_trayecto()
        elif opcion == "2":
            mostrar_historial()
        elif opcion == "3":
            print("\n👋 Gracias por usar el Taxímetro Digital. ¡Hasta la próxima!\n")
            break
        else:
            print("⚠️ Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
            

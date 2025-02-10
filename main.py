def mostrar_bienvenida():
    """Muestra un mensaje de bienvenida y explica el funcionamiento del taxímetro."""
    print("\n🚖 Bienvenido al Taxímetro Digital 🚖")
    print("Este programa calcula la tarifa de un trayecto en función del tiempo.")
    print("🔹 2 céntimos por segundo cuando está detenido.")
    print("🔹 5 céntimos por segundo cuando está en movimiento.")
    print("¡Comencemos!\n")


def iniciar_trayecto():
    """Inicia un trayecto y permite al usuario ingresar manualmente el tiempo transcurrido."""
    total = 0
    en_movimiento = False
    print(
        "Trayecto iniciado. Escribe 'm' para moverte, 'p' para parar, 'f' para finalizar."
    )

    while True:
        accion = (
            input("🚗 Escribe 'm' (moverse), 'p' (parar) o 'f' (finalizar): ")
            .strip()
            .lower()
        )

        if accion in ["m", "p"]:
            try:
                segundos = int(input("⏳ Ingresa el tiempo transcurrido en segundos: "))
                if segundos < 0:
                    print("⚠️ El tiempo no puede ser negativo.")
                    continue
            except ValueError:
                print("⚠️ Debes ingresar un número entero válido.")
                continue

            tarifa = 0.05 if accion == "m" else 0.02
            total += segundos * tarifa
            en_movimiento = accion == "m"

            estado = "en movimiento" if en_movimiento else "detenido"
            print(f"➡️ Taxi {estado}. Total: {total:.2f}€")

        elif accion == "f":
            print(f"\n🔚 Trayecto finalizado. Tarifa total: {total:.2f}€\n")
            break

        else:
            print("⚠️ Opción no válida. Inténtalo de nuevo.")


def main():
    """Función principal del programa."""
    mostrar_bienvenida()

    while True:
        iniciar_trayecto()
        reiniciar = input("¿Deseas iniciar otro trayecto? (s/n): ").strip().lower()
        if reiniciar != "s":
            print("\n👋 Gracias por usar el Taxímetro Digital. ¡Hasta la próxima!\n")
            break


if __name__ == "__main__":
    main()

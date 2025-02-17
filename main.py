# 📌 Taxímetro Digital con Tiempo Automático en Python y funcionalidad de registro de logs, tests e historial de trayectos

import time
import logging  # Importamos logging para registrar eventos en un archivo
import os

# Configuración del sistema de logs
logging.basicConfig(
    filename="taximetro.log",  # Archivo donde se guardarán los logs
    level=logging.INFO,  # Nivel de registro: INFO (guarda eventos clave)
    format="%(asctime)s - %(message)s",  # Formato del mensaje de log
    # filemode="w" # Esto hace que el archivo se sobrescriba en cada ejecución
)

# Archivo donde se guardará el historial de trayectos
HISTORIAL_FILE = "historial.txt"


TARIFA_MOVIMIENTO = 0.05
TARIFA_PARADO = 0.02

historial_trayectos = []


def cargar_historial():
    """Carga el historial de trayectos desde un archivo de texto al iniciar el programa."""
    if os.path.exists(HISTORIAL_FILE):
        with open(HISTORIAL_FILE, "r") as file:
            for linea in file:
                historial_trayectos.append(float(linea.strip()))


def guardar_historial():
    """Guarda el historial de trayectos en un archivo de texto."""
    with open(HISTORIAL_FILE, "w") as file:
        for total in historial_trayectos:
            file.write(f"{total}\n") #file.write(f"{round(total, 2):.2f}\n") para guardarlo solo con 2 decimales y redondeo


def mostrar_bienvenida():
    """Muestra mensaje de bienvenida y explica el funcionamiento del taxímetro"""
    print("\n🚕 Bienvenido al Taxímetro digital en py 🚕")
    print("Este programa calcula la tarifa de un trayecto en función del tiempo.")
    print(f"🔹 {TARIFA_PARADO * 100:.0f} céntimos por segundo cuando está detenido. ")
    print(
        f"🔹 {TARIFA_MOVIMIENTO * 100:.0f} céntimos por segundo cuando está detenido. "
    )
    print("¡COMENCEMOS!\n")


def calcular_tarifa(segundos, en_movimiento):
    """Calcula la tarifa según el tiempo y el estado del taxi."""
    tarifa = TARIFA_MOVIMIENTO if en_movimiento else TARIFA_PARADO
    return segundos * tarifa


def formato_moneda(total):
    """Formatea el total para mostrarlo en céntimos si es menor de 1 euro, o en euros si es 1 o más."""
    if total < 1:
        return f"{total * 100:.0f} céntimos"
    else:
        return f"{total:.2f}€"


def iniciar_trayecto():
    """Inicia un trayecto y permite al usuario ingresar manualmente el tiempo transcurrido."""
    total = 0
    logging.info("🚕 Trayecto iniciado.")  # 📌 Se registra el inicio del trayecto
    en_movimiento = False
    print(
        "\n🛑 Trayecto iniciado. Escribe 'm' para moverte, 'p' para pararte, 'f' para finalizar."
    )

    tiempo_inicio = time.time()

    while True:
        accion = (
            input("Escribe 'm' (moverse), 'p' (parar) o 'f' (finalizar): ")
            .strip()
            .lower()
        )

        tiempo_actual = time.time()
        segundos = tiempo_actual - tiempo_inicio

        if accion in ["m", "p"]:

            total += calcular_tarifa(segundos, en_movimiento)
            en_movimiento = accion == "m"
            estado = "en movimiento" if en_movimiento else "detenido"

            logging.info(
                f"➡️ Cambio de estado: {estado} ({segundos:.2f} segundos) - Tarifa acumulada: {total:.2f}€"
            )
            print(f"🚕 Trayecto {estado}. Tarifa acumulada: {formato_moneda(total)}.")

            tiempo_inicio = time.time()

        elif accion == "f":

            print(f"\n🏁 Trayecto finalizado. Tarifa total: {formato_moneda(total)}.")
            historial_trayectos.append(total)
            guardar_historial()
            logging.info(
                f"🏁 Trayecto finalizado. Tarifa total: {total:.2f}€"
            )  # 📌 Se registra la tarifa final en el log
            break
        else:
            print("⛔ Debes escribir 'm' (moverse), 'p' (parar) o 'f' (finalizar).")


def mostrar_historial():
    """Muestra el historial de trayectos finalizados."""
    print("\n📜 Historial de trayectos:")
    if not historial_trayectos:
        print("No hay trayectos registrados aún en el historial.")
        logging.info("ℹ️ Historial consultado: No hay trayectos registrados.")
    else:
        print("Historial de trayectos:")
        for i, total in enumerate(historial_trayectos, start=1):
            print(f"Trayecto {i}: {formato_moneda(total)}.")
            logging.info(
                f"ℹ️ Historial consultado: {len(historial_trayectos)} trayectos registrados."
            )


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

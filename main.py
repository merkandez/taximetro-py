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
                    print("⛔El tiempo no puede ser negativo.")
                    continue
            except ValueError:
                print("⛔ Debes ingresar un número entero válido.")
                

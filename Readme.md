# 🚖 Taxímetro Digital en Python

Este proyecto es una evolución didáctica de un taxímetro digital en Python. A lo largo de varias ramas, hemos ido agregando nuevas funcionalidades paso a paso para aprender conceptos clave del lenguaje.

Esta `main` contiene la versión más básica del código, pero puedes explorar las versiones más avanzadas en diferentes ramas.

---

## 🏗 1. Estructura del Proyecto

Este proyecto está organizado en **múltiples ramas**, cada una representando una etapa de aprendizaje y evolución del código.

| 🌱 **Versión**       | 📌 **Rama**                | 🔍 **Características**  |
|----------------------|--------------------------|-------------------------|
| **Taxímetro básico** | `main`                   | Cálculo manual de tarifas, sin almacenamiento ni automatización. |
| **Automatización con `time`** | `feature-time-uv` | Se implementa `time` para medir el tiempo en movimiento y detenerse automáticamente. |
| **Nivel intermedio** | `feature-nivel-medio`    | Logs, tests unitarios e historial de trayectos en un archivo de texto. |

---

## 📌 2. ¿Cómo Explorar la Evolución del Proyecto?

Si has clonado este repositorio y quieres ver cómo evolucionó el código, puedes cambiar entre ramas con:

```sh
git checkout feature-time-uv  # Ir a la versión con time
git checkout feature-nivel-medio  # Ir a la versión con logs, tests e historial
```

Para ver todas las ramas disponibles:

```sh
git branch -a
```

---

## 🛠 3. Código de la Versión `main`

Esta versión es la más básica y permite calcular tarifas de taxi de manera manual.

### 📌 Funciones Principales

1️⃣ **`mostrar_bienvenida()`** → Muestra un mensaje explicativo.  
2️⃣ **`iniciar_trayecto()`** → Calcula la tarifa de un trayecto según el tiempo ingresado.  
3️⃣ **`main()`** → Controla el flujo del programa.  

### 📜 Código de `main.py`

```python
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

```

---

## 🎓 4. ¿Cómo Continuar con el Aprendizaje?

Para seguir aprendiendo y entender cómo mejorar este código, revisa las siguientes ramas:

1️⃣ `feature-time-uv` → **Automatización con `time`**  
   - Se sustituye el ingreso manual de segundos por una medición automática del tiempo transcurrido.  
   - Permite calcular la tarifa sin intervención del usuario.

2️⃣ `feature-nivel-medio` → **Logs, tests e historial de trayectos**  
   - Se registra información en un archivo de logs.  
   - Se implementan tests unitarios para validar cálculos.  
   - Se guarda el historial de trayectos en un archivo de texto.

Puedes revisar cada rama con:

```sh
git checkout feature-time-uv
```

Y ejecutar el código normalmente con:

```sh
python main.py
```

---

## 🚀 5. Mejoras Futuras

Este proyecto tiene mucho potencial de evolución. Algunas mejoras futuras podrían incluir:

✅ **Configuración de tarifas dinámicas** → Ajustar precios en función de la demanda.  
✅ **Interfaz gráfica (GUI)** → Hacerlo más visual e interactivo.  
✅ **Integración con GPS** → Calcular distancias en lugar de depender solo del tiempo.  

---

## 💡 Conclusión

Este proyecto es una guía didáctica para aprender Python de manera progresiva. Hemos estructurado el código en ramas para reflejar la evolución de un programa real, permitiendo explorar mejoras paso a paso.  

🔹 **Empieza desde `main`, explora las ramas y mejora el código a tu propio ritmo.**  
🔹 **Si tienes dudas, revisa el README de cada rama para entender los cambios.**  

👨‍💻 ¡Feliz aprendizaje y programación! 🚀


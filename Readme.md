# 🚕 Taxímetro Digital con Tiempo Automático en Python  

## 📌 Descripción  
Este proyecto es una versión mejorada de nuestro taxímetro digital, ahora con **medición automática del tiempo** usando la librería estándar `time` en Python.  
En versiones anteriores, el usuario debía ingresar manualmente el tiempo transcurrido, pero ahora el programa mide **de manera precisa el tiempo real** en cada estado (movimiento o detenido), simulando mejor un taxímetro real.  

---

## 🔄 **Cambios Introducidos**
1️⃣ **Se eliminó la entrada manual de segundos** → Antes, el usuario tenía que escribir cuántos segundos pasaban en cada estado.  
2️⃣ **Se implementó `time.time()` para medir el tiempo real** → Ahora, el programa **captura automáticamente** el tiempo cuando el taxi está en movimiento o detenido.  
3️⃣ **Se mejoró la precisión del cálculo de tarifas** → Ya no depende de la entrada del usuario, sino del tiempo exacto transcurrido.  
4️⃣ **El programa es más intuitivo** → Solo hay que indicar si el taxi está **en movimiento o detenido**, y el sistema calculará la tarifa sin intervención manual.  

---

## 🛠 **Explicación del Código y de los Cambios**
### 🔹 **1. Importación de la Librería `time`**
```python
import time
```
`time` es una librería estándar de Python que permite medir el tiempo en segundos desde el **1 de enero de 1970** (timestamp).  

🔹 **En este proyecto, usamos `time.time()` para capturar el tiempo en cada cambio de estado.**  

---

### 🔹 **2. Eliminación de la Entrada Manual de Segundos**
📌 **Antes (Método Manual)**  
```python
segundos = int(input("⌚ Ingresa el tiempo transcurrido en segundos: "))
```
🚨 **Problema**: El usuario tenía que escribir el tiempo transcurrido, lo que no era realista ni preciso.

📌 **Ahora (Método Automático con `time`)**  
```python
tiempo_actual = time.time()
segundos = tiempo_actual - tiempo_inicio
```
✅ **Solución**:  
- `time.time()` **captura automáticamente** el tiempo en segundos.  
- `segundos = tiempo_actual - tiempo_inicio` calcula el tiempo transcurrido.  
- **El usuario ya no tiene que ingresar nada manualmente.**  

---

### 🔹 **3. Cálculo Automático del Tiempo y Tarifa**
📌 **Antes**:
```python
total += calcular_tarifa(segundos, en_movimiento)
```
Aquí, `segundos` era un número ingresado manualmente por el usuario.  

📌 **Ahora**:
```python
total += calcular_tarifa(segundos, en_movimiento)
tiempo_inicio = time.time()  # Reinicia el temporizador después de cada acción
```
✅ **Diferencia**:
- **Ahora `segundos` se calcula en base al tiempo real**.
- **Cada vez que el usuario cambia de estado (`m` o `p`), el temporizador se reinicia**.

---

### 🔹 **4. Mejor Gestión del Formato de Moneda**
📌 **Antes**:
- El total se mostraba siempre en euros, sin importar si era menor a 1€.

📌 **Ahora**:
```python
def formato_moneda(total):
    if total < 1:
        return f"{total * 100:.0f} céntimos"
    else:
        return f"{total:.2f}€"
```
✅ **Mejora**:
- Si la tarifa es **menor de 1€**, se muestra en céntimos (`50 céntimos` en vez de `0.50€`).
- Si es **mayor o igual a 1€**, se muestra con dos decimales (`1.25€`).

---

## 🎯 **Flujo de Funcionamiento**
1️⃣ **El usuario inicia un trayecto** con `m` (moverse) o `p` (parar).  
2️⃣ **El programa captura automáticamente el tiempo** que el taxi pasa en cada estado.  
3️⃣ **Se calcula la tarifa en función del tiempo real transcurrido**.  
4️⃣ **Cuando el usuario finaliza (`f`)**, se muestra el costo total del trayecto.  
5️⃣ **El historial de trayectos se guarda** para futuras consultas.  

---

## 🖥 **Ejemplo de Uso**
```
🛑 Trayecto iniciado. Escribe 'm' para moverte, 'p' para pararte, 'f' para finalizar.
Escribe 'm' (moverse), 'p' (parar) o 'f' (finalizar): m
(Después de 5 segundos...)
🚕 Trayecto en movimiento. Tarifa acumulada: 25 céntimos.
Escribe 'm' (moverse), 'p' (parar) o 'f' (finalizar): p
(Después de 3 segundos...)
🚕 Trayecto detenido. Tarifa acumulada: 31 céntimos.
Escribe 'm' (moverse), 'p' (parar) o 'f' (finalizar): f

🏁 Trayecto finalizado. Tarifa total: 31 céntimos.
```

---

## 🚀 **Beneficios de esta Versión**
✔ **Mayor precisión** → El tiempo se mide en segundos reales, sin depender del usuario.  
✔ **Más intuitivo** → Solo se indican los cambios de estado, sin necesidad de escribir números.  
✔ **Flujo de uso más realista** → Simula un taxímetro de verdad.  
✔ **Código más limpio y fácil de entender** → Sin entradas manuales innecesarias.  

---

## 📌 **Conclusión**
- **Este proyecto demuestra cómo `time` puede mejorar la funcionalidad de un programa** sin necesidad de cambios complejos.  
- **Nos permite entender cómo medir el tiempo y cómo estructurar un programa de manera modular**.  
- **Además, este código sigue siendo una excelente base para futuras mejoras** (como integrar GPS o aplicar tarifas dinámicas).  

👨‍💻 **¡Prueba el código y experimenta con los cambios!** 🚕💨


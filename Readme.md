# 📌 Taxímetro Digital - Nivel Medio

## 🚀 Mejoras Implementadas en esta Rama
Esta rama implementa funcionalidades adicionales para mejorar la trazabilidad y la fiabilidad del taxímetro digital. Se han agregado las siguientes mejoras respecto a la versión anterior:

### 🛠 1️⃣ Sistema de Logs
- Se ha implementado `logging` para registrar eventos clave.
- Se guarda un historial en `taximetro.log`, registrando:
  - Inicio y finalización de trayectos.
  - Cambios de estado (moviéndose/detenido) con tiempo y tarifa acumulada.
  - Consultas al historial de trayectos.

### 🧪 2️⃣ Pruebas Unitarias
- Se han añadido pruebas con `unittest` en `tests/test_taximetro.py`.
- Se verifica:
  - Cálculo correcto de tarifas en movimiento y detenido.
  - Formateo correcto de la moneda (céntimos o euros).

### 📜 3️⃣ Historial de Trayectos en Archivo de Texto
- Ahora, cada trayecto finalizado se almacena en `historial.txt`.
- Al iniciar el programa, el historial se carga automáticamente.
- Esto permite que los trayectos persistan entre ejecuciones del programa.

---

## ✅ Ejecutar la Aplicación y los Tests
### 1️⃣ **Ejecutar el taxímetro**
```sh
uv run python main.py
```

### 2️⃣ **Ejecutar los tests unitarios**
```sh
uv run python -m unittest discover tests -v
```

---

## 📌 Impacto de las Mejoras
Estas mejoras permiten que el programa sea más robusto y trazable. Ahora, cada acción queda registrada, asegurando mayor confiabilidad y depuración de errores.

---

## 📌 Siguiente Paso
Una posible mejora futura es la **configuración de tarifas dinámicas**, permitiendo ajustar precios sin modificar el código. Esto se podría lograr con un archivo de configuración `config.txt`.

---



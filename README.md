# 📐 Programación Lineal Interactiva

Aplicación de escritorio para resolver problemas de **programación lineal de 2 variables** mediante el método gráfico. Permite ingresar la función objetivo y las restricciones de forma interactiva, y genera automáticamente la visualización gráfica de la región factible y la solución óptima.

---

## 🖥️ Tecnologías

| Componente | Tecnología |
|---|---|
| Lenguaje | Python 3.8+ |
| GUI | Tkinter (estándar de Python) |
| Visualización | Matplotlib + `FigureCanvasTkAgg` |
| Cálculo numérico | NumPy |
| Empaquetado | PyInstaller |

---

## 📁 Estructura del proyecto

```
├── programacion_lineal_interactiva.py  # Aplicación principal
├── guia_programacion_lineal.py         # Manual de instrucciones de uso
├── ejemplos_programacion_lineal.py     # Ejemplos con cálculos manuales
├── demostracion_completa.py            # Demostración paso a paso del algoritmo
├── mejoras_visualizacion.py            # Registro de mejoras aplicadas a la UI
├── crear_ejecutable.py                 # Script para generar el .exe con PyInstaller
└── README.md
```

---

## ⚙️ Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/TU_USUARIO/programacion-lineal.git
   cd programacion-lineal
   ```

2. Instala las dependencias:
   ```bash
   pip install numpy matplotlib
   ```

3. Ejecuta la aplicación:
   ```bash
   python programacion_lineal_interactiva.py
   ```

> **Nota:** Tkinter viene incluido con Python. No requiere instalación adicional.

---

## 🚀 Uso

1. **Selecciona** el tipo de optimización: *Maximizar* o *Minimizar*
2. **Ingresa** los coeficientes de la función objetivo `Z = C1·X₁ + C2·X₂`
3. **Agrega** las restricciones una por una:
   - Coeficientes `A1`, `A2`
   - Tipo de inecuación: `<=`, `>=` o `=`
   - Valor del lado derecho `B`
4. Marca o desmarca la opción de **no negatividad** `X₁, X₂ ≥ 0`
5. Presiona **RESOLVER** para generar el gráfico

También puedes usar el botón **Ejemplo Demo** para cargar un problema precargado automáticamente.

---

## 📊 Ejemplo

**Problema:** Maximizar `Z = 3X₁ + 2X₂`

| Restricción | Expresión |
|---|---|
| Capacidad de máquina | `2X₁ + X₂ ≤ 100` |
| Capacidad total | `X₁ + X₂ ≤ 80` |
| Límite producto A | `X₁ ≤ 40` |
| No negatividad | `X₁, X₂ ≥ 0` |

**Solución óptima:** `X₁ = 20`, `X₂ = 60`, `Z = 180`

---

## 🗄️ Almacenamiento de datos

Esta aplicación **no utiliza base de datos**. Todos los datos se manejan **en memoria (RAM)** durante la sesión activa y se pierden al cerrar la ventana. No se escribe ningún archivo en disco durante la ejecución normal.

Los datos se almacenan en atributos de la clase `ProgramacionLinealInteractiva`:

| Atributo | Tipo | Contenido |
|---|---|---|
| `self.restricciones` | `list` de tuplas | Cada restricción `(A1, A2, tipo, B)` ingresada por el usuario |
| `self.funcion_objetivo` | `list` | Coeficientes `[C1, C2]` de la función objetivo |
| `self.tipo_optimizacion` | `str` | `'max'` o `'min'` |
| `self.vertices` | `list` de tuplas | Coordenadas `(x, y)` de los vértices de la región factible |
| `self.solucion_optima` | `tuple` | Coordenadas `(x, y)` del punto óptimo |
| `self.valor_optimo` | `float` | Valor de `Z` en la solución óptima |

> Si se desea guardar los resultados, se debe copiar manualmente la información mostrada en pantalla. Una futura mejora podría incluir exportación a PDF o CSV.

---

## 🧮 Algoritmo

La aplicación implementa el **método gráfico** siguiendo estos pasos:

1. Recopila todas las restricciones (incluyendo no negatividad)
2. Calcula las intersecciones entre todos los pares de restricciones
3. Filtra los puntos que satisfacen todas las restricciones (puntos factibles)
4. Ordena los vértices en sentido antihorario para dibujar la región correctamente
5. Evalúa la función objetivo en cada vértice
6. Determina el óptimo según el tipo de optimización (max o min)
7. Genera la visualización gráfica completa

> ⚠️ Este método aplica únicamente para problemas con **2 variables de decisión**.

---

## 📦 Generar ejecutable (.exe)

Para distribuir la aplicación sin necesidad de tener Python instalado:

```bash
python crear_ejecutable.py
```

El ejecutable se genera en la carpeta `dist/ProgramacionLineal.exe`.

---

## 📋 Casos soportados

- ✅ Maximización y minimización
- ✅ Restricciones `<=`, `>=`, `=`
- ✅ Restricciones de no negatividad opcionales
- ✅ Múltiples restricciones
- ✅ Regiones factibles con múltiples vértices
- ✅ Validación de entrada de datos

---

## 📄 Licencia

Este proyecto fue desarrollado con fines académicos.

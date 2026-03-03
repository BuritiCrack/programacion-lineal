"""
DEMOSTRACIÓN COMPLETA - Programación Lineal Interactiva
======================================================

Este archivo demuestra los cálculos que realiza la aplicación automáticamente.

EJEMPLO 1: PROBLEMA DE PRODUCCIÓN (MAXIMIZACIÓN)
==============================================
Función Objetivo: Maximizar Z = 3X₁ + 2X₂

Restricciones:
1. 2X₁ + X₂ ≤ 100  (capacidad de máquina)
2. X₁ + X₂ ≤ 80    (capacidad total)  
3. X₁ ≤ 40         (límite producto A)
4. X₁, X₂ ≥ 0      (no negatividad)

CÁLCULO DE VÉRTICES:
==================
1. Intersección de restricciones:
   
   V1: Origen (0, 0)
   - X₁ = 0, X₂ = 0
   - Z = 3(0) + 2(0) = 0
   
   V2: Intersección X₁=0 con X₁+X₂≤80
   - X₁ = 0, X₂ = 80
   - Z = 3(0) + 2(80) = 160
   
   V3: Intersección 2X₁+X₂=100 con X₁+X₂=80
   - Sistema: 2X₁ + X₂ = 100
   -         X₁ + X₂ = 80
   - Restando: X₁ = 20, entonces X₂ = 60
   - Z = 3(20) + 2(60) = 180 ← MÁXIMO
   
   V4: Intersección X₁=40 con X₁+X₂=80
   - X₁ = 40, X₂ = 40
   - Pero viola 2X₁+X₂≤100: 2(40)+40=120>100 ❌
   
   V4: Intersección X₁=40 con 2X₁+X₂=100
   - X₁ = 40, X₂ = 20  
   - Z = 3(40) + 2(20) = 160
   
   V5: Intersección X₁=40 con X₂=0
   - X₁ = 40, X₂ = 0
   - Z = 3(40) + 2(0) = 120

RESULTADO: X₁* = 20, X₂* = 60, Z* = 180

EJEMPLO 2: PROBLEMA DE DIETA (MINIMIZACIÓN)
==========================================
Función Objetivo: Minimizar Z = 2X₁ + 3X₂

Restricciones:
1. X₁ + 2X₂ ≥ 10   (vitamina A)
2. 2X₁ + X₂ ≥ 12   (vitamina B)
3. X₁, X₂ ≥ 0      (no negatividad)

CÁLCULO DE VÉRTICES:
==================
V1: Intersección X₂=0 con 2X₁+X₂≥12
- X₁ = 6, X₂ = 0 (punto (6,0))
- Z = 2(6) + 3(0) = 12

V2: Intersección X₁+2X₂=10 con 2X₁+X₂=12
- Sistema: X₁ + 2X₂ = 10 → X₁ = 10 - 2X₂
-         2X₁ + X₂ = 12 → 2(10-2X₂) + X₂ = 12
-         20 - 4X₂ + X₂ = 12 → -3X₂ = -8
- X₂ = 8/3, X₁ = 10 - 2(8/3) = 14/3
- Z = 2(14/3) + 3(8/3) = 28/3 + 24/3 = 52/3 = 17.33

V3: Intersección X₁=0 con X₁+2X₂≥10
- X₁ = 0, X₂ = 5 (punto (0,5))
- Verificar 2X₁+X₂≥12: 2(0)+5=5<12 ❌
- Usar intersección con 2X₁+X₂=12: X₁=0, X₂=12
- Z = 2(0) + 3(12) = 36

RESULTADO: X₁* = 14/3 ≈ 4.67, X₂* = 8/3 ≈ 2.67, Z* = 52/3 ≈ 17.33

PUNTOS DE CORTE AUTOMÁTICOS:
===========================
Para restricción aX₁ + bX₂ = c:

1. Punto de corte con eje X₁ (X₂=0): X₁ = c/a
2. Punto de corte con eje X₂ (X₁=0): X₂ = c/b

Ejemplo con 2X₁ + X₂ = 100:
- Corte X₁: (50, 0) cuando X₂=0
- Corte X₂: (0, 100) cuando X₁=0

INSTRUCCIONES PARA LA APLICACIÓN:
=================================
1. Ejecutar: python programacion_lineal_interactiva.py
2. La aplicación abre una ventana con dos paneles
3. Panel izquierdo: Controles de entrada
4. Panel derecho: Gráfico automático

PASOS PARA USAR:
===============
1. Seleccionar tipo: Maximizar/Minimizar
2. Ingresar coeficientes de función objetivo
3. Agregar restricciones una por una:
   - Coeficientes A1, A2
   - Tipo de inecuación (<=, >=, =)  
   - Valor del lado derecho B
4. Marcar/desmarcar no negatividad según necesites
5. Presionar "RESOLVER"

LA APLICACIÓN CALCULARÁ AUTOMÁTICAMENTE:
=======================================
✓ Todos los puntos de intersección entre restricciones
✓ Verificación de factibilidad de cada punto
✓ Identificación de vértices de la región factible
✓ Evaluación de función objetivo en todos los vértices
✓ Determinación de la solución óptima
✓ Visualización gráfica completa con:
  - Líneas de restricciones con colores diferentes
  - Región factible sombreada
  - Vértices marcados y etiquetados
  - Solución óptima destacada
  - Línea de función objetivo óptima
  - Dirección de optimización con flecha
  - Información detallada al lado del gráfico

FUNCIONALIDADES AVANZADAS:
=========================
• Manejo automático de casos especiales
• Ordenamiento correcto de vértices para dibujo
• Detección de regiones no acotadas
• Manejo de restricciones de igualdad
• Zoom automático según el tamaño de la región
• Leyendas y etiquetas informativas
• Cálculos con precisión numérica adecuada

¡La aplicación está lista para usar con cualquier problema de programación lineal de 2 variables!
"""

if __name__ == "__main__":
    print("Demostración cargada.")
    print("Ejecuta 'python programacion_lineal_interactiva.py' para usar la aplicación interactiva.")

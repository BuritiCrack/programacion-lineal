"""
Guía de Uso - Aplicación de Programación Lineal Interactiva
===========================================================

INSTRUCCIONES DE USO:
1. La aplicación se abre con una interfaz dividida en dos partes:
   - Panel izquierdo: Controles de entrada
   - Panel derecho: Área de gráfico

2. FUNCIÓN OBJETIVO:
   - Selecciona "Maximizar" o "Minimizar"
   - Ingresa los coeficientes C1 y C2 para Z = C1*X1 + C2*X2

3. RESTRICCIONES:
   - Ingresa coeficientes A1 y A2
   - Selecciona el tipo de inecuación (<=, >=, =)
   - Ingresa el valor del lado derecho B
   - Presiona "Agregar Restricción"
   - Repite para todas las restricciones

4. OPCIONES ADICIONALES:
   - Marca/desmarca "X₁, X₂ ≥ 0" según necesites
   - Usa "Eliminar" para quitar la restricción seleccionada
   - Usa "Limpiar Todo" para empezar de nuevo

5. RESOLVER:
   - Presiona "RESOLVER" para generar el gráfico
   - El programa encuentra automáticamente los vértices
   - Identifica la solución óptima
   - Muestra toda la información detallada

FUNCIONALIDADES PRINCIPALES:
- Cálculo automático de puntos de corte
- Identificación de vértices de la región factible
- Evaluación de la función objetivo en todos los vértices
- Visualización gráfica completa con región sombreada
- Información detallada de la solución

EJEMPLO DE USO:
Problema: Maximizar Z = 3X₁ + 2X₂
Sujeto a: 2X₁ + X₂ ≤ 100
          X₁ + X₂ ≤ 80
          X₁ ≤ 40
          X₁, X₂ ≥ 0

Pasos:
1. Seleccionar "Maximizar"
2. Ingresar C1=3, C2=2
3. Agregar restricción: 2, 1, <=, 100
4. Agregar restricción: 1, 1, <=, 80
5. Agregar restricción: 1, 0, <=, 40
6. Mantener marcada "X₁, X₂ ≥ 0"
7. Presionar "RESOLVER"

El programa encontrará automáticamente:
- Vértices: (0,0), (0,80), (20,60), (40,20), (40,0)
- Solución óptima: X₁=20, X₂=60, Z=180

NOTAS IMPORTANTES:
- La aplicación maneja automáticamente casos especiales
- Ordena los vértices para dibujar correctamente la región factible
- Muestra puntos de corte con los ejes
- Incluye flechas indicando la dirección de optimización
- Información detallada se muestra al lado del gráfico
"""

# Ejemplo práctico adicional
def ejemplo_produccion():
    """
    EJEMPLO PRÁCTICO: Problema de Producción
    
    Una empresa fabrica dos productos A y B.
    Cada unidad de A requiere 2 horas de máquina y genera $3 de ganancia.
    Cada unidad de B requiere 1 hora de máquina y genera $2 de ganancia.
    
    Restricciones:
    - Máximo 100 horas de máquina disponibles: 2A + B ≤ 100
    - Máximo 80 unidades en total: A + B ≤ 80  
    - Máximo 40 unidades de A: A ≤ 40
    - No negatividad: A, B ≥ 0
    
    Objetivo: Maximizar ganancia Z = 3A + 2B
    
    SOLUCIÓN ESPERADA:
    A* = 20, B* = 60, Z* = 180
    """
    pass

def ejemplo_dieta():
    """
    EJEMPLO PRÁCTICO: Problema de Dieta
    
    Minimizar el costo de una dieta que contenga al menos:
    - 10 unidades de vitamina A
    - 12 unidades de vitamina B
    
    Alimentos disponibles:
    - X₁: Cuesta $2/unidad, contiene 1 unidad A y 2 unidades B
    - X₂: Cuesta $3/unidad, contiene 2 unidades A y 1 unidad B
    
    Restricciones:
    - X₁ + 2X₂ ≥ 10 (vitamina A)
    - 2X₁ + X₂ ≥ 12 (vitamina B)
    - X₁, X₂ ≥ 0
    
    Objetivo: Minimizar costo Z = 2X₁ + 3X₂
    
    Para ingresar este problema:
    1. Seleccionar "Minimizar"
    2. Ingresar C1=2, C2=3
    3. Agregar: 1, 2, >=, 10
    4. Agregar: 2, 1, >=, 12
    5. Resolver
    """
    pass

if __name__ == "__main__":
    print("Guía de uso cargada. Ejecuta programacion_lineal_interactiva.py para usar la aplicación.")
    print("\nEJEMPLOS INCLUIDOS:")
    print("- Problema de Producción (maximización)")
    print("- Problema de Dieta (minimización)")
    print("- Usa el botón 'Ejemplo Demo' en la aplicación para cargar automáticamente un ejemplo")

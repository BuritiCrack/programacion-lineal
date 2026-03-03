"""
Ejemplos y Casos de Prueba para Programación Lineal
==================================================
Colección de problemas típicos para probar la aplicación
"""

import numpy as np
import matplotlib.pyplot as plt

def resolver_ejemplo_basico():
    """
    Ejemplo básico de maximización
    Maximizar: Z = 3X₁ + 2X₂
    Sujeto a: 2X₁ + X₂ ≤ 100
              X₁ + X₂ ≤ 80
              X₁ ≤ 40
              X₁, X₂ ≥ 0
    
    Solución esperada: X₁=20, X₂=60, Z=180
    """
    print("EJEMPLO 1: Problema de Producción")
    print("="*40)
    print("Función Objetivo: Maximizar Z = 3X₁ + 2X₂")
    print("Restricciones:")
    print("  1. 2X₁ + X₂ ≤ 100  (capacidad máquina)")
    print("  2. X₁ + X₂ ≤ 80    (capacidad total)")
    print("  3. X₁ ≤ 40         (límite producto A)")
    print("  4. X₁, X₂ ≥ 0      (no negatividad)")
    
    # Vértices calculados manualmente
    vertices = [(0, 0), (0, 80), (20, 60), (40, 20), (40, 0)]
    
    print(f"\nVértices de la región factible:")
    for i, (x, y) in enumerate(vertices, 1):
        z = 3*x + 2*y
        print(f"  V{i}: ({x}, {y}) → Z = {z}")
    
    # Encontrar óptimo
    valores = [3*x + 2*y for x, y in vertices]
    max_valor = max(valores)
    idx_max = valores.index(max_valor)
    x_opt, y_opt = vertices[idx_max]
    
    print(f"\nSOLUCIÓN ÓPTIMA:")
    print(f"  X₁* = {x_opt}")
    print(f"  X₂* = {y_opt}")
    print(f"  Z*  = {max_valor}")
    
    return vertices, (x_opt, y_opt, max_valor)

def resolver_ejemplo_minimizacion():
    """
    Ejemplo de minimización
    Minimizar: Z = 2X₁ + 3X₂
    Sujeto a: X₁ + 2X₂ ≥ 10
              2X₁ + X₂ ≥ 12
              X₁, X₂ ≥ 0
    
    Solución esperada: X₁=14/3, X₂=8/3, Z=20
    """
    print("\n\nEJEMPLO 2: Problema de Dieta (Minimización)")
    print("="*45)
    print("Función Objetivo: Minimizar Z = 2X₁ + 3X₂")
    print("Restricciones:")
    print("  1. X₁ + 2X₂ ≥ 10   (vitamina A)")
    print("  2. 2X₁ + X₂ ≥ 12   (vitamina B)")
    print("  3. X₁, X₂ ≥ 0      (no negatividad)")
    
    # Para minimización, necesitamos encontrar la intersección de las restricciones
    # Intersección de X₁ + 2X₂ = 10 y 2X₁ + X₂ = 12
    # Resolviendo el sistema:
    # X₁ + 2X₂ = 10  → X₁ = 10 - 2X₂
    # 2(10 - 2X₂) + X₂ = 12 → 20 - 4X₂ + X₂ = 12 → -3X₂ = -8 → X₂ = 8/3
    # X₁ = 10 - 2(8/3) = 10 - 16/3 = 30/3 - 16/3 = 14/3
    
    vertices = [(0, 12), (14/3, 8/3), (10, 0)]
    
    print(f"\nVértices de la región factible:")
    for i, (x, y) in enumerate(vertices, 1):
        z = 2*x + 3*y
        print(f"  V{i}: ({x:.3f}, {y:.3f}) → Z = {z:.3f}")
    
    # Encontrar mínimo
    valores = [2*x + 3*y for x, y in vertices]
    min_valor = min(valores)
    idx_min = valores.index(min_valor)
    x_opt, y_opt = vertices[idx_min]
    
    print(f"\nSOLUCIÓN ÓPTIMA:")
    print(f"  X₁* = {x_opt:.3f}")
    print(f"  X₂* = {y_opt:.3f}")
    print(f"  Z*  = {min_valor:.3f}")
    
    return vertices, (x_opt, y_opt, min_valor)

def resolver_ejemplo_mixto():
    """
    Ejemplo con restricciones mixtas
    Maximizar: Z = X₁ + X₂
    Sujeto a: X₁ + X₂ ≤ 6
              2X₁ + X₂ ≥ 4
              X₁ ≥ 1
              X₂ ≤ 4
              X₁, X₂ ≥ 0
    """
    print("\n\nEJEMPLO 3: Restricciones Mixtas")
    print("="*35)
    print("Función Objetivo: Maximizar Z = X₁ + X₂")
    print("Restricciones:")
    print("  1. X₁ + X₂ ≤ 6     (límite superior)")
    print("  2. 2X₁ + X₂ ≥ 4    (límite inferior)")
    print("  3. X₁ ≥ 1          (mínimo X₁)")
    print("  4. X₂ ≤ 4          (máximo X₂)")
    print("  5. X₁, X₂ ≥ 0      (no negatividad)")
    
    # Vértices del problema mixto
    vertices = [(1, 2), (1, 4), (2, 4), (6, 0), (2, 0)]
    
    # Filtrar vértices que satisfacen todas las restricciones
    vertices_validos = []
    for x, y in vertices:
        if (x + y <= 6 and 2*x + y >= 4 and x >= 1 and y <= 4 and x >= 0 and y >= 0):
            vertices_validos.append((x, y))
    
    print(f"\nVértices válidos de la región factible:")
    for i, (x, y) in enumerate(vertices_validos, 1):
        z = x + y
        print(f"  V{i}: ({x}, {y}) → Z = {z}")
    
    # Encontrar óptimo
    if vertices_validos:
        valores = [x + y for x, y in vertices_validos]
        max_valor = max(valores)
        idx_max = valores.index(max_valor)
        x_opt, y_opt = vertices_validos[idx_max]
        
        print(f"\nSOLUCIÓN ÓPTIMA:")
        print(f"  X₁* = {x_opt}")
        print(f"  X₂* = {y_opt}")
        print(f"  Z*  = {max_valor}")
    
    return vertices_validos

def calcular_puntos_corte(a, b, c):
    """
    Calcula los puntos de corte de una restricción aX₁ + bX₂ = c
    con los ejes X₁ y X₂
    """
    print(f"\nPuntos de corte para {a}X₁ + {b}X₂ = {c}:")
    
    # Punto de corte con eje X₁ (cuando X₂ = 0)
    if abs(a) > 1e-10:
        x_corte = c / a
        print(f"  Con eje X₁: ({x_corte:.3f}, 0)")
    else:
        print("  Con eje X₁: No existe (línea horizontal)")
    
    # Punto de corte con eje X₂ (cuando X₁ = 0)
    if abs(b) > 1e-10:
        y_corte = c / b
        print(f"  Con eje X₂: (0, {y_corte:.3f})")
    else:
        print("  Con eje X₂: No existe (línea vertical)")

def demostrar_casos_especiales():
    """
    Demuestra casos especiales en programación lineal
    """
    print("\n\nCASOS ESPECIALES:")
    print("="*20)
    
    print("\n1. SOLUCIÓN NO ACOTADA:")
    print("   Maximizar Z = X₁ + X₂")
    print("   Sujeto a: X₁ - X₂ ≤ 1")
    print("            X₁, X₂ ≥ 0")
    print("   → La función objetivo puede crecer infinitamente")
    
    print("\n2. REGIÓN FACTIBLE VACÍA:")
    print("   Maximizar Z = X₁ + X₂")
    print("   Sujeto a: X₁ + X₂ ≤ -1")
    print("            X₁, X₂ ≥ 0")
    print("   → No existe región factible")
    
    print("\n3. SOLUCIONES MÚLTIPLES:")
    print("   Maximizar Z = X₁ + X₂")
    print("   Sujeto a: X₁ + X₂ ≤ 4")
    print("            X₁, X₂ ≥ 0")
    print("   → Toda la arista de (0,4) a (4,0) es óptima")

def main():
    """Función principal que ejecuta todos los ejemplos"""
    print("EJEMPLOS DE PROGRAMACIÓN LINEAL")
    print("="*50)
    
    # Ejecutar ejemplos
    resolver_ejemplo_basico()
    resolver_ejemplo_minimizacion() 
    resolver_ejemplo_mixto()
    
    # Mostrar cálculos de puntos de corte
    print("\n\nCÁLCULO DE PUNTOS DE CORTE:")
    print("="*30)
    calcular_puntos_corte(2, 1, 100)  # 2X₁ + X₂ = 100
    calcular_puntos_corte(1, 1, 80)   # X₁ + X₂ = 80
    calcular_puntos_corte(1, 0, 40)   # X₁ = 40
    
    # Casos especiales
    demostrar_casos_especiales()
    
    print("\n\n" + "="*50)
    print("INSTRUCCIONES PARA LA APLICACIÓN INTERACTIVA:")
    print("1. Ejecuta 'programacion_lineal_interactiva.py'")
    print("2. Usa el botón 'Ejemplo Demo' para cargar automáticamente")
    print("3. O ingresa manualmente cualquiera de estos ejemplos")
    print("4. Los resultados deben coincidir con los cálculos mostrados")
    print("="*50)

if __name__ == "__main__":
    main()

"""
Script para crear ejecutable de la aplicación de Programación Lineal
Convierte el archivo Python en un ejecutable .exe independiente
"""

import subprocess
import sys
import os

def verificar_archivo():
    """Verifica que existe el archivo principal"""
    archivo = "programacion_lineal_interactiva.py"
    if not os.path.exists(archivo):
        print(f"❌ No se encuentra el archivo '{archivo}'")
        print("   Asegúrate de estar en la carpeta correcta")
        return False
    
    # Verificar que el archivo no esté vacío
    with open(archivo, 'r', encoding='utf-8') as f:
        contenido = f.read()
        if len(contenido.strip()) < 1000:
            print(f"⚠️  El archivo parece estar incompleto ({len(contenido)} caracteres)")
            return False
    
    print(f"✅ Archivo '{archivo}' encontrado y verificado")
    return True

def instalar_pyinstaller():
    """Instala PyInstaller para crear el ejecutable"""
    print("📦 Instalando PyInstaller...")
    try:
        # Usar el Python del entorno virtual si está disponible
        python_exe = sys.executable
        subprocess.check_call([python_exe, "-m", "pip", "install", "pyinstaller"])
        print("✅ PyInstaller instalado correctamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al instalar PyInstaller: {e}")
        return False

def crear_ejecutable():
    """Crea el archivo ejecutable usando PyInstaller"""
    print("🔨 Creando ejecutable...")
    
    # Comando para crear ejecutable
    comando = [
        "pyinstaller",
        "--onefile",                    # Un solo archivo ejecutable
        "--windowed",                   # Sin ventana de consola
        "--name=ProgramacionLineal",    # Nombre del ejecutable
        "--clean",                      # Limpiar cache anterior
        "programacion_lineal_interactiva.py"
    ]
    
    try:
        subprocess.check_call(comando)
        print("✅ Ejecutable creado correctamente")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al crear ejecutable: {e}")
        return False
    except FileNotFoundError:
        print("❌ PyInstaller no encontrado. Reinstalando...")
        if instalar_pyinstaller():
            return crear_ejecutable()
        return False

def mostrar_resultado():
    """Muestra la información del ejecutable creado"""
    exe_path = os.path.join("dist", "ProgramacionLineal.exe")
    
    if os.path.exists(exe_path):
        tamaño = os.path.getsize(exe_path) / (1024*1024)  # MB
        
        print("\n" + "="*60)
        print("🎉 ¡EJECUTABLE CREADO EXITOSAMENTE!")
        print("="*60)
        print(f"📁 Ubicación: {exe_path}")
        print(f"📊 Tamaño: {tamaño:.1f} MB")
        print(f"📧 Archivo para enviar: ProgramacionLineal.exe")
        print("\n📋 INSTRUCCIONES PARA LA PROFESORA:")
        print("   1. Descargar el archivo ProgramacionLineal.exe")
        print("   2. Hacer doble clic para ejecutar")
        print("   3. No necesita instalar Python ni otras dependencias")
        print("   4. Funciona en cualquier computadora Windows")
        print("="*60)
        return True
    else:
        print("❌ No se encontró el ejecutable en dist/")
        return False

def limpiar_archivos():
    """Limpia archivos temporales de PyInstaller"""
    import shutil
    
    try:
        if os.path.exists("build"):
            shutil.rmtree("build")
        if os.path.exists("ProgramacionLineal.spec"):
            os.remove("ProgramacionLineal.spec")
        print("🧹 Archivos temporales eliminados")
    except Exception as e:
        print(f"⚠️  No se pudieron eliminar archivos temporales: {e}")

def main():
    """Función principal para crear el ejecutable"""
    print("🚀 CREADOR DE EJECUTABLE - PROGRAMACIÓN LINEAL")
    print("="*50)
    print("📅 Fecha:", "29 de Agosto, 2025")
    print("👨‍💻 Proyecto: Investigación de Operaciones")
    print("="*50)
    
    # Paso 1: Verificar archivo fuente
    print("\n🔍 PASO 1: Verificando archivo fuente...")
    if not verificar_archivo():
        print("\n❌ PROCESO CANCELADO")
        print("   Verifica que el archivo programacion_lineal_interactiva.py")
        print("   esté completo y en la carpeta actual")
        input("\nPresiona ENTER para salir...")
        return
    
    # Paso 2: Instalar PyInstaller
    print("\n📦 PASO 2: Preparando herramientas...")
    if not instalar_pyinstaller():
        print("\n❌ PROCESO CANCELADO")
        print("   No se pudo instalar PyInstaller")
        input("\nPresiona ENTER para salir...")
        return
    
    # Paso 3: Crear ejecutable
    print("\n🔨 PASO 3: Creando ejecutable...")
    print("   (Esto puede tomar unos minutos...)")
    if not crear_ejecutable():
        print("\n❌ PROCESO CANCELADO")
        print("   Error al crear el ejecutable")
        input("\nPresiona ENTER para salir...")
        return
    
    # Paso 4: Verificar resultado
    print("\n✅ PASO 4: Verificando resultado...")
    if mostrar_resultado():
        limpiar_archivos()
        print("\n🎯 PROCESO COMPLETADO EXITOSAMENTE")
        print("   Tu ejecutable está listo para enviar a la profesora!")
    else:
        print("\n❌ PROBLEMA AL VERIFICAR EL EJECUTABLE")
    
    input("\nPresiona ENTER para salir...")

if __name__ == "__main__":
    main()

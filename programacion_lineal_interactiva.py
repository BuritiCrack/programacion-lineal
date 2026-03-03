import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox, Button, RadioButtons, CheckButtons
import matplotlib.patches as patches
from itertools import combinations
import tkinter as tk
from tkinter import messagebox, ttk
import warnings
warnings.filterwarnings('ignore')

class ProgramacionLinealInteractiva:
    def __init__(self):
        """Inicializa la aplicación de programación lineal interactiva"""
        self.fig = None
        self.ax = None
        self.restricciones = []
        self.funcion_objetivo = [1, 1]  # Coeficientes por defecto
        self.tipo_optimizacion = 'max'  # 'max' o 'min'
        self.vertices = []
        self.solucion_optima = None
        self.valor_optimo = None
        
        # Configurar la ventana principal
        self.setup_gui()
    
    def setup_gui(self):
        """Configura la interfaz gráfica principal"""
        self.root = tk.Tk()
        self.root.title("Programación Lineal - 2 Variables")
        self.root.geometry("1400x900")  # Ventana más grande para acomodar mejor el contenido
        
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Frame izquierdo para controles
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        # Frame derecho para gráfico (se creará cuando sea necesario)
        self.graph_frame = ttk.Frame(main_frame)
        self.graph_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.setup_controls(control_frame)
    
    def setup_controls(self, parent):
        """Configura los controles de entrada"""
        
        # Título
        title_label = ttk.Label(parent, text="Programación Lineal 2D", 
                               font=("Arial", 16, "bold"))
        title_label.pack(pady=(0, 20))
        
        # Función Objetivo
        obj_frame = ttk.LabelFrame(parent, text="Función Objetivo", padding=10)
        obj_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Tipo de optimización
        ttk.Label(obj_frame, text="Tipo:").pack(anchor=tk.W)
        self.opt_var = tk.StringVar(value="max")
        ttk.Radiobutton(obj_frame, text="Maximizar", variable=self.opt_var, 
                       value="max").pack(anchor=tk.W)
        ttk.Radiobutton(obj_frame, text="Minimizar", variable=self.opt_var, 
                       value="min").pack(anchor=tk.W)
        
        # Coeficientes de la función objetivo
        coef_frame = ttk.Frame(obj_frame)
        coef_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Label(coef_frame, text="Z =").pack(side=tk.LEFT)
        self.c1_var = tk.StringVar(value="1")
        ttk.Entry(coef_frame, textvariable=self.c1_var, width=8).pack(side=tk.LEFT, padx=(5, 0))
        ttk.Label(coef_frame, text="X₁ +").pack(side=tk.LEFT, padx=(5, 0))
        self.c2_var = tk.StringVar(value="1")
        ttk.Entry(coef_frame, textvariable=self.c2_var, width=8).pack(side=tk.LEFT, padx=(5, 0))
        ttk.Label(coef_frame, text="X₂").pack(side=tk.LEFT, padx=(5, 0))
        
        # Restricciones
        rest_frame = ttk.LabelFrame(parent, text="Restricciones", padding=10)
        rest_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Lista de restricciones
        self.rest_listbox = tk.Listbox(rest_frame, height=8)
        self.rest_listbox.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Entrada para nueva restricción
        new_rest_frame = ttk.Frame(rest_frame)
        new_rest_frame.pack(fill=tk.X, pady=(0, 5))
        
        self.a1_var = tk.StringVar(value="1")
        ttk.Entry(new_rest_frame, textvariable=self.a1_var, width=6).pack(side=tk.LEFT)
        ttk.Label(new_rest_frame, text="X₁ +").pack(side=tk.LEFT, padx=(2, 0))
        
        self.a2_var = tk.StringVar(value="1")
        ttk.Entry(new_rest_frame, textvariable=self.a2_var, width=6).pack(side=tk.LEFT, padx=(2, 0))
        ttk.Label(new_rest_frame, text="X₂").pack(side=tk.LEFT, padx=(2, 0))
        
        # Tipo de inecuación
        self.ineq_var = tk.StringVar(value="<=")
        ineq_combo = ttk.Combobox(new_rest_frame, textvariable=self.ineq_var, 
                                 values=["<=", ">=", "="], width=4, state="readonly")
        ineq_combo.pack(side=tk.LEFT, padx=(5, 0))
        
        self.b_var = tk.StringVar(value="1")
        ttk.Entry(new_rest_frame, textvariable=self.b_var, width=6).pack(side=tk.LEFT, padx=(5, 0))
        
        # Botones para restricciones
        btn_frame = ttk.Frame(rest_frame)
        btn_frame.pack(fill=tk.X, pady=(5, 0))
        
        ttk.Button(btn_frame, text="Agregar Restricción", 
                  command=self.agregar_restriccion).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_frame, text="Eliminar", 
                  command=self.eliminar_restriccion).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(btn_frame, text="Limpiar Todo", 
                  command=self.limpiar_restricciones).pack(side=tk.LEFT)
        
        # Restricciones de no negatividad
        noneg_frame = ttk.Frame(rest_frame)
        noneg_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.noneg_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(noneg_frame, text="X₁, X₂ ≥ 0 (No negatividad)", 
                       variable=self.noneg_var).pack(anchor=tk.W)
        
        # Botones principales
        main_btn_frame = ttk.Frame(parent)
        main_btn_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Button(main_btn_frame, text="RESOLVER", 
                  command=self.resolver_problema, 
                  style="Accent.TButton").pack(fill=tk.X, pady=(0, 5))
        ttk.Button(main_btn_frame, text="Limpiar Gráfico", 
                  command=self.limpiar_grafico).pack(fill=tk.X, pady=(0, 5))
        ttk.Button(main_btn_frame, text="Ejemplo Demo", 
                  command=self.cargar_ejemplo).pack(fill=tk.X)
        
        # Configurar estilo para el botón principal
        style = ttk.Style()
        style.configure("Accent.TButton", font=("Arial", 10, "bold"))
    
    def agregar_restriccion(self):
        """Agrega una nueva restricción a la lista"""
        try:
            a1 = float(self.a1_var.get())
            a2 = float(self.a2_var.get())
            b = float(self.b_var.get())
            ineq = self.ineq_var.get()
            
            restriccion = (a1, a2, ineq, b)
            self.restricciones.append(restriccion)
            
            # Mostrar en la lista
            rest_text = f"{a1}X₁ + {a2}X₂ {ineq} {b}"
            self.rest_listbox.insert(tk.END, rest_text)
            
            # Limpiar campos
            self.a1_var.set("1")
            self.a2_var.set("1")
            self.b_var.set("1")
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")
    
    def eliminar_restriccion(self):
        """Elimina la restricción seleccionada"""
        selection = self.rest_listbox.curselection()
        if selection:
            index = selection[0]
            self.rest_listbox.delete(index)
            del self.restricciones[index]
    
    def limpiar_restricciones(self):
        """Limpia todas las restricciones"""
        self.rest_listbox.delete(0, tk.END)
        self.restricciones = []
    
    def cargar_ejemplo(self):
        """Carga un ejemplo de demostración"""
        # Limpiar todo
        self.limpiar_restricciones()
        
        # Configurar función objetivo
        self.c1_var.set("3")
        self.c2_var.set("2")
        self.opt_var.set("max")
        
        # Agregar restricciones de ejemplo
        ejemplos = [
            (2, 1, "<=", 100),
            (1, 1, "<=", 80),
            (1, 0, "<=", 40)
        ]
        
        for a1, a2, ineq, b in ejemplos:
            self.restricciones.append((a1, a2, ineq, b))
            rest_text = f"{a1}X₁ + {a2}X₂ {ineq} {b}"
            self.rest_listbox.insert(tk.END, rest_text)
        
        messagebox.showinfo("Ejemplo Cargado", 
                           "Se ha cargado un ejemplo de problema de programación lineal.\n" +
                           "Presiona 'RESOLVER' para ver la solución gráfica.")
    
    def resolver_problema(self):
        """Resuelve el problema de programación lineal"""
        try:
            # Obtener coeficientes de la función objetivo
            c1 = float(self.c1_var.get())
            c2 = float(self.c2_var.get())
            self.funcion_objetivo = [c1, c2]
            self.tipo_optimizacion = self.opt_var.get()
            
            if not self.restricciones:
                messagebox.showwarning("Advertencia", "Agregue al menos una restricción")
                return
            
            # Resolver el problema
            self.encontrar_vertices()
            self.evaluar_funcion_objetivo()
            self.crear_grafico()
            
        except ValueError:
            messagebox.showerror("Error", "Por favor verifique que todos los valores sean numéricos")
        except Exception as e:
            messagebox.showerror("Error", f"Error al resolver el problema: {str(e)}")
    
    def encontrar_vertices(self):
        """Encuentra los vértices de la región factible"""
        self.vertices = []
        
        # Lista de todas las restricciones incluyendo límites
        todas_restricciones = list(self.restricciones)
        
        # Agregar restricciones de no negatividad si están activas
        if self.noneg_var.get():
            todas_restricciones.extend([
                (1, 0, ">=", 0),  # X₁ >= 0
                (0, 1, ">=", 0)   # X₂ >= 0
            ])
        
        # Encontrar intersecciones de cada par de restricciones
        for i, rest1 in enumerate(todas_restricciones):
            for j, rest2 in enumerate(todas_restricciones):
                if i >= j:
                    continue
                
                punto = self.interseccion_restricciones(rest1, rest2)
                if punto is not None:
                    x, y = punto
                    # Verificar si el punto satisface todas las restricciones
                    if self.punto_factible(x, y, todas_restricciones):
                        # Evitar duplicados
                        if not any(abs(x - vx) < 1e-10 and abs(y - vy) < 1e-10 
                                 for vx, vy in self.vertices):
                            self.vertices.append((x, y))
    
    def interseccion_restricciones(self, rest1, rest2):
        """Encuentra la intersección entre dos restricciones"""
        a1, b1, _, c1 = rest1
        a2, b2, _, c2 = rest2
        
        # Sistema de ecuaciones: a1*x + b1*y = c1, a2*x + b2*y = c2
        det = a1 * b2 - a2 * b1
        
        if abs(det) < 1e-10:  # Líneas paralelas
            return None
        
        x = (c1 * b2 - c2 * b1) / det
        y = (a1 * c2 - a2 * c1) / det
        
        return (x, y)
    
    def punto_factible(self, x, y, restricciones):
        """Verifica si un punto satisface todas las restricciones"""
        for a, b, ineq, c in restricciones:
            valor = a * x + b * y
            
            if ineq == "<=" and valor > c + 1e-10:
                return False
            elif ineq == ">=" and valor < c - 1e-10:
                return False
            elif ineq == "=" and abs(valor - c) > 1e-10:
                return False
        
        return True
    
    def evaluar_funcion_objetivo(self):
        """Evalúa la función objetivo en todos los vértices"""
        if not self.vertices:
            self.solucion_optima = None
            self.valor_optimo = None
            return
        
        valores = []
        for x, y in self.vertices:
            valor = self.funcion_objetivo[0] * x + self.funcion_objetivo[1] * y
            valores.append((valor, x, y))
        
        # Encontrar el óptimo según el tipo de optimización
        if self.tipo_optimizacion == "max":
            self.valor_optimo, x_opt, y_opt = max(valores)
        else:
            self.valor_optimo, x_opt, y_opt = min(valores)
        
        self.solucion_optima = (x_opt, y_opt)
    
    def crear_grafico(self):
        """Crea y muestra el gráfico con la solución"""
        # Limpiar frame de gráfico anterior
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
        
        # Crear figura de matplotlib con más espacio para la información
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        
        # Ajustar los márgenes para dejar espacio a la información lateral y leyenda inferior
        self.fig.subplots_adjust(left=0.08, right=0.62, top=0.93, bottom=0.15)
        
        # Determinar rango de visualización
        if self.vertices:
            x_coords = [v[0] for v in self.vertices]
            y_coords = [v[1] for v in self.vertices]
            
            x_min = min(0, min(x_coords) - 1)
            x_max = max(x_coords) + 2
            y_min = min(0, min(y_coords) - 1)
            y_max = max(y_coords) + 2
        else:
            x_min, x_max = -1, 10
            y_min, y_max = -1, 10
        
        self.ax.set_xlim(x_min, x_max)
        self.ax.set_ylim(y_min, y_max)
        
        # Dibujar restricciones
        self.dibujar_restricciones(x_min, x_max, y_min, y_max)
        
        # Dibujar región factible
        if len(self.vertices) >= 3:
            self.dibujar_region_factible()
        
        # Dibujar vértices
        self.dibujar_vertices()
        
        # Dibujar función objetivo
        if self.solucion_optima:
            self.dibujar_funcion_objetivo(x_min, x_max, y_min, y_max)
        
        # Configurar gráfico
        self.ax.grid(True, alpha=0.3)
        self.ax.set_xlabel('X₁', fontsize=12)
        self.ax.set_ylabel('X₂', fontsize=12)
        
        titulo = f"Programación Lineal - {'Maximizar' if self.tipo_optimizacion == 'max' else 'Minimizar'}"
        self.ax.set_title(titulo, fontsize=14, fontweight='bold')
        
        # Mostrar información de la solución
        self.mostrar_informacion_solucion()
        
        # Integrar con tkinter
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        canvas = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    def dibujar_restricciones(self, x_min, x_max, y_min, y_max):
        """Dibuja las líneas de las restricciones"""
        x = np.linspace(x_min, x_max, 100)
        
        colores = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']
        
        for i, (a, b, ineq, c) in enumerate(self.restricciones):
            color = colores[i % len(colores)]
            
            if abs(b) > 1e-10:  # b ≠ 0
                y = (c - a * x) / b
                self.ax.plot(x, y, color=color, linewidth=2, 
                           label=f'{a}X₁ + {b}X₂ {ineq} {c}')
                
                # Sombreado para mostrar región válida
                if ineq == "<=":
                    self.ax.fill_between(x, y, y_max, alpha=0.1, color=color)
                elif ineq == ">=":
                    self.ax.fill_between(x, y, y_min, alpha=0.1, color=color)
            
            else:  # Línea vertical
                x_line = c / a if abs(a) > 1e-10 else 0
                self.ax.axvline(x=x_line, color=color, linewidth=2, 
                              label=f'{a}X₁ {ineq} {c}')
        
        # Restricciones de no negatividad
        if self.noneg_var.get():
            self.ax.axhline(y=0, color='black', linewidth=1, linestyle='--', alpha=0.5)
            self.ax.axvline(x=0, color='black', linewidth=1, linestyle='--', alpha=0.5)
        
        # Colocar leyenda en la parte inferior para no interferir con la información
        self.ax.legend(bbox_to_anchor=(0.5, -0.1), loc='upper center', ncol=2)
    
    def dibujar_region_factible(self):
        """Dibuja la región factible sombreada"""
        if len(self.vertices) >= 3:
            # Ordenar vértices en sentido antihorario
            vertices_ordenados = self.ordenar_vertices_antihorario(self.vertices)
            
            # Crear polígono
            vertices_array = np.array(vertices_ordenados + [vertices_ordenados[0]])
            
            # Dibujar región factible
            self.ax.fill(vertices_array[:, 0], vertices_array[:, 1], 
                        alpha=0.3, color='lightblue', 
                        edgecolor='darkblue', linewidth=2,
                        label='Región Factible')
    
    def ordenar_vertices_antihorario(self, vertices):
        """Ordena los vértices en sentido antihorario desde el centro"""
        # Calcular centro
        cx = sum(v[0] for v in vertices) / len(vertices)
        cy = sum(v[1] for v in vertices) / len(vertices)
        
        # Calcular ángulo desde el centro para cada vértice
        def angulo(v):
            return np.arctan2(v[1] - cy, v[0] - cx)
        
        return sorted(vertices, key=angulo)
    
    def dibujar_vertices(self):
        """Dibuja los vértices de la región factible"""
        for i, (x, y) in enumerate(self.vertices):
            self.ax.plot(x, y, 'ko', markersize=8, zorder=5)
            
            # Etiqueta del vértice
            self.ax.annotate(f'V{i+1}({x:.2f}, {y:.2f})', 
                           xy=(x, y), xytext=(5, 5), 
                           textcoords='offset points',
                           bbox=dict(boxstyle='round,pad=0.3', fc='yellow', alpha=0.7),
                           fontsize=9)
        
        # Destacar solución óptima
        if self.solucion_optima:
            x_opt, y_opt = self.solucion_optima
            self.ax.plot(x_opt, y_opt, 'ro', markersize=12, zorder=6,
                        label=f'Solución Óptima: ({x_opt:.2f}, {y_opt:.2f})')
    
    def dibujar_funcion_objetivo(self, x_min, x_max, y_min, y_max):
        """Dibuja las líneas de la función objetivo"""
        if not self.solucion_optima:
            return
        
        c1, c2 = self.funcion_objetivo
        
        # Línea que pasa por la solución óptima
        x_opt, y_opt = self.solucion_optima
        valor_opt = c1 * x_opt + c2 * y_opt
        
        x = np.linspace(x_min, x_max, 100)
        
        if abs(c2) > 1e-10:
            y = (valor_opt - c1 * x) / c2
            self.ax.plot(x, y, 'r--', linewidth=3, alpha=0.8,
                        label=f'Función Objetivo: Z = {valor_opt:.2f}')
            
            # Dirección de crecimiento/decrecimiento
            arrow_x = x_opt
            arrow_y = y_opt
            
            # Vector gradiente (dirección de crecimiento)
            grad_x = c1
            grad_y = c2
            
            # Normalizar para la flecha
            norm = np.sqrt(grad_x**2 + grad_y**2)
            if norm > 0:
                grad_x /= norm
                grad_y /= norm
            
            if self.tipo_optimizacion == "max":
                self.ax.arrow(arrow_x, arrow_y, grad_x, grad_y, 
                             head_width=0.3, head_length=0.2, fc='red', ec='red',
                             label='Dirección de Maximización')
            else:
                self.ax.arrow(arrow_x, arrow_y, -grad_x, -grad_y, 
                             head_width=0.3, head_length=0.2, fc='red', ec='red',
                             label='Dirección de Minimización')
    
    def mostrar_informacion_solucion(self):
        """Muestra información detallada de la solución"""
        info_text = "INFORMACIÓN DE LA SOLUCIÓN\n"
        info_text += "="*30 + "\n\n"
        
        # Función objetivo
        c1, c2 = self.funcion_objetivo
        info_text += f"Función Objetivo: {'Maximizar' if self.tipo_optimizacion == 'max' else 'Minimizar'} Z = {c1}X₁ + {c2}X₂\n\n"
        
        # Restricciones
        info_text += "Restricciones:\n"
        for i, (a, b, ineq, c) in enumerate(self.restricciones, 1):
            info_text += f"{i}. {a}X₁ + {b}X₂ {ineq} {c}\n"
        
        if self.noneg_var.get():
            info_text += f"{len(self.restricciones)+1}. X₁, X₂ ≥ 0\n"
        
        # Vértices encontrados
        info_text += f"\nVértices de la región factible: {len(self.vertices)}\n"
        for i, (x, y) in enumerate(self.vertices, 1):
            valor_z = self.funcion_objetivo[0] * x + self.funcion_objetivo[1] * y
            info_text += f"V{i}: ({x:.3f}, {y:.3f}) → Z = {valor_z:.3f}\n"
        
        # Solución óptima
        if self.solucion_optima and self.valor_optimo is not None:
            x_opt, y_opt = self.solucion_optima
            info_text += f"\nSOLUCIÓN ÓPTIMA:\n"
            info_text += f"X₁* = {x_opt:.3f}\n"
            info_text += f"X₂* = {y_opt:.3f}\n"
            info_text += f"Z* = {self.valor_optimo:.3f}\n"
            
            # Puntos de corte con los ejes
            #info_text += f"\nPUNTOS DE CORTE:\n"
            #self.mostrar_puntos_corte(info_text)
        
        # Mostrar en una caja de texto posicionada correctamente
        self.ax.text(1.03, 0.98, info_text, transform=self.ax.transAxes, 
                    fontsize=9, verticalalignment='top', horizontalalignment='left',
                    bbox=dict(boxstyle='round,pad=0.5', facecolor='lightblue', alpha=0.9, edgecolor='navy'),
                    family='monospace')
    
    def mostrar_puntos_corte(self, info_base):
        """Calcula y muestra los puntos de corte de cada restricción con los ejes"""
        for i, (a, b, ineq, c) in enumerate(self.restricciones, 1):
            # Punto de corte con eje X₁ (cuando X₂ = 0)
            if abs(a) > 1e-10:
                x_corte = c / a
                corte_x = f"({x_corte:.2f}, 0)"
            else:
                corte_x = "No existe"
            
            # Punto de corte con eje X₂ (cuando X₁ = 0)
            if abs(b) > 1e-10:
                y_corte = c / b
                corte_y = f"(0, {y_corte:.2f})"
            else:
                corte_y = "No existe"
            
            print(f"Restricción {i}: X₁-intercepto: {corte_x}, X₂-intercepto: {corte_y}")
    
    def limpiar_grafico(self):
        """Limpia el gráfico actual"""
        for widget in self.graph_frame.winfo_children():
            widget.destroy()
        
        self.vertices = []
        self.solucion_optima = None
        self.valor_optimo = None
    
    def ejecutar(self):
        """Inicia la aplicación"""
        self.root.mainloop()

def main():
    """Función principal"""
    print("Iniciando Aplicación de Programación Lineal Interactiva...")
    print("="*50)
    print("CARACTERÍSTICAS:")
    print("• Interfaz gráfica intuitiva")
    print("• Ingreso de función objetivo (maximización/minimización)")
    print("• Múltiples restricciones con diferentes tipos (<=, >=, =)")
    print("• Cálculo automático de vértices de región factible")
    print("• Visualización gráfica completa")
    print("• Identificación de solución óptima")
    print("• Puntos de corte automáticos")
    print("="*50)
    
    app = ProgramacionLinealInteractiva()
    app.ejecutar()

if __name__ == "__main__":
    main()

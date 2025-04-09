import tkinter as tk
from tkinter import messagebox
from functools import reduce

# Colores personalizados
COLOR_FONDO = "#f0f4f8"
COLOR_TITULO = "#2c3e50"
COLOR_ETIQUETA = "#34495e"
COLOR_BOTON = "#2980b9"
COLOR_BOTON_TEXTO = "white"

# Aspectos a calificar
aspectos = [
    "Actividades",
    "Claridad del profesor",
    "Disponibilidad del profesor",
    "Relación teoría-práctica"
]

# Asignaturas
materias = [
    "Interacción y Diseño de Interfaces",
    "Programación Lógica y Funcional",
    "Administración de Redes"
]

calificaciones = {}

def promedio(lista):
    return reduce(lambda x, y: x + y, lista) / len(lista) if lista else 0

def suma(lista):
    if not lista:
        return 0
    return lista[0] + suma(lista[1:])

ventana = tk.Tk()
ventana.title("Encuesta de Evaluación de Asignaturas")
ventana.configure(bg=COLOR_FONDO)

etiquetas_entries = {}

def guardar_respuestas():
    try:
        for materia in materias:
            respuestas = []
            for asp in aspectos:
                valor = etiquetas_entries[(materia, asp)].get()
                if not valor.isdigit() or not (1 <= int(valor) <= 10):
                    raise ValueError(f"Valor inválido para '{asp}' en '{materia}'. Usa números del 1 al 10.")
                respuestas.append(int(valor))
            calificaciones[materia] = respuestas
        mostrar_resultados()
    except ValueError as e:
        messagebox.showerror("Error de entrada", str(e))

def mostrar_resultados():
    resultados = tk.Toplevel()
    resultados.title("Resultados de la Encuesta")
    resultados.configure(bg=COLOR_FONDO)

    for materia in materias:
        notas = calificaciones.get(materia, [])
        prom = promedio(notas)
        total = suma(notas)
        tk.Label(resultados, text=f"{materia} - Promedio: {prom:.2f}, Total: {total}",
                 bg=COLOR_FONDO, fg=COLOR_ETIQUETA, font=("Arial", 11)).pack(pady=2)

# Construcción de la interfaz 
for materia in materias:
    tk.Label(ventana, text=f"Materia: {materia}", font=("Arial", 12, "bold"),
             bg=COLOR_FONDO, fg=COLOR_TITULO).pack(pady=(10, 0))
    for asp in aspectos:
        tk.Label(ventana, text=f"{asp}:", bg=COLOR_FONDO, fg=COLOR_ETIQUETA).pack()
        entry = tk.Entry(ventana)
        entry.pack(pady=2)
        etiquetas_entries[(materia, asp)] = entry

tk.Button(ventana, text="Enviar Encuesta", command=guardar_respuestas,
          bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, padx=10, pady=5).pack(pady=15)

ventana.mainloop()

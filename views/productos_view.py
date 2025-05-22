import tkinter as tk
from services.my_sql import conectar

def cargar_productos(ventana):
    productos_panel = tk.Frame(ventana, bg="gray", padx=0, pady=0, width=8000, height=1000)
    productos_panel.pack()

    titulo = tk.Label(productos_panel, text="Productos", font=("Arial", 14, "bold"), bg="gray")
    titulo.pack(pady=10)

    # Corregir la consulta SQL (usar "nombre" en lugar de "nombres")
    resultados = conectar("SELECT nombre FROM productos")  

    if resultados:
        # Crear un contenedor para organizar los nombres
        contenedor = tk.Frame(productos_panel, bg="gray")
        contenedor.pack()

        # Iterar sobre cada resultado y extraer el primer elemento de la tupla
        for producto in resultados:
            nombre = producto[0]  # <<< Acceder al primer elemento
            etiqueta = tk.Label(contenedor, text=nombre, bg="gray", font=("Arial", 12))
            etiqueta.pack(anchor="w", padx=20)
    else:
        mensaje = tk.Label(productos_panel, text="No hay productos", bg="gray")
        mensaje.pack()

    print("Panel productos cargado")
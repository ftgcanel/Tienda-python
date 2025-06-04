import tkinter as tk
from services.my_sql import conectar

def cargar_productos(ventana):
    productos_panel = tk.Frame(ventana, bg="#a8b9cf", padx=10, pady=10, width=8000, height=1000)
    productos_panel.pack(fill="both", expand=True)

    titulo = tk.Label(
        productos_panel,
        text="📦 Productos", font=("Helvetica", 16, "bold"),bg="#f0f0f0",fg="#333")
    titulo.pack(pady=(0, 20))

    # Consulta SQL
    resultados = conectar("SELECT nombre FROM productos")  

    if resultados:
        # Crear un contenedor para organizar los nombres
        contenedor = tk.Frame(productos_panel, bg="#ffffff", bd=2, relief="groove")
        contenedor.pack(padx=20, pady=10, fill="x")

        for producto in resultados:
            nombre = producto[0]
            etiqueta = tk.Label(contenedor,text=f"- {nombre}",bg="#ffffff",font=("Helvetica", 12),anchor="w",padx=10,pady=5)
            etiqueta.pack(fill="x")
    else:
        mensaje = tk.Label(
            productos_panel,text="No hay productos disponibles.",bg="#f0f0f0",fg="red",font=("Helvetica", 12, "italic"))
        mensaje.pack(pady=10)
    print("Panel productos cargado")
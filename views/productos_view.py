import tkinter as tk
from services.manipular_sql import manipular

def cargar_productos(frame_contenedor):
    for widget in frame_contenedor.winfo_children():
        widget.destroy()
        # Configuración de estilos
    BG_COLOR = "#ffffff"
    HEADER_BG = "#333333"
    HEADER_FG = "white"
    ROW_BG1 = "#f0f0f0"
    ROW_BG2 = "#e0e0e0"
    FONT_HEADER = ("Arial", 10, "bold")
    FONT_ROW = ("Arial", 10)



    productos_panel = tk.Frame(frame_contenedor,bg="#ffffff")
    productos_panel.pack(fill="both", expand=True)

    titulo = tk.Label(productos_panel, text="📦 Lista de Productos", 
             font=("Arial", 14, "bold"), bg=BG_COLOR, fg="#333333")
    titulo.pack(pady=(0, 10), anchor="w")
    categorias_map = {
    1: "Laptops",
    2: "Periféricos",
    3: "Audio",
    4: "Almacenamiento",
    5: "Teléfonos"
}

     # Realizar consulta
    resultados = manipular(
        "SELECT p.nombre, p.precio, p.cantidad, c.nombre AS categoria_id "
        "FROM productos p "
        "JOIN categorias c ON p.categoria_id = c.id"
    )

    if resultados:
        # Crear tabla con encabezados
        tabla_frame = tk.Frame(productos_panel, bg=HEADER_BG, bd=1, relief="solid")
        tabla_frame.pack(fill="x", padx=10, pady=10)
        
        # Encabezados
        encabezados = ["Nombre", "Precio", "Cantidad", "Categoría"]
        for col, texto in enumerate(encabezados):
            header = tk.Label(
                tabla_frame,
                text=texto,
                font=FONT_HEADER,
                bg=HEADER_BG,
                fg=HEADER_FG,
                padx=10,
                pady=5,
                width=20 if col == 0 else 10,
                anchor="w" if col == 0 else "e" if col == 1 else "center"
            )
            header.grid(row=0, column=col, sticky="ew")

        # Filas de datos
        for row_idx, (nombre, precio, cantidad, categoria) in enumerate(resultados):
            row_bg = ROW_BG1 if row_idx % 2 == 0 else ROW_BG2
            fila = tk.Frame(productos_panel, bg=row_bg)
            fila.pack(fill="x", padx=10, pady=(0, 1))
            
            # Nombre
            tk.Label(
                fila, 
                text=nombre, 
                font=FONT_ROW, 
                bg=row_bg, 
                padx=10,
                pady=5,
                width=20,
                anchor="w"
            ).pack(side="left")
            
            # Precio
            tk.Label(
                fila, 
                text=f"Q.{float(precio):.2f}", 
                font=FONT_ROW, 
                bg=row_bg, 
                padx=10,
                pady=5,
                width=10,
                anchor="e"
            ).pack(side="left")
            
            # Cantidad
            tk.Label(
                fila, 
                text=str(cantidad), 
                font=FONT_ROW, 
                bg=row_bg, 
                padx=10,
                pady=5,
                width=10,
                anchor="center"
            ).pack(side="left")
            
            # Categoría
            tk.Label(
                fila, 
                text=categoria, 
                font=FONT_ROW, 
                bg=row_bg, 
                padx=10,
                pady=5,
                width=20,
                anchor="w"
            ).pack(side="left", fill="x", expand=True)

    else:
        tk.Label(productos_panel, text="No hay productos registrados", 
                 font=("Arial", 12), bg=BG_COLOR).pack(pady=20)

    print("Panel productos cargado")
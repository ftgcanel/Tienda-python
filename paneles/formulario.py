import tkinter as tk
from tkinter import messagebox
from services.manipular_sql import manipular

def formulario(frame_padre, actualizar_productos):
    BG_COLOR = "#f0f0f0"
    LABEL_FONT = ("Arial", 10, "bold")
    ENTRY_FONT = ("Arial", 10)
    BUTTON_BG = "#4CAF50"  # Verde
    BUTTON_FG = "white"

    panel_izquierdo = tk.Frame(frame_padre, bg=BG_COLOR, padx=20, pady=20)    
    panel_izquierdo.pack(side="left", fill="y")

    marco_formulario = tk.LabelFrame(
        panel_izquierdo, 
        text="Formulario Producto", 
        font=("Arial", 12, "bold"),
        bg=BG_COLOR,
        padx=10,
        pady=10
    )
    marco_formulario.pack(fill="both", expand=True, pady=(0, 10))
    row = 0
    tk.Label(marco_formulario, text="Nombre:", font=LABEL_FONT, bg=BG_COLOR, anchor="w").grid(row=row, column=0, sticky="w", pady=(5, 2))
    entry_nombre = tk.Entry(marco_formulario, font=ENTRY_FONT, width=25)
    entry_nombre.grid(row=row, column=1, sticky="ew", pady=(5, 2), padx=(0, 10))
    row += 1

    tk.Label(marco_formulario, text="Precio:", font=LABEL_FONT, bg=BG_COLOR, anchor="w").grid(row=row, column=0, sticky="w", pady=2)
    entry_precio = tk.Entry(marco_formulario, font=ENTRY_FONT, width=25)
    entry_precio.grid(row=row, column=1, sticky="ew", pady=2, padx=(0, 10))
    row += 1

    tk.Label(marco_formulario, text="Cantidad:", font=LABEL_FONT, bg=BG_COLOR, anchor="w").grid(row=row, column=0, sticky="w", pady=2)
    entry_cantidad = tk.Entry(marco_formulario, font=ENTRY_FONT, width=25)
    entry_cantidad.grid(row=row, column=1, sticky="ew", pady=2, padx=(0, 10))
    row += 1

    tk.Label(marco_formulario, text="Categoría:", font=LABEL_FONT, bg=BG_COLOR, anchor="w").grid(row=row, column=0, sticky="w", pady=2)

    categorias = ["Laptops", "Periféricos", "Audio", "Almacenamiento", "Teléfonos"]
    categoria_map = {"Laptops": 1,"Periféricos": 2,"Audio": 3, "Almacenamiento": 4,"Teléfonos": 5}

    # Variable para almacenar la selección
    categoria_seleccionada = tk.StringVar(panel_izquierdo)
    categoria_seleccionada.set("")  # Valor por defecto
    dropdown_frame = tk.Frame(marco_formulario, bg=BG_COLOR)
    dropdown_frame.grid(row=row, column=1, sticky="ew", pady=2, padx=(0, 10))
    
    dropdown_categoria = tk.OptionMenu(dropdown_frame,categoria_seleccionada,*categorias)
    
    dropdown_categoria.config(font=ENTRY_FONT, width=22, anchor="w")
    dropdown_categoria.pack(fill="x")
    
    # Menú desplegable
    dropdown_categoria = tk.OptionMenu(
        panel_izquierdo,
        categoria_seleccionada,
        *categorias)
    


    def guardar_producto():
        nombre_val = entry_nombre.get()
        precio_val = entry_precio.get()
        cantidad_val = entry_cantidad.get()
        categoria_nombre = categoria_seleccionada.get()
        try:
            precio_float = float(precio_val)
            cantidad_int = int(cantidad_val)
            categoria_id = categoria_map[categoria_nombre]
        except ValueError:
            messagebox.showerror("Error de datos")
            return

        sql = "INSERT INTO productos (nombre, precio, cantidad, categoria_id) VALUES (%s, %s, %s, %s)"
        datos = (nombre_val, precio_float, cantidad_int, categoria_id)
        resultado = manipular(sql, datos)

        if resultado is not None:
            messagebox.showinfo("Éxito", "Producto guardado correctamente.")
            entry_nombre.delete(0, tk.END)
            entry_precio.delete(0, tk.END)
            entry_cantidad.delete(0, tk.END)
            categoria_seleccionada.set(categorias[0])
            actualizar_productos()  # ✅ Recargar productos
        else:
            messagebox.showerror("Error", "No se pudo guardar el producto.")

    tk.Button(panel_izquierdo, text="Guardar", command=guardar_producto).pack(pady=10)




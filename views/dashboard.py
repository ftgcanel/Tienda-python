import tkinter as tk
from paneles.productos_view import cargar_productos
from paneles.formulario import formulario

def ventana_usuario(datos):
    ventana_usuario = tk.Tk()
    ventana_usuario.title("Ventana usuario")
    ventana_usuario.state("zoomed")
    ventana_usuario.configure(bg="#f0f0f0")

    panel_derecho = tk.Frame(ventana_usuario, bg="#ffffff")
    panel_derecho.pack(side="right", fill="both", expand=True, padx=(10, 0))

    formulario(ventana_usuario, lambda: cargar_productos(panel_derecho))

    cargar_productos(panel_derecho)

    ventana_usuario.mainloop()



import tkinter as tk
from paneles.productos_view import cargar_productos
from paneles.formulario import formulario

def ventana_usuario(datos):
    ventana_usuario = tk.Tk()
    ventana_usuario.title("Ventana usuario")
    ventana_usuario.state("zoomed")
    ventana_usuario.configure(bg="#f0f0f0")

    # Contenedor principal
    frame_principal = tk.Frame(ventana_usuario)
    frame_principal.pack(fill="both", expand=True)

    panel_derecho = tk.Frame(frame_principal,bg="#ffffff")
    panel_derecho.pack(side="right", fill="both", expand=True, padx=(10, 0))

    # Pasar la función de recargar
    formulario(frame_principal, lambda: cargar_productos(panel_derecho))

    cargar_productos(panel_derecho)

    ventana_usuario.mainloop()


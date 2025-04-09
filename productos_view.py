import tkinter as tk
def cargar_productos(ventana):
    productos_panel = tk.Frame(ventana, bg="gray", padx=0,pady=0,width=1000,height=500)
    productos_panel.pack()

    print("Panel productos cargado")
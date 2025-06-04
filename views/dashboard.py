import tkinter as tk
from views.productos_view import cargar_productos

def ventana_usuario(datos):
    ventana_usuario =  tk.Tk()
    ventana_usuario.title("Ventana usuario")
    ventana_usuario.geometry("1100x1100")    
    cargar_productos(ventana_usuario)
    ventana_usuario.mainloop()


import tkinter as tk
from views.header_view import cargar_header
from views.productos_view import cargar_productos

ventana = tk.Tk()
ventana.title("Mi tienda")
ventana.geometry("800x500")

cargar_header(ventana)
cargar_productos(ventana)

ventana.mainloop()
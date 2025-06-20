import tkinter as tk
from views.header_view import cargar_header
from views.productos_view import cargar_productos
from views.login_view import cargar_login
from views.dashboard import ventana_usuario
# ventana de la aplicación
ventana = tk.Tk()
ventana.title("Mi tienda")
ventana.geometry("800x500")

#modulos
cargar_login(ventana)


ventana.mainloop()
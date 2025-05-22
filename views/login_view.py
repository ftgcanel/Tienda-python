import tkinter as tk
from services.my_sql import conectar

def cargar_login(ventana):
    login_panel = tk.Frame(
        ventana,
        bg = "grey",
        padx = 0,
        pady = 0,
        width = 1000,
        height = 540,
        )
    
# Formulario
    titulo = tk.Label(login_panel, text="Login")
    titulo.pack()

# Correo
    correo = tk.Label(login_panel, text="Correo")
    correo.pack()

# Entrada correo# Correo
    entrada_correo = tk.Entry(login_panel)
    entrada_correo.pack()

#Contraseña
    contraseña = tk.Label(login_panel, text="Contraseña")
    contraseña.pack()

# Entrada contraseña
    entrada_contraseña = tk.Entry(login_panel)
    entrada_contraseña.pack()

# Botón ingresar

    def funcion_boton():
        datocorreo = entrada_correo.get()
        print(datocorreo)
        datocontraseña = entrada_contraseña.get()
        print(conectar("SHOW TABLES"))


    boton = tk.Button(login_panel, text="Continuar", command=funcion_boton)
    boton.pack()


    login_panel.pack()
    print("panel login cargado")


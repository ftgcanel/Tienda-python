import tkinter as tk

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

# Entrada correo
    entrada_correo = tk.Entry(login_panel)
    entrada_correo.pack()

#Contraseña
    contraseña = tk.Label(login_panel, text="Contraseña")
    contraseña.pack()

# Entrada contraseña
    entrada_contraseña = tk.Entry(login_panel)
    entrada_contraseña.pack()

# Botón ingresar
    boton = tk.Button(login_panel, text="Continuar")
    boton.pack()

    def funcion_boton():
        print("hola")


    login_panel.pack()
    print("panel login cargado")


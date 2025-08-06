import tkinter as tk
from services.my_sql import conectar
from views.dashboard import ventana_usuario 

def cargar_login(ventana):
    login_panel = tk.Frame(
        ventana,
        bg="#f0f0f0",
        padx=20,
        pady=20,
        width=1000,
        height=540,
    )
    
    # Título
    titulo = tk.Label(
        login_panel, 
        text="Login", 
        font=("Helvetica", 20, "bold"),
        bg="#f0f0f0",
        fg="#333"
    )
    titulo.pack(pady=(10, 30))

    # Correo
    correo = tk.Label(
        login_panel, 
        text="Correo:", 
        font=("Helvetica", 12),
        bg="#f0f0f0",
        anchor="w"
    )
    correo.pack(fill="x")

    entrada_correo = tk.Entry(
        login_panel, 
        font=("Helvetica", 12),
        relief="solid",
        borderwidth=1
    )
    entrada_correo.pack(fill="x", pady=(0, 15))

    # Contraseña
    contraseña = tk.Label(
        login_panel, 
        text="Contraseña:", 
        font=("Helvetica", 12),
        bg="#f0f0f0",
        anchor="w"
    )
    contraseña.pack(fill="x")

    entrada_contraseña = tk.Entry(
        login_panel, 
        font=("Helvetica", 12), 
        show="*", 
        relief="solid",
        borderwidth=1
    )
    entrada_contraseña.pack(fill="x", pady=(0, 25))

    # Botón ingresar
    def funcion_boton():
        correo = entrada_correo.get()
        datocontraseña = entrada_contraseña.get()
        consultar_usuario = conectar(f"SELECT * FROM usuario WHERE correo = '{correo}' AND contrasena = '{datocontraseña}'")

        if len(consultar_usuario) != 0:
            print("Usuario activo")
            ventana.destroy()
            print(consultar_usuario[0][3])
            ventana_usuario(consultar_usuario)
        else:
            print("Datos incorrectos") 

    boton = tk.Button(
        login_panel, 
        text="Continuar", 
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50", 
        fg="white", 
        padx=10, 
        pady=5,
        command=funcion_boton,
        activebackground="#45a049",relief="flat")
    boton.pack()

    login_panel.pack(expand=True)
    print("panel login cargado")
    return login_panel


import tkinter as tk

def cargar_header(ventana):
    header_panel = tk.Frame(ventana, bg="lightgray", padx=0,pady=0,width=1000,height=100)
    header_panel.pack()

    print("Panel header cargado")
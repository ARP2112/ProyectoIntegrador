from tkinter import Tk, Button, Frame
import tkinter as tk
from tkinter import *

def Requisiciones():
    ventana1 = Tk()
    ventana1.title("REQUISICIONES")
    ventana1.geometry("600x300")

    seccion1 = Frame(ventana1, bg = "#e6e6ff")
    seccion1.pack(expand = True, fill = 'both')

    requisicion = tk.StringVar()
    label1=tk.Label(seccion1, text="Requisición:")
    label1.place (x=400, y=30)
    requisicion1 = Entry(seccion1, width=15, textvariable = requisicion)
    requisicion1.place(x=480, y = 30)

    fecha = tk.StringVar()
    label2=tk.Label(seccion1, text="Fecha:")
    label2.place (x=400, y=70)
    fecha1 = Entry(seccion1, width=20, textvariable = fecha)
    fecha1.place(x=460, y = 70)
    
    partida = tk.StringVar()
    label3=tk.Label(seccion1, text="Partida:")
    label3.place (x=20, y=100)
    partida1 = Entry(seccion1, width=10, textvariable = partida)
    partida1.place(x=70, y = 100)
    
    cantidad = tk.StringVar()
    label4=tk.Label(seccion1, text="Cantidad:")
    label4.place (x=20, y=130)
    cantidad1 = Entry(seccion1, width=10, textvariable = cantidad)
    cantidad1.place(x=90, y = 130)
    
    descripcion = tk.StringVar()
    label5=tk.Label(seccion1, text="Descripción:")
    label5.place (x=20, y=160)
    descripcion1 = Entry(seccion1, width=50, textvariable = descripcion)
    descripcion1.place(x=110, y = 160)
    
    area = tk.StringVar()
    label6=tk.Label(seccion1, text="Área del solicitante:")
    label6.place (x=20, y=190)
    area1 = Entry(seccion1, width=50, textvariable = area)
    area1.place(x=140, y = 190)
    
    botonGuardar = Button(seccion1, text = "Guardar", fg = "white", bg = "gray")
    botonGuardar.place(x=40, y=240, width = 100, height = 30)
    
    botonEnviar = Button(seccion1, text = "Enviar", fg = "white", bg = "gray")
    botonEnviar.place(x=240, y=240, width = 100, height = 30)
    
    botonReenviar = Button(seccion1, text = "Reenviar", fg = "white", bg = "gray")
    botonReenviar.place(x=440, y=240, width = 100, height = 30)

    ventana1.mainloop()
    
def Cotizaciones():
    def Proveedores():
        ventana3 = Tk()
        ventana3.title("PROVEEDORES")
        ventana3.geometry("450x300")
        
        seccion3 = Frame(ventana3, bg = "#e6e6ff")
        seccion3.pack(expand = True, fill = 'both')
        
        nombre = tk.StringVar()
        label1=tk.Label(seccion3, text="Nombre:")
        label1.place (x=20, y=40)
        nombre1 = Entry(seccion3, width=25, textvariable = nombre)
        nombre1.place(x=80, y = 40)
        
        apellidoP = tk.StringVar()
        label2=tk.Label(seccion3, text="Apellido Paterno:")
        label2.place (x=20, y=80)
        apellidoP1 = Entry(seccion3, width=25, textvariable = apellidoP)
        apellidoP1.place(x=120, y = 80)
        
        apellidoM = tk.StringVar()
        label3=tk.Label(seccion3, text="Apellido Materno:")
        label3.place (x=20, y=120)
        apellidoM1 = Entry(seccion3, width=25, textvariable = apellidoM)
        apellidoM1.place(x=120, y = 120)
        
        rfc = tk.StringVar()
        label4=tk.Label(seccion3, text="RFC:")
        label4.place (x=20, y=160)
        rfc1 = Entry(seccion3, width=25, textvariable = rfc)
        rfc1.place(x=50, y = 160)
        
        empresa = tk.StringVar()
        label5=tk.Label(seccion3, text="Empresa:")
        label5.place (x=20, y=200)
        empresa1 = Entry(seccion3, width=25, textvariable = empresa)
        empresa1.place(x=75, y = 200)
        
        botonAceptar1 = Button(seccion3, text = "Aceptar", fg = "white", bg = "gray")
        botonAceptar1.place(x=320, y=240, width = 100, height = 30)
        
        ventana3.mainloop()
        
        
    ventana2 = Tk()
    ventana2.title("COTIZACIONES")
    ventana2.geometry("600x300")

    seccion2 = Frame(ventana2, bg = "#e6e6ff")
    seccion2.pack(expand = True, fill = 'both')
    
    nCot = tk.StringVar()
    label1=tk.Label(seccion2, text="N° de cotización:")
    label1.place (x=380, y=30)
    nCot1 = Entry(seccion2, width=15, textvariable = nCot)
    nCot1.place(x=480, y = 30)
    
    fecha2 = tk.StringVar()
    label2=tk.Label(seccion2, text="Fecha:")
    label2.place (x=20, y=90)
    fecha3 = Entry(seccion2, width=25, textvariable = fecha2)
    fecha3.place(x=70, y = 90)
    
    partida2 = tk.StringVar()
    label3=tk.Label(seccion2, text="Partida:")
    label3.place (x=20, y=120)
    partida3 = Entry(seccion2, width=10, textvariable = partida2)
    partida3.place(x=70, y = 120)
    
    cantidad2 = tk.StringVar()
    label4=tk.Label(seccion2, text="Cantidad:")
    label4.place (x=20, y=150)
    cantidad3 = Entry(seccion2, width=10, textvariable = cantidad2)
    cantidad3.place(x=90, y = 150)
    
    descripcion2 = tk.StringVar()
    label5=tk.Label(seccion2, text="Descripción:")
    label5.place (x=20, y=180)
    descripcion3 = Entry(seccion2, width=50, textvariable = descripcion2)
    descripcion3.place(x=110, y = 180)
    
    botonAceptar = Button(seccion2, text = "Aceptar", fg = "white", bg = "gray")
    botonAceptar.place(x=40, y=240, width = 100, height = 30)
    
    botonProveedores = Button(seccion2, text = "PROVEEDORES", fg = "white", bg = "gray", command = Proveedores)
    botonProveedores.place(x=470, y=240, width = 100, height = 30)
    
    ventana2.mainloop()
    
    
ventana = Tk()
ventana.title("INICIO")
ventana.geometry("300x200")

seccion = Frame(ventana, bg = "#e6e6ff")
seccion.pack(expand = True, fill = 'both')

botonRequi = Button(seccion, text = "Requisición", fg = "white", bg = "gray", command = Requisiciones)
botonRequi.place(x=100, y=60, width = 100, height = 30)

botonCot = Button(seccion, text = "Cotización", fg = "white", bg = "gray", command = Cotizaciones)
botonCot.place(x=100, y=110, width = 100, height = 30)

ventana.mainloop()
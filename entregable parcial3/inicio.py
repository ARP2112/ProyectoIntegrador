from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorRequisiciones import *

controladorR = controladorRequi()

def GuardarRequi():
    controladorR.GuardarRequisicion(varRequi.get(), varFecha.get(), varPartida.get(), varCantidad.get(), varDescr.get(), varASolicitante.get())

Ventana = Tk()
Ventana.title("REQUISICIONES")
Ventana.geometry("500x350")

panel = ttk.Notebook(Ventana)
panel.pack(fill = 'both', expand = 'yes')

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)

varRequi = tk.StringVar()
varFecha = tk.StringVar()
varPartida = tk.StringVar()
varCantidad = tk.StringVar()
varDescr = tk.StringVar()
varASolicitante = tk.StringVar()

titulo = Label(pestana1, text = "Requisiciones", fg = "blue", font = ("Modern", 18)). pack()
lblRequi = Label(pestana1, text = "Requisicion:").pack()
txtRequi = Entry(pestana1, textvariable = varRequi).pack()

lblFecha = Label(pestana1, text = "Fecha:").pack()
txtFecha = Entry(pestana1, textvariable = varFecha).pack()

lblPartida = Label(pestana1, text = "Partida:").pack()
txtPartida = Entry(pestana1, textvariable = varPartida).pack()

lblCantidad = Label(pestana1, text = "Cantidad:").pack()
txtCantidad = Entry(pestana1, textvariable = varCantidad).pack()

lblDescr = Label(pestana1, text = "Descripción:").pack()
txtDescr = Entry(pestana1, textvariable = varDescr).pack()

lblASoli = Label(pestana1, text = "Área del solicitante:").pack()
txtASoli = Entry(pestana1, textvariable = varASolicitante).pack()

btnGuardar = Button(pestana1, text = "Guardar requisición", command = GuardarRequi).pack()

panel.add(pestana1, text = 'Formulario')
panel.add(pestana2, text = 'Buscar Requisición')
panel.add(pestana3, text = 'Consultar Requisición')
panel.add(pestana4, text = 'Actualizar Requisición')

Ventana.mainloop()
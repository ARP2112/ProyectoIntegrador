from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorRequisiciones import *

controladorR = controladorRequi()

def GuardarRequi():
    controladorR.GuardarRequisicion(varRequi.get(), varFecha.get(), varPartida.get(), varCantidad.get(), varDescr.get(), varASolicitante.get())
    
def BuscarRequi():
    buscar = controladorR.consultarRequi(varIDCon.get())
    if (buscar):
        for usu in buscar:
            tabla.delete(*tabla.get_children())
            tabla.insert("", "end", text = usu[0], values = (usu[1], usu[2], usu[3], usu[4], usu[5], usu[6]))
    else:
        messagebox.showwarning ("No encontrado", "La requisición no existe en la base de datos", icon = "error")
        
def ConsultarRequi():
    
    bus = controladorR.consultarTodosLosUsuarios()
    tabla1.delete(*tabla1.get_children()) #limpia
    for usu in bus:
        tabla1.insert("", "end", text = usu[0], values = (usu[1], usu[2], usu[3], usu[4], usu[5], usu[6]))

def EliminarRequi():
    msg = messagebox.askquestion("Warning", "¿Está seguro de eliminar la requisición?")
    if (msg == "no"):
        messagebox.showinfo("No eliminado", "Requisición no eliminada")
    else:
        controladorR.EliminarRequi(varDelete.get())
        messagebox.showinfo("Eliminado exitoso", "Requisición eliminada")
        
def ActualizarRequi():
    controladorR.ActualizarRequiNum(varID.get(), varRequi1.get())
    

def ActualizarFecha():
    controladorR.ActualizarFecha(varID.get(), varFecha1.get())
    

def ActualizarPartida():
    controladorR.ActualizarPartida(varID.get(), varPartida1.get())
    
    
def ActualizarCantidad():
    controladorR.ActualizarCantidad(varID.get(), varCantidad1.get())
    

def ActualizarDescr():
    controladorR.ActualizarDescr(varID.get(), varDescr1.get())
    

def ActualizarASoli():
    controladorR.ActualizarASoli(varID.get(), varASolicitante1.get())

Ventana = Tk()
Ventana.title("REQUISICIONES")
Ventana.geometry("800x500")

panel = ttk.Notebook(Ventana)
panel.pack(fill = 'both', expand = 'yes')

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestana5 = ttk.Frame(panel)

#PESTAÑA 1

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

#PESTAÑA 2

varIDCon = tk.StringVar()
titulo = Label(pestana2, text = "Consultar requisición", fg = "blue", font = ("Modern", 18)). pack()
lblID = Label(pestana2, text = "ID de requisicion:").pack()
txtID = Entry(pestana2, textvariable = varIDCon).pack()
btnBusqueda = Button(pestana2, text = "Buscar", command = BuscarRequi).pack()
subID = Label(pestana2, text = "Registrado:", fg = "blue", font = ("Modern",15)).pack()
tabla = ttk.Treeview (pestana2)
tabla ["columns"] = ("Requisición", "Fecha", "Partida", "Cantidad", "Descripción", "Área solicitante")
tabla.column("#0", width = 60, minwidth = 60)
tabla.column("Requisición", width = 100, minwidth = 60)
tabla.column("Fecha", width = 200, minwidth = 110)
tabla.column("Partida", width = 100, minwidth = 60)
tabla.column("Cantidad", width = 100, minwidth = 60)
tabla.column("Descripción", width = 100, minwidth = 200)
tabla.column("Área solicitante", width = 100, minwidth = 200)
tabla.heading("#0", text = "ID", anchor = tk.CENTER)
tabla.heading("Requisición", text = "Requisición", anchor = tk.CENTER)
tabla.heading("Fecha", text = "Fecha", anchor = tk.CENTER)
tabla.heading("Partida", text = "Partida", anchor = tk.CENTER)
tabla.heading("Cantidad", text = "Cantidad", anchor = tk.CENTER)
tabla.heading("Descripción", text = "Descripción", anchor = tk.CENTER)
tabla.heading("Área solicitante", text = "Área solicitante", anchor = tk.CENTER)
tabla.pack()

# PESTAÑA 3
titulo = Label(pestana3, text = "Consultar requisición", fg = "blue", font = ("Modern", 18)). pack()
subID1 = Label(pestana3, text = "Registrados:", fg = "blue", font = ("Modern",15)).pack()
tabla1 = ttk.Treeview (pestana3)
tabla1 ["columns"] = ("Requisición", "Fecha", "Partida", "Cantidad", "Descripción", "Área solicitante")
tabla1.column("#0", width = 60, minwidth = 60)
tabla1.column("Requisición", width = 100, minwidth = 60)
tabla1.column("Fecha", width = 200, minwidth = 110)
tabla1.column("Partida", width = 100, minwidth = 60)
tabla1.column("Cantidad", width = 100, minwidth = 60)
tabla1.column("Descripción", width = 100, minwidth = 200)
tabla1.column("Área solicitante", width = 100, minwidth = 200)
tabla1.heading("#0", text = "ID", anchor = tk.CENTER)
tabla1.heading("Requisición", text = "Requisición", anchor = tk.CENTER)
tabla1.heading("Fecha", text = "Fecha", anchor = tk.CENTER)
tabla1.heading("Partida", text = "Partida", anchor = tk.CENTER)
tabla1.heading("Cantidad", text = "Cantidad", anchor = tk.CENTER)
tabla1.heading("Descripción", text = "Descripción", anchor = tk.CENTER)
tabla1.heading("Área solicitante", text = "Área solicitante", anchor = tk.CENTER)
tabla1.pack()
btnBusqueda = Button(pestana3, text = "Buscar", command = ConsultarRequi).pack()

# PESTAÑA 4

varID = tk.StringVar()
varRequi1 = tk.StringVar()
varFecha1 = tk.StringVar()
varPartida1 = tk.StringVar()
varCantidad1 = tk.StringVar()
varDescr1 = tk.StringVar()
varASolicitante1 = tk.StringVar()

titulo4 = Label(pestana4, text = "Actualizar usuarios", fg = "blue", font = ("Modern", 18)). pack()
lblID2 = Label(pestana4, text = "ID requisición:").pack()
txtID2 = Entry(pestana4, textvariable = varID).pack()
lblRequi1 = Label(pestana4, text = "Requisicion:").pack()
txtRequi1 = Entry(pestana4, textvariable = varRequi1).pack()
btnRequi1 = Button(pestana4, text = "Actualizar número requisición", command = ActualizarRequi).pack()
lblFecha1 = Label(pestana4, text = "Fecha:").pack()
txtFecha1 = Entry(pestana4, textvariable = varFecha1).pack()
btnFecha1 = Button(pestana4, text = "Actualizar fecha", command = ActualizarFecha).pack()
lblPartida1 = Label(pestana4, text = "Partida:").pack()
txtPartida1 = Entry(pestana4, textvariable = varPartida1).pack()
btnPartida1 = Button(pestana4, text = "Actualizar partida", command = ActualizarPartida).pack()
lblCantidad1 = Label(pestana4, text = "Cantidad:").pack()
txtCantidad1 = Entry(pestana4, textvariable = varCantidad1).pack()
btnCantidad1 = Button(pestana4, text = "Actualizar cantidad", command = ActualizarCantidad).pack()
lblDescr1 = Label(pestana4, text = "Descripción:").pack()
txtDescr1 = Entry(pestana4, textvariable = varDescr1).pack()
btnDescr1 = Button(pestana4, text = "Actualizar descripción", command = ActualizarDescr).pack()
lblASoli1 = Label(pestana4, text = "Área del solicitante:").pack()
txtASoli1 = Entry(pestana4, textvariable = varASolicitante1).pack()
btnASoli1 = Button(pestana4, text = "Actualizar área solicitante", command = ActualizarASoli).pack()

# PESTAÑA 5

varDelete = tk.StringVar()
titulo5 = Label(pestana5, text = "Eliminar requisición", fg = "blue", font = ("Modern", 18)). pack()
lblID2 = Label(pestana5, text = "Identificador de requisición:").pack()
txtID2 = Entry(pestana5, textvariable = varDelete).pack()
btnEliminar = Button(pestana5, text = "Eliminar", command = EliminarRequi).pack()


panel.add(pestana1, text = 'Formulario')
panel.add(pestana2, text = 'Buscar Requisición')
panel.add(pestana3, text = 'Consultar Requisiciones')
panel.add(pestana4, text = 'Actualizar Requisición')
panel.add(pestana5, text = 'Eliminar Requisición')

Ventana.mainloop()
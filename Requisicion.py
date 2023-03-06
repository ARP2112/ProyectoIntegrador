from tkinter import Tk, Button, Frame
import tkinter as tk
from tkinter import *

ventana = Tk()
ventana.title("REQUISICIONES")
ventana.geometry("800x500")

seccion1 = Frame(ventana, bg = "#e6e2da")
seccion1.pack(expand = True, fill = 'both')

requisicion = tk.StringVar()
label1=tk.Label(seccion1, text="Requisición:")
label1.place (x=540, y=40)
requisicion = Entry(seccion1, width=15, textvariable = requisicion)
requisicion.place(x=620, y = 40)

fecha = tk.StringVar()
label1=tk.Label(seccion1, text="Fecha:")
label1.place (x=565, y=70)
fecha = Entry(seccion1, width=20, textvariable = fecha)
fecha.place(x=620, y = 70)

ventana.mainloop()
from tkinter import messagebox
import sqlite3

class controladorRequi:
    
    def conexionBD (self):
        try:
            conexion = sqlite3.connect ("C:/Users/mecat/OneDrive/Documentos/GitHub/ProyectoIntegrador/entregable parcial3/BDRequisicion.db")
            print ("conectado a la BD")
            return conexion
        
        except sqlite3.OperationalError:
            print ("no se pudo conectar")
            
    def GuardarRequisicion (self, requi, fecha, partida, cant, des, asoli):
        #llamar metodo conexion
        conx = self.conexionBD()
        
        #validar vacíos
        if (requi == "" or fecha == "" or partida == "" or cant == "" or des == "" or asoli == ""):
            messagebox.showwarning ("Warning", "Formulario incompleto")
            conx.close()
            
        else:
            #realizar insert a la base de datos
            #preparar variables
            cursor = conx.cursor()
            datos = (requi, fecha, partida, cant, des, asoli)
            sqlInsert = "insert into Requisicion(requisicion, fecha, partida, cantidad, descripcion, areaSolicitante) values (?, ?, ?, ?, ?, ?)"
            
            #ejecutar insert
            cursor.execute(sqlInsert, datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Registro exitoso", "Requisición guardada")
            
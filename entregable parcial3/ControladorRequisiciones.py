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
            
    def consultarRequi(self, id):
        #1. Realizar conexión a la base de datos
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == ""):
            messagebox.showwarning ("Warning", "Ingresa un ID")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "select * from Requisicion where id_requi = " + id
                
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect)
                RSusuario = cursor.fetchall()
                conx.close()
                return RSusuario
                
            except sqlite3.OperationalError:
                print ("Error de consulta")
    
    def consultarTodosLosUsuarios(self):
        #1. Realizar conexión a la base de datos
        conx = self.conexionBD()
        
        try: 
                #4. Preparar lo necesario
            cursor = conx.cursor()
            sqlSelect = "select * from Requisicion"
                
                #5. Ejecutar y cerrar conexión
            cursor.execute(sqlSelect)
            RSusuario = cursor.fetchall()
            conx.close()
            return RSusuario
                
        except sqlite3.OperationalError:
            print ("Error de consulta todos los usuarios")
            
    def EliminarRequi(self, id):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == ""):
            messagebox.showwarning ("Warning", "Ingresa un ID")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "DELETE FROM Requisicion WHERE id_requi = "+ id
                
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect)
                conx.commit()
                conx.close()
                
            except sqlite3.OperationalError:
                print ("Error")
    
    def ActualizarRequiNum(self, id, requi):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == "" or requi == ""):
            messagebox.showwarning ("Warning", "Ingresa el ID y número de requisición")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "UPDATE Requisicion SET requisicion = ? WHERE id_requi = ?"
                actualizar = (requi, id)
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect, actualizar)
                conx.commit()
                conx.close()
                messagebox.showinfo("Actualización exitosa", "Se actualizó el número de requisición exitosamente")
                
            except sqlite3.OperationalError:
                print ("Error para actualizar requisición")
    
    def ActualizarFecha(self, id, fecha):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == "" or fecha == ""):
            messagebox.showwarning ("Warning", "Ingresa el ID y fecha")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "UPDATE Requisicion SET fecha = ? WHERE id_requi = ?"
                actualizar = (fecha, id)
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect, actualizar)
                conx.commit()
                conx.close()
                messagebox.showinfo("Actualización exitosa", "Se actualizó la fecha exitosamente")
                
            except sqlite3.OperationalError:
                print ("Error para actualizar fecha")
    
    def ActualizarPartida(self, id, part):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == "" or part== ""):
            messagebox.showwarning ("Warning", "Ingresa el ID y partida")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "UPDATE Requisicion SET partida = ? WHERE id_requi = ?"
                actualizar = (part, id)
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect, actualizar)
                conx.commit()
                conx.close()
                messagebox.showinfo("Actualización exitosa", "Se actualizó la partida exitosamente")
                
            except sqlite3.OperationalError:
                print ("Error para actualizar partida")
    
    def ActualizarCantidad(self, id, cant):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == "" or cant == ""):
            messagebox.showwarning ("Warning", "Ingresa el ID y cantidad")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "UPDATE Requisicion SET cantidad = ? WHERE id_requi = ?"
                actualizar = (cant, id)
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect, actualizar)
                conx.commit()
                conx.close()
                messagebox.showinfo("Actualización exitosa", "Se actualizó la cantidad exitosamente")
                
            except sqlite3.OperationalError:
                print ("Error para actualizar requisición")
                
    def ActualizarDescr(self, id, descr):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == "" or descr == ""):
            messagebox.showwarning ("Warning", "Ingresa el ID y descripción")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "UPDATE Requisicion SET descripcion = ? WHERE id_requi = ?"
                actualizar = (descr, id)
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect, actualizar)
                conx.commit()
                conx.close()
                messagebox.showinfo("Actualización exitosa", "Se actualizó la descripción exitosamente")
                
            except sqlite3.OperationalError:
                print ("Error para actualizar descripción")
                
    def ActualizarASoli(self, id, soli):
        conx = self.conexionBD()
        
        #2. Verificar que el id no esté vacío
        if (id == "" or soli == ""):
            messagebox.showwarning ("Warning", "Ingresa el ID y área del solicitante")
            conx.close()
        else:
            #3. Ejecutar la consulta
            try: 
                #4. Preparar lo necesario
                cursor = conx.cursor()
                sqlSelect = "UPDATE Requisicion SET areaSolicitante = ? WHERE id_requi = ?"
                actualizar = (soli, id)
                #5. Ejecutar y cerrar conexión
                cursor.execute(sqlSelect, actualizar)
                conx.commit()
                conx.close()
                messagebox.showinfo("Actualización exitosa", "Se actualizó el área del solicitante exitosamente")
                
            except sqlite3.OperationalError:
                print ("Error para actualizar área solicitante")
            
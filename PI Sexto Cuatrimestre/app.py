from flask import Flask, render_template, request, redirect,url_for,flash #Importar libreria
from flask_mysqldb import MySQL

app=Flask(__name__) #Inicializacion del servidor Flask

#Configuraciones para la conexion de   
app.config['MYSQL_HOST']="localhost" #Especificar en que servidor trabajamos
app.config['MYSQL_USER']="root" #Especificar usuario
app.config['MYSQL_PASSWORD']="" #Especificar contraseña
app.config['MYSQL_DB']="proyectointegrador" #Especificar a que base de datos

app.secret_key='mysecretkey' #Permite hacer envios a traves de post

mysql=MySQL(app)

#Declaracion de rutas

#Declarar ruta Index/principal http//localhost:5000
#Ruta se compone de nombre y funcion
@app.route('/')
def index():
    return render_template('index.html')

#app.route('/ingresar', methods={'GET','POST'})
#def ingresarP():

@app.route('/requisiciones')
def requisiciones():
    return render_template('RegistrarRequisicion.html')

@app.route('/cotizaciones')
def cotizaciones():
    return render_template('RegistrarCotizacion.html')

@app.route('/proovedores')
def proveedores():
    return render_template('RegistrarProveedor.html')

#Registrar
@app.route('/registrarR',methods=['GET','POST'])
def registrarR():
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        Nfecha=request.form['Fecha']
        Nnumad=request.form['requisicion']
        Ncant=request.form['Cantidad']
        Npart=request.form['Partida']
        Ndescrip=request.form['Descripcion']
        Nas=request.form['Area_solicitante']
        
        CS=mysql.connection.cursor()
        CS.execute('insert into requisicion(fecha,numeroadquisicion,cantidad,partida,descripcion,areasolicitante) values(%s,%s,%s,%s,%s,%s)',
                   (Nfecha,Nnumad,Ncant,Npart,Ndescrip,Nas)) #Para ejecutar codigo sql, y pasamos parametros
        mysql.connection.commit()

    flash('Requisicion registrada')
    return render_template('RegistrarRequisicion.html') #Reedireccionamiento a la vista index

@app.route('/registrarC',methods=['GET','POST'])
def registrarC():
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        Nval=request.form['Validar']
        Nnumcot=request.form['Numero cotizacion']
        Nfechac=request.form['Fecha']
        Nem=request.form['Empresa']
        Nrfc=request.form['RFC']
        Nidd=request.form['Domicilio']
      
        CS=mysql.connection.cursor()
        CS.execute('insert into cotizacion(validar,numerocotizacion,fecha,empresa,rfc,domicilio) values(%s,%s,%s,%s,%s,%s)',
                   (Nval,Nnumcot,Nfechac,Nem,Nrfc,Nidd)) #Para ejecutar codigo sql, y pasamos parametros
        mysql.connection.commit()

    flash('Cotizacion registrada')
    return render_template('RegistrarCotizacion.html') #Reedireccionamiento a la vista index

@app.route('/registrarP',methods=['GET','POST'])
def registrarP():
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        Nnombre=request.form['Nombre']
        Nap=request.form['Apellido Paterno']
        Nam=request.form['Apellido Materno']
        Nrfcp=request.form['RFC']
        Nempp=request.form['Empresa']
        Niddp=request.form['Domicilio']
        
        CS=mysql.connection.cursor()
        CS.execute('insert into proveedores(nombre,ap,am,rfc,empresa,domicilio) values(%s,%s,%s,%s,%s,%s)',
                   (Nnombre,Nap,Nam,Nrfcp,Nempp,Niddp)) #Para ejecutar codigo sql, y pasamos parametros
        mysql.connection.commit()

    flash('Proveedor registrado')
    return render_template('RegistrarProveedor.html')

#Actualizar
@app.route('/actualizarR/<id>',methods=['GET','POST'])
def actualizarR(id):
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        Nfecha=request.form['Fecha']
        Nnumad=request.form['requisicion']
        Ncant=request.form['Cantidad']
        Npart=request.form['Partida']
        Ndescrip=request.form['Descripcion']
        Nas=request.form['Area_solicitante']
        
        CS=mysql.connection.cursor()
        CS.execute('update requisicion set fecha=%s,numeroadquisicion=%s,cantidad=%s,partida=%s,descripcion=%s,areasolicitante=%s where id_requisicion=%s',
                   (Nfecha,Nnumad,Ncant,Npart,Ndescrip,Nas,id)) #Para ejecutar codigo sql, y pasamos parametros
        mysql.connection.commit()

    flash('Requisicion registrada')
    return redirect(url_for('index')) #Reedireccionamiento a la vista index

@app.route('/actualizarC/<id>',methods=['GET','POST'])
def actualizarC(id):
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        Nval=request.form['Validar']
        Nnumcot=request.form['Numero cotizacion']
        Nfechac=request.form['Fecha']
        Nem=request.form['Empresa']
        Nrfc=request.form['RFC']
        Nidd=request.form['Domicilio']
      
        CS=mysql.connection.cursor()
        CS.execute('update cotizacion set validar=%s,numerocotizacion=%s,fecha=%s,empresa=%s,rfc=%s,domicilio=%s where id_cotizacion=%s',
                   (Nval,Nnumcot,Nfechac,Nem,Nrfc,Nidd,id)) #Para ejecutar codigo sql, y pasamos parametros
        mysql.connection.commit()

    flash('Cotizacion registrada')
    return redirect(url_for('index'))

@app.route('/actualizarP/<id>',methods=['GET','POST'])
def actualizarP(id):
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        Nnombre=request.form['Nombre']
        Nap=request.form['Apellido Paterno']
        Nam=request.form['Apellido Materno']
        Nrfcp=request.form['RFC']
        Nempp=request.form['Empresa']
        Niddp=request.form['Domicilio']
        
        CS=mysql.connection.cursor()
        CS.execute('update proveedores set nombre=%s,ap=%s,am=%s,rfc=%s,empresa=%s,domicilio=%s where id_proveedores=%s',
                   (Nnombre,Nap,Nam,Nrfcp,Nempp,Niddp,id)) #Para ejecutar codigo sql, y pasamos parametros
        mysql.connection.commit()

    flash('Proveedor registrado')
    return redirect(url_for('index'))

#Editar pase de parametros --- ACTUALIZAR
@app.route('/editarR/<id>')
def editarR(id):
    curEditar=mysql.connection.cursor()
    curEditar.execute('select * from requisicion where id_requisicion= %s', (id,))#Coma importante por que lo confunde con una tupla
    consultaID=curEditar.fetchone() #Para traer unicamente un registro

    return render_template('ActualizarRequisicion.html', edrequi=consultaID)

@app.route('/editarC/<id>')
def editarC(id):
    curEditar=mysql.connection.cursor()
    curEditar.execute('select * from cotizacion where id_cotizacion= %s', (id,))#Coma importante por que lo confunde con una tupla
    consultaID=curEditar.fetchone() #Para traer unicamente un registro

    return render_template('ActualizarCotizacion.html', edcoti=consultaID)

@app.route('/editarP/<id>')
def editarP(id):
    curEditar=mysql.connection.cursor()
    curEditar.execute('select * from proveedores where id_proveedores= %s', (id,))#Coma importante por que lo confunde con una tupla
    consultaID=curEditar.fetchone() #Para traer unicamente un registro

    return render_template('ActualizarProveedor.html', edprov=consultaID)

#Busq para vistas

@app.route('/busqR/<id>' ,methods=['GET','POST'] )
def busqR(id):
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from requisicion where id_requisicion=%s', (id,))
    consulta=curSelect.fetchone() #Para traer solo un registro
    return render_template('BuscarRequisicion.html', busrequi=consulta)

#Buscar
@app.route('/buscarR',methods=['GET','POST'])
def buscarR():
    '''curSelect=mysql.connection.cursor()
    curSelect.execute('select * from requisicion where id=%s', (id,))
    consulta=curSelect.fetchone() #Para traer solo un registro'''
    return render_template('BuscarRequisicion.html')

@app.route('/buscarC/<id>',methods=['GET','POST'])
def buscarC():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from cotizacion where id=%s', (id,))
    consulta=curSelect.fetchone() #Para traer solo un registro
    return render_template('BuscarCotizacion.html', buscoti=consulta)

@app.route('/buscarP/<id>',methods=['GET','POST'])
def buscarP():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from proveedores where id=%s', (id,))
    consulta=curSelect.fetchone() #Para traer solo un registro
    return render_template('BuscarProveedor.html', busprov=consulta)

#Consultar
@app.route('/consultarR',methods=['GET','POST'])
def consultarR():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from requisicion')
    consulta=curSelect.fetchall() #Para traer varios registros
    #print(consulta)
    return render_template('ConsultarRequisicion.html', tbrequisicion=consulta)#Nos sirve para concatenar las consultas y abrir rutas

@app.route('/consultarC',methods=['GET','POST'])
def consultaC():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from cotizacion')
    consulta=curSelect.fetchall() #Para traer varios registros
    return render_template('ConsultarCotizacion.html', tbcoti=consulta)

@app.route('/consultarP',methods=['GET','POST'])
def consultarP():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from proveedores')
    consulta=curSelect.fetchall() #Para traer varios registros
    #print(consulta)
    return render_template('ConsultarProveedor.html', tbprov=consulta)

#Eliminar
@app.route('/eliminarR/<id>', methods=['GET','POST'])
def eliminarR(id):
    curDelete=mysql.connection.cursor()
    curDelete.execute('delete from requisicion where id_requisicion=%s', (id)) 
    mysql.connection.commit() #Para actualizar

    flash('Requisicion eliminada correctamente')
    return redirect(url_for('index'))

@app.route('/eliminarC/<id>', methods=['GET','POST'])
def eliminarC(id):
    curDelete=mysql.connection.cursor()
    curDelete.execute('delete from cotizacion where id_cotizacion=%s', (id)) 
    mysql.connection.commit() #Para actualizar

    flash('Cotizacion eliminada correctamente')
    return redirect(url_for('index'))

@app.route('/eliminarP/<id>', methods=['GET','POST'])
def eliminarP(id):
    curDelete=mysql.connection.cursor()
    curDelete.execute('delete from proveedores where id_proveedores=%s', (id)) 
    mysql.connection.commit() #Para actualizar

    flash('Proveedor eliminada correctamente')
    return redirect(url_for('index'))

#Borrar para eliminar

@app.route('/borrarR/<id>')
def borrarR(id):
    curBorrar=mysql.connection.cursor()
    curBorrar.execute('select * from requisicion where id_requisicion= %s', (id,))#Coma importante por que lo confunde con una tupla
    consultaID=curBorrar.fetchone() #Para traer unicamente un registro

    return render_template('EliminarRequisicion.html', brequi=consultaID)

@app.route('/borrarC/<id>')
def borrarC(id):
    curBorrar=mysql.connection.cursor()
    curBorrar.execute('select * from cotizacion where id_cotizacion= %s', (id,))#Coma importante por que lo confunde con una tupla
    consultaID=curBorrar.fetchone() #Para traer unicamente un registro

    return render_template('EliminarCotizacion.html', bcoti=consultaID)

@app.route('/borrarP/<id>')
def borrarP(id):
    curBorrar=mysql.connection.cursor()
    curBorrar.execute('select * from proveedores where id_proveedores= %s', (id,))#Coma importante por que lo confunde con una tupla
    consultaID=curBorrar.fetchone() #Para traer unicamente un registro

    return render_template('EliminarProveedor.html', bprov=consultaID)

#Ejecucion del servidor
if __name__=='__main__':
    app.run(port=5005,debug=True) #Procurar que sea un puerto desocupado, debug(prendido)
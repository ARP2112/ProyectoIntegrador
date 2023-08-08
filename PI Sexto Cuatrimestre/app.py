from flask import Flask, render_template, request, redirect,url_for,flash #Importar libreria
from flask_login import LoginManager, login_user, logout_user, login_required

#Config
from config import config

#Database
from flask_mysqldb import MySQL

#Models
from models.modelUser import ModelUser

#Entities
from models.entities.user import User

app=Flask(__name__) #Inicializacion del servidor Flask

#Configuraciones para la conexion de   
app.config['MYSQL_HOST']="localhost" #Especificar en que servidor trabajamos
app.config['MYSQL_USER']="root" #Especificar usuario
app.config['MYSQL_PASSWORD']="" #Especificar contraseña
app.config['MYSQL_DB']="proyectointegrador" #Especificar a que base de datos

app.secret_key='mysecretkey' #Permite hacer envios a traves de post

mysql=MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(mysql, id)

#Declaracion de rutas

#Declarar ruta Index/principal http//localhost:5000
#Ruta se compone de nombre y funcion
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    usuario=request.form['Usuario']
    contraseña=request.form['Contraseña']
    if request.method=='POST':
        
        user = User(0, usuario, contraseña)
        logged_user = ModelUser.login(mysql, user)
        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('inicio'))
            else:
                flash ('Contraseña incorrecta')
                return render_template ('login.html')
        else:
            flash ('Usuario no encontrado')
            return render_template ('login.html')
    else:
        return render_template ('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return render_template ('login.html')

@app.route('/inicio')
@login_required
def inicio():
    return render_template('inicio.html')

@app.route('/requisiciones')
@login_required
def requisiciones():
    return render_template('RegistrarRequisicion.html')

@app.route('/cotizaciones')
@login_required
def cotizaciones():
    return render_template('RegistrarCotizacion.html')

@app.route('/proovedores')
@login_required
def proveedores():
    return render_template('RegistrarProveedor.html')

@app.route('/ordenCompra')
@login_required
def ordenCompra():
    return render_template('RegistrarOrdenCompra.html')

@app.route('/registrarUsuario')
@login_required
def registrarUsuario():
    return render_template('RegistrarUsuario.html')

#Registrar USUARIOS
"""@app.route('/registrarU',methods=['GET','POST'])
def registrarU():
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        usuario=request.form['Usuario']
        contraseña=request.form['Contraseña']
        nombre=request.form['NombreC']
        
        CS=mysql.connection.cursor()
        CS.execute('insert into Usuarios(nombreusuario, contraseña, Nombre_completo) values(%s,%s,%s)',
                   (usuario, contraseña, nombre)) #Para ejecutar codigo sql, y pasamos parametros
        mysql.connection.commit()

    flash('Usuario registrado')
    return render_template('RegistrarUsuario.html') #Reedireccionamiento a la vista index"""

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
    return render_template('inicio.html') #Reedireccionamiento a la vista index

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
    return render_template('inicio.html') #Reedireccionamiento a la vista index

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
    return render_template('inicio.html')

@app.route('/registrarO',methods=['GET','POST'])
def registrarO():
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        NnumC=request.form['NumCompra']
        Nfecha=request.form['Fecha']
        Ndesc=request.form['Descripcion']
        Ncant=request.form['Cantidad']
        Npt=request.form['PrecioTotal']
        
        CS=mysql.connection.cursor()
        CS.execute('insert into OrdenesCompra(numeroCompra,fecha,descripcion,cantidad,preciototal) values(%s,%s,%s,%s,%s)',
                   (NnumC,Nfecha,Ndesc,Ncant,Npt)) #Para ejecutar codigo sql, y pasamos parametros
        mysql.connection.commit()

    flash('Orden de compra registrada')
    return render_template('RegistrarOrdenCompra.html')

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

    flash('Requisición Actualizada')
    return redirect(url_for('inicio')) #Reedireccionamiento a la vista index

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

    flash('Cotización Actualizada')
    return redirect(url_for('inicio'))

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

    flash('Proveedor Actualizado')
    return redirect(url_for('inicio'))

@app.route('/actualizarO/<id>',methods=['GET','POST'])
def actualizarO(id):
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        NnumC=request.form['NumCompra']
        Nfecha=request.form['Fecha']
        Ndesc=request.form['Descripcion']
        Ncant=request.form['Cantidad']
        Npt=request.form['PrecioTotal']
        
        CS=mysql.connection.cursor()
        CS.execute('update OrdenesCompra set numeroCompra=%s,fecha=%s,descripcion=%s,cantidad=%s,preciototal=%s where id_ordenesCompra=%s',
                   (NnumC,Nfecha,Ndesc,Ncant,Npt,id)) #Para ejecutar codigo sql, y pasamos parametros
        mysql.connection.commit()

    flash('Orden de compra Actualizada')
    return redirect(url_for('inicio'))

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

@app.route('/editarO/<id>')
def editarO(id):
    curEditar=mysql.connection.cursor()
    curEditar.execute('select * from OrdenesCompra where id_ordenesCompra= %s', (id,))#Coma importante por que lo confunde con una tupla
    consultaID=curEditar.fetchone() #Para traer unicamente un registro

    return render_template('ActualizarOrdenCompra.html', edoc=consultaID)

#Busq para vistas

#Buscar
@app.route('/buscarR',methods=['GET','POST'])
def buscarR():
    Bas = request.form.get('Area_solicitante')
    curBusq=mysql.connection.cursor()
    curBusq.execute('select * from requisicion where areasolicitante LIKE %s', (f'%{Bas}%',))
    consulta=curBusq.fetchall() #Para traer solo un registro'''
    return render_template('BuscarRequisicion.html', busrequi=consulta)

@app.route('/buscarC',methods=['GET','POST'])
def buscarC():
    Bemp=request.form.get('empresa')
    curBusq=mysql.connection.cursor()
    curBusq.execute('select * from cotizacion where empresa LIKE %s', (f'%{Bemp}%',))
    consulta=curBusq.fetchall() #Para traer solo un registro
    return render_template('BuscarCotizacion.html', buscoti=consulta)

@app.route('/buscarP',methods=['GET','POST'])
def buscarP():
    Bnom=request.form.get('nombre')
    curBusq=mysql.connection.cursor()
    curBusq.execute('select * from proveedores where nombre LIKE %s', (f'%{Bnom}%',))
    consulta=curBusq.fetchall() #Para traer solo un registro
    return render_template('BuscarProveedor.html', busprov=consulta)

@app.route('/buscarO',methods=['GET','POST'])
def buscarO():
    return render_template('BuscarOrdenCompra.html')

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

@app.route('/consultarO',methods=['GET','POST'])
def consultarO():
    curSelect=mysql.connection.cursor()
    curSelect.execute('select * from ordenesCompra')
    consulta=curSelect.fetchall() #Para traer varios registros
    #print(consulta)
    return render_template('ConsultarOrdenCompra.html', tboc=consulta)

#Eliminar
@app.route('/eliminarR/<id>', methods=['GET','POST'])
def eliminarR(id):
    curDelete=mysql.connection.cursor()
    curDelete.execute('delete from requisicion where id_requisicion=%s', (id)) 
    mysql.connection.commit() #Para actualizar

    flash('Requisición Eliminada')
    return redirect(url_for('inicio'))

@app.route('/eliminarC/<id>', methods=['GET','POST'])
def eliminarC(id):
    curDelete=mysql.connection.cursor()
    curDelete.execute('delete from cotizacion where id_cotizacion=%s', (id)) 
    mysql.connection.commit() #Para actualizar

    flash('Cotización Eliminada')
    return redirect(url_for('inicio'))

@app.route('/eliminarP/<id>', methods=['GET','POST'])
def eliminarP(id):
    curDelete=mysql.connection.cursor()
    curDelete.execute('delete from proveedores where id_proveedores=%s', (id)) 
    mysql.connection.commit() #Para actualizar

    flash('Proveedor Eliminado')
    return redirect(url_for('inicio'))

@app.route('/eliminarO/<id>', methods=['GET','POST'])
def eliminarO(id):
    curDelete=mysql.connection.cursor()
    curDelete.execute('delete from OrdenesCompra where id_ordenesCompra=%s', (id)) 
    mysql.connection.commit() #Para actualizar

    flash('Orden de compra Eliminada')
    return redirect(url_for('inicio'))

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

@app.route('/borrarO/<id>')
def borrarO(id):
    curBorrar=mysql.connection.cursor()
    curBorrar.execute('select * from OrdenesCompra where id_ordenesCompra= %s', (id,))#Coma importante por que lo confunde con una tupla
    consultaID=curBorrar.fetchone() #Para traer unicamente un registro

    return render_template('EliminarOrdenCompra.html', boc=consultaID)


#ERROR HTML PARA USUARIOS QUE NO HAN INGRESADO (ERROR 401)
def status_401(error):
    return redirect(url_for('login'))


#ERROR HTML PARA URL NO ENCONTRADAS (ERROR 404)
def status_404(eror):
    return "<h1> Página no encontrada </h1>", 404


#Ejecucion del servidor
if __name__=='__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(port=5005,debug=True) #Procurar que sea un puerto desocupado, debug(prendido)
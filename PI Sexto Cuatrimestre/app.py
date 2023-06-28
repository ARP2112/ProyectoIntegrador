from flask import Flask, render_template, request, redirect,url_for,flash #Importar libreria
from flask_mysqldb import MySQL

app=Flask(__name__) #Inicializacion del servidor Flask

#Configuraciones para la conexion de   
app.config['MYSQL_HOST']="localhost" #Especificar en que servidor trabajamos
app.config['MYSQL_USER']="root" #Especificar usuario
app.config['MYSQL_PASSWORD']="" #Especificar contraseña
app.config['MYSQL_DB']="ProyectoIntegrador2(2)" #Especificar a que base de datos

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
        Nfecha=request.form['fecha']
        Nnumad=request.form['numeroadquisicion']
        Ncant=request.form['cantidad']
        Npart=request.form['partida']
        Ndescrip=request.form['descripcion']
        Nas=request.form['areasolicitante']
        
        CS=mysql.connection.cursor()
        CS.execute('insert into requisicion(fecha,numeroadquisicion,cantidad,partida,descripcion,areasolicitante) values(%s,%s,%s,%s,%s,%s)',
                   (Nfecha,Nnumad,Ncant,Npart,Ndescrip,Nas)) #Para ejecutar codigo sql, y pasamos parametros
        mysql.connection.commit()

    flash('Requisicion registrada')
    return render_template('RegistrarRequisicion.html') #Reedireccionamiento a la vista index

@app.route('/registrarC',methods=['GET','POST'])
def registrarC():
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        Nval=request.form['validar']
        Nnumcot=request.form['numerocotizacion']
        Nfechac=request.form['fecha']
        Nem=request.form['empresa']
        Nrfc=request.form['rfc']
        Nidd=request.form['id_domicilio']
      
        CS=mysql.connection.cursor()
        CS.execute('insert into cotizacion(validar,numerocotizacion,fecha,empresa,rfc,id_domicilio) values(%s,%s,%s,%s,%s,%s)',
                   (Nval,Nnumcot,Nfechac,Nem,Nrfc,Nidd)) #Para ejecutar codigo sql, y pasamos parametros
        mysql.connection.commit()

    flash('Cotizacion registrada')
    return render_template('RegistrarCotizacion.html') #Reedireccionamiento a la vista index

@app.route('/registrarP',methods=['GET','POST'])
def registrarP():
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        Nnombre=request.form['nombre']
        Nap=request.form['ap']
        Nam=request.form['am']
        Nrfcp=request.form['rfc']
        Nempp=request.form['empresa']
        Niddp=request.form['id_domicilio']
        
        CS=mysql.connection.cursor()
        CS.execute('insert into proveedores(nombre,ap,am,rfc,empresa,id_domicilio) values(%s,%s,%s,%s,%s,%s)',
                   (Nnombre,Nap,Nam,Nrfcp,Nempp,Niddp)) #Para ejecutar codigo sql, y pasamos parametros
        mysql.connection.commit()

    flash('Proveedor registrado')
    return render_template('RegistrarProveedor.html')

#Actualizar
@app.route('/actualizarR',methods=['GET','POST'])
def actualizarR():
    return render_template('ActualizarRequisicion.html')

@app.route('/actualizarC',methods=['GET','POST'])
def actualizarC():
    return render_template('ActualizarCotizacion.html')

@app.route('/actualizarP',methods=['GET','POST'])
def actualizarP():
    return render_template('ActualizarProovedor.html')

#Buscar
@app.route('/buscarR',methods=['GET','POST'])
def buscarR():
    return render_template('BuscarRequisicion.html')

@app.route('/buscarC',methods=['GET','POST'])
def buscarC():
    return render_template('BuscarCotizacion.html')

@app.route('/buscarP',methods=['GET','POST'])
def buscarP():
    return render_template('BuscarProveedor.html')

#Consultar
@app.route('/consultarR',methods=['GET','POST'])
def consultarR():
    return render_template('ConsultarRequisicion.html')

@app.route('/consultarC',methods=['GET','POST'])
def consultaC():
    return render_template('ConsultarCotizacion.html')

@app.route('/consultarP',methods=['GET','POST'])
def consultarP():
    return render_template('ConsultarProveedor.html')

#Eliminar
@app.route('/eliminarR', methods=['GET','POST'])
def eliminarR():
    return render_template('EliminarRequisicion.html')

@app.route('/eliminarC', methods=['GET','POST'])
def eliminarC():
    return render_template('EliminarCotizacion.html')

@app.route('/eliminarP', methods=['GET','POST'])
def eliminarP():
    return render_template('EliminarProveedor.html')

#Ejecucion del servidor
if __name__=='__main__':
    app.run(port=5000,debug=True) #Procurar que sea un puerto desocupado, debug(prendido)
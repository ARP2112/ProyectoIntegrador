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
    #return redirect(url_for('Admin_med registrar usuario.html'))
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        Nnombre=request.form['nombre']
        Nap=request.form['AP']
        Nam=request.form['AM']
        Ncp=request.form['CP']
        Npass=request.form['pass']
        Nce=request.form['CE']
        Nrol=request.form['rol']
        #print(titulo,artista,anio)
        CS=mysql.connection.cursor()
        CS.execute('insert into admin_med_registrar_usuarios(nombre,ap,am,cedulap,contraseña,correo,rol) values(%s,%s,%s,%s,%s,%s,%s)',
                   (Nnombre,Nap,Nam,Ncp,Npass,Nce,Nrol)) #Para ejecutar codigo sql, y pasamos parametros
        mysql.connection.commit()

    flash('Requisicion registrada')
    return render_template('RegistrarRequisicion.html') #Reedireccionamiento a la vista index

@app.route('/registrarC',methods=['GET','POST'])
def registrarC():
    if request.method=='POST': #Peticiones del usuario a traves del metodo POST
        Nmedico=request.form['medico']
        Npaciente=request.form['paciente']
        Nap=request.form['AP']
        Nam=request.form['AM']
        Nfn=request.form['FN']
        Nec=request.form['EC']
        Nal=request.form['AL']
        Naf=request.form['AF']
        #print(titulo,artista,anio)
        CS=mysql.connection.cursor()
        CS.execute('insert into expediente_paciente(medico_atiende,nombre_paciente,ap_paciente,am_paciente,fecha_nacimiento,enfermedades_cronicas,alergias,antecedentes_familiares) values(%s,%s,%s,%s,%s,%s,%s,%s)',
                   (Nmedico,Npaciente,Nap,Nam,Nfn,Nec,Nal,Naf)) #Para ejecutar codigo sql, y pasamos parametros
        mysql.connection.commit()

    flash('Cotizacion registrada')
    return render_template('RegistrarCotizacion.html') #Reedireccionamiento a la vista index

@app.route('/registrarP',methods=['GET','POST'])
def registrarP():
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
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
    return render_template('index.html')

@app.route('/proovedores')
def proveedores():
    return render_template('index.html')

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

@app.route('/Login',methods=['GET','POST'])
def login():
    return render_template('Interfaz login.html')


@app.route('/actualizarPaciente',methods=['GET','POST'])
def actualizarPaciente():
    return render_template('Actualizar paciente.html')

@app.route('/actualizarMedico',methods=['GET','POST'])
def actualizarMedico():
    return render_template('Admin_med actualizar datos.html')

@app.route('/buscarMedico',methods=['GET','POST'])
def buscarMedico():
    return render_template('Buscar médico.html')

@app.route('/consultarCitas',methods=['GET','POST'])
def consultarCitas():
    return render_template('Consultar citas.html')

@app.route('/consultaMedico',methods=['GET','POST'])
def consultaMedico():
    return render_template('Consultar médico.html')

@app.route('/consultarPaciente',methods=['GET','POST'])
def consultarPaciente():
    return render_template('Consultar paciente.html')

@app.route('/descargarReceta',methods=['GET','POST'])
def descargarReceta():
    return render_template('Descargar receta.html')
@app.route('/diagPaciente',methods=['GET','POST'])
def diagPaciente():
    return render_template('Diagnóstico paciente.html')

@app.route('/eliminarRequisicion', methods=['GET','POST'])
def eliminarRequisicion():
    return render_template('EliminarRequisicion.html')

@app.route('/exPaciente',methods=['GET','POST'])
def exPaciente():
    return render_template('Exploración paciente.html')
#Ejecucion del servidor
if __name__=='__main__':
    app.run(port=5000,debug=True) #Procurar que sea un puerto desocupado, debug(prendido)
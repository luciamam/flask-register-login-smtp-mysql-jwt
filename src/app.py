from flask import Flask,render_template,redirect,url_for,request



app=Flask(__name__)




@app.route('/')
def home():
    #cuando aterrizemos a la ruta raiz debemos redirigirnos a la ruta login 
    #return "Soy la ruta raiz que le va servir el formulario de login "

    return redirect(url_for('login'))

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form['name']
        fullname=request.form['fullname']
        email=request.form['email']
        password=request.form['password']

        return "procesar estos datos "
    
    return render_template('RegisterTemplate.html')



@app.route('/perfil')
def perfil():
    return "soy la ruta que te servira tu perfil"



@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']

        #vamos a comprobar que el usuario existe en la base de datos 
        return "usuario existe"
    return render_template('LoginTemplate.html')

#manejar el el codigo 404


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
    

if __name__=='__main__':
    app.run(debug=True)

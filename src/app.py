from flask import Flask,render_template,redirect,url_for



app=Flask(__name__)




@app.route('/')
def home():
    #cuando aterrizemos a la ruta raiz debemos redirigirnos a la ruta login 
    #return "Soy la ruta raiz que le va servir el formulario de login "

    return redirect(url_for('login'))

@app.route('/register')
def register():
    return "soy la ruta regsiter"


@app.route('/perfil')
def perfil():
    return "soy la ruta que te servira tu perfil"



@app.route('/login')
def login():
    return "soy la ruta login"

#manejar el el codigo 404


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404
    

if __name__=='__main__':
    app.run(debug=True)

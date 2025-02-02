from flask import Flask,render_template



app=Flask(__name__)




@app.route('/')
def home():
    return "Soy la ruta raiz que le va servir el formulario de login "

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

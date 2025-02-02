from flask import Flask



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



if __name__=='__main__':
    app.run(debug=True)

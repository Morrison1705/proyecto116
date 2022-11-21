# importar modulos de la biblioteca Flask.
from flask import Flask , render_template

# crear objetos de la clase Flask, dando __name__ como argumento.
app = Flask(__name__)

# escribir las rutas usando las funciones "decorator".
# ruta o 'URL' predefinida.
@app.route("/")
def home():

    name = "" # escribe tu nombre
    age = "" # escribe tu edad

    return render_template('index.html' , name = name , age = age)

# define la ruta a la página web de tu padre.
@app.route("/padre")
def father():
    name="tu papa"
    age="40"
    return render_template("father.html",name=name,age=age)
    
@app.route("/madre")
def mother():
    name="tu mama"
    age="12"
    return render_template("mother.html",name=name,age=age)

@app.route("/amigos")
def friends():
    name="tus amigos"
    age="23"
    return render_template("friends.html",name=name,age=age)

# define la ruta a la página web de tu madre.


# define la ruta a la página web de tus amigos.


# agrega otras rutas, si tú quieres.




# ejecuta el archivo
if __name__  ==  '__main__':
    app.run(debug=True)

from flask import Flask, render_template 

app=Flask(__name__)

@app.route("/")
def index():
    miscursos=['php','python','kotlin','switf']
    datos={
    'titulo':'hola',
    'bienvenida':"saludos",
    'edad':15,
    'curso':miscursos,
    'numerocursos':len(miscursos)

    }
    return render_template('index.html',data=datos)


@app.route('/formulario')
def inicio():
    return render_template("formulario.html")


if __name__=='__main__':
    app.run(debug=True,port=5000)

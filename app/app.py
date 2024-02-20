from flask import Flask, render_template


# este parametro es para identificar el archovo como principal
app = Flask(__name__)

# creacion de primera vista

# este metodo tiene que estar registrado como una ruta ra que cuando acceda a esta ruta me devuelva el metodo
# @app.route('/')#ruta raiz
# def index():#metodo de python
#     # return '<h1>hola wapo<h1>'
#     return '<h1>hola wapo<h1>'


# forma 2
# def index():

#     return '<h1>hola wapo<h1>'

# @app.route('/holaMundo')
# def hola_mundo():
#     return 'hola mundo'

@app.route('/')
def index():
    # de esta manera ya se babe que tiene que buscar este elemento dentro de la carpeta templates
    #return render_template('index.html ', titulo = 'Pagina Principal')
    #forma de encio por medio de diccionario
    data={
        'titulo': 'index',
        'encabezado':'Bienvenido'
    }
    return render_template('index.html ',  data= data)

if __name__ == '__main__':  # si estamos utilizando esta clase como principal
    # app.add_url_rule('/',view_func = index) #esta es otra forma 2
    app.run(debug=True)

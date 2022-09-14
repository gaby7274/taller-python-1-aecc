from re import L
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder='html-templates')


# pass the list to the template
@app.route('/')
def index():

    # Vamos a crear title

    # crea listas_de_apellidos, listas_de_nombres, listas de interes

    #  El Goal
    #  [
    #   ["Gabriel",'Van Gogh','Bloomberg',['comida','beber','janguear']],
    #   ["Luis",'Bloomberg','Rivera',['beber','janguear', 'dormir']],
    #   ["Eliam",'Rivera','Santiago', ['janguear', 'dormir','Jugar']],
    #   ["Cristian",'Santiago','Bunny',['dormir','jugar','carcajear']]
    #   ["Rose","Bunny","Van Gogh", ['jugar','carcajear','comida']]
    #
    #   ]
    #
    #
    #
    #
    #
    #
    #

    la_tabla = []

    for i in range(len("???")):

        fila_de_cada_tabla = []

        fila_de_cada_tabla.append("???")

        temp_lista_interes = []

        # Vamos a construir un while, TIP, usa otro indice, que empiece desde our current position

        fila_de_cada_tabla.append(temp_lista_interes)

        # que falta aqui??

    return render_template('user.html', title=title, la_tabla=la_tabla)


if __name__ == '__main__':
    app.run(debug=True)

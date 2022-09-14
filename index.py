from re import L
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder='html-templates')


# pass the list to the template
@app.route('/')
def index():

    title = "Titulo que quieran"

    listas_de_interes = ["Comida", "Beber", 'Janguear', 'Gaming', 'Marvel',
                         'Bad Bunny', 'Café', 'Llorar', 'Tumbarte los sandwiches de Bloomberg']

    listas_de_nombres = ['Gabriel', 'Yao Wei',
                         'Spongebob', 'Edward', 'Katarina', 'BRR', 'Tiago']
    listas_de_apellidos = ['Van Gogh', 'Bloomberg',
                           'González', 'Anuel-AA', 'Vélez', 'Kaponi', 'Penélope']

    #  El Goal
    #  [
    #   ["Gabriel",'Van Gogh','Bloomberg',['comida','beber','janguear']],
    #   ["Gabriel",'Van Gogh','Bloomberg',['comida','beber','janguear']
    #
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

    for i in range(len(listas_de_nombres)):

        fila_de_cada_tabla = []

        fila_de_cada_tabla.append(listas_de_nombres[i])
        fila_de_cada_tabla.append(listas_de_apellidos[i])
        fila_de_cada_tabla.append(
            listas_de_apellidos[(i+1) % len(listas_de_apellidos)])

        temp_lista_interes = []

        j = i

        while(j <= i+2):
            temp_lista_interes.append(listas_de_interes[j])
            j += 1
        fila_de_cada_tabla.append(temp_lista_interes)

        la_tabla.append(fila_de_cada_tabla)

    return render_template('user.html', title=title, la_tabla=la_tabla)


if __name__ == '__main__':
    app.run(debug=True)

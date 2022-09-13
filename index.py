from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

lista_interes = ['Bears', 'Coffee', 'Python', 'League of Legends', 'Jazz', 'Villano Antillano']
name = 'Nat'


@app.route('/')
def index(list, name):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__, template_folder='html-templates')

lista_interes = ['Bears', 'Coffee', 'Python', 'League of Legends', 'Jazz', 'Villana Antillano']
name = 'Nat'

# pass the list to the template
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<name>')
def user(name):	
    return render_template('user.html', name=name, lista_interes=lista_interes)

if __name__ == '__main__':
    app.run(debug=True)
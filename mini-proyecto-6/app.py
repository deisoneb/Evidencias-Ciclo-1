from flask import Flask, render_template, request
from num2words import num2words

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    palabras = ""
    if request.method == 'POST':
        numero = request.form.get('number')
        if numero:
            try:
                numero = int(numero)
                palabras = num2words(numero, lang='es')
            except ValueError:
                palabras = "Por favor, introduce un número válido."
    return render_template('index.html', palabras=palabras)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return  'Bienvenue monde des nabila'

@app.route('/produit/<titre>', methods=['GET'])
def produtto(titre):
    return f'Produit:{titre}'

@app.route('/acme/produit/<titre>')
def prod(titre):
    return render_template('produit.html', titulo=titre)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
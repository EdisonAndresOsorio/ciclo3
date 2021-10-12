import os
from flask import Flask, render_template, request, jsonify
#import productos
from productos import getProductosList
from  producto import getProducto



app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/producto', methods=['GET'])
@app.route('/producto/', methods=['GET'])
def producto():
    return render_template('product.html')

@app.route('/productos', methods=['GET','POST'])
@app.route('/productos/', methods=['GET','POST'])
def getProductos():
    return jsonify(getProductosList());

@app.route('/obtenerProducto', methods=['GET','POST'])
@app.route('/obtenerProducto/', methods=['GET','POST'])
def obtenerProducto():
    return jsonify(getProducto());

if(__name__ == '__main__'):
    app.run(debug=True, port=8080)

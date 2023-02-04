from flask import Flask, render_template
from flask import request

app=Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    datos = {
        'nombre': '',
        'compradores': '',
        'tarjeta': '',
        'boletas': '',
        'errores': '',
        'total': '',
    }
    return render_template('cinepolis.html', datos = datos)

@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form.get('nombre')
    compradores = int(request.form.get('compradores'))
    tarjeta = request.form.get('tarjeta')
    boletas = int(request.form.get('boletas'))
    total = 0
    errores = []
    
    if (boletas > compradores * 7):
        errores.append('No se pueden comprar mas de 7 boletas por persona.')

    if not errores:
        descuento = 0
        total = boletas * 12
        if boletas > 5:
            descuento = descuento + 0.15
        elif boletas > 2:
            descuento = descuento + 0.10

        if tarjeta:
            descuento = descuento + 0.10

        total = total - total * descuento

    datos = {
        'nombre': nombre,
        'compradores': compradores,
        'tarjeta': tarjeta,
        'boletas': boletas,
        'errores': errores,
        'total': total,
    }

    return render_template('cinepolis.html', datos = datos)



if __name__ == '__main__':
    app.run(debug=True,port=3000)
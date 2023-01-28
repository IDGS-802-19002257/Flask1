from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/operasbas', methods=['GET','POST'])
def operasBas():
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        operador = request.form.get('opera')
        if operador == 'suma':
            return '<h2> La suma es: {}'.format(str(int(num1)+int(num2)))
        elif operador == 'resta':
            return '<h2> La resta es: {}'.format(str(int(num1)-int(num2)))
        elif operador == 'division':
            return '<h2> La division es: {}'.format(str(int(num1)/int(num2)))
        else:
            return '<h2> La multiplicacion es: {}'.format(str(int(num1)*int(num2)))
    else:
        return """ 
        <form action='/operasbas' method='POST'>
            <label>N1:</label>
            <input type='text' name='num1'/><br>
            <label>N2:</label>
            <input type='text' name='num2'/><br>
            <label>¿Que operacion quieres realizar?</label><br>
            <label>Suma</label>
            <input type='radio' name='opera' value='suma'><br>
            <label>Resta</label>
            <input type='radio' name='opera' value='resta'><br>
            <label>Division</label>
            <input type='radio' name='opera' value='division'><br>
            <label>Multiplicacion</label>
            <input type='radio' name='opera' value='multiplicacion'><br>
            <input type='submit' value='calcular'/>
        </form> 
        """

if __name__ == '__main__':
    app.run(debug=True,port=3000)
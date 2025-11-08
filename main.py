from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal que renderiza el archivo HTML
@app.route('/')
def mostrar_producto():
    return render_template('Productos.html')

if __name__ == '__main__':
    app.run(debug=True)

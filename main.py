from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Ruta principal que renderiza el archivo HTML
@app.route('/')
def mostrar_producto():
    return render_template('Productos.html')

# Ruta para manejar el POST request del formulario
@app.route('/guardar_producto', methods=['POST'])
def guardar_producto():
    # Obtener los datos del JSON
    data = request.get_json()  # Aquí cambiamos a `get_json` en lugar de `form.get`

    # Verificar si los datos necesarios están presentes
    if not data or not all(key in data for key in ['name', 'description', 'price', 'stock', 'category', 'image']):
        return "Faltan datos necesarios en la solicitud", 400

    # Obtener los datos del JSON
    nombre = data.get('name')
    descripcion = data.get('description')
    precio = data.get('price')
    stock = data.get('stock')
    categoria = data.get('category')
    imagen = data.get('image')

    # Crear el cuerpo del JSON que será enviado a la API
    payload = {
        "title": nombre,
        "body": descripcion,
        "userId": 1,  # Usamos un ID ficticio para el ejemplo
    }

    # Enviar el POST request a la API externa
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)

    # Comprobar si la respuesta es exitosa (código 201)
    if response.status_code == 201:
        return redirect(url_for('mostrar_producto'))  # Redirigir al formulario
    else:
        return f"Error al guardar el producto: {response.status_code}", 500
if __name__ == '__main__':
    app.run(debug=True)

import flask
from flask import request, send_file, render_template
import qrcode
import io
import base64 # Importamos base64

app = flask.Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    qr_image = None # Variable para guardar la imagen en base64

    if request.method == 'POST':
        # 1. El formulario fue enviado (POST)
        data = request.form.get('data')
        
        if data:
            # 2. Generar el QR en memoria
            img = qrcode.make(data)
            buf = io.BytesIO()
            img.save(buf, format='PNG')
            
            # 3. Codificar la imagen en Base64
            # Esto nos da un string de texto que podemos incrustar en el HTML
            qr_image = base64.b64encode(buf.getvalue()).decode('utf-8')

    # 4. Renderizar la plantilla HTML.
    # Si es GET, qr_image será None (no se muestra nada).
    # Si es POST, qr_image tendrá los datos de la imagen.
    return render_template('index.html', qr_image=qr_image)


@app.route('/qr', methods=['GET'])
def generar_qr_api():
    # Dejamos esta ruta como una API "pura" por si la necesitas
    data = request.args.get('data')

    if not data:
        return "Error: No se proporcionó el parámetro 'data'.", 400

    try:
        img = qrcode.make(data)
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        buf.seek(0)
        return send_file(buf, mimetype='image/png')

    except Exception as e:
        return f"Error al generar el QR: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
# app.py
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import tensorflow as tf
import numpy as np
import cv2
import os

app = Flask(__name__)
CORS(app)  # Permite todas as origens

app.config["UPLOAD_FOLDER"] = "uploads"

# Função de processamento da imagem
def process_image(image_path):
    model = tf.keras.models.load_model("hypermodel.keras")
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    resize = tf.image.resize(img, (256, 256))
    test_prediction = model.predict(np.expand_dims(resize / 255, 0))
    return "A imagem é de uma fruta boa!" if test_prediction < 0.5 else "A imagem é de uma fruta podre!"

# Endpoint para upload de múltiplas imagens
@app.route("/upload", methods=["POST"])
def upload_images():
    if "image" not in request.files:
        return jsonify({"error": "Nenhuma imagem enviada"}), 400

    # Cria uma lista para armazenar as respostas de cada imagem
    responses = []

    # Processa cada imagem enviada
    for image in request.files.getlist("image"):
        if image.filename == "":
            responses.append({"error": "Arquivo de imagem inválido"})
            continue

        # Salva a imagem no servidor
        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        image.save(image_path)

        # Processa a imagem
        message = process_image(image_path)
        
        # URL para acessar a imagem
        image_url = f"http://localhost:5000/uploads/{filename}"
        
        # Adiciona o resultado à lista de respostas
        responses.append({"status": "sucesso", "message": message, "image_url": image_url})

    # Retorna a lista com os resultados de todas as imagens
    return jsonify(responses), 200

# Endpoint para servir arquivos da pasta uploads
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == "__main__":
    app.run(debug=True)

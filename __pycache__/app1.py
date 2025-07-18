from flask import Flask, render_template, request, url_for, current_app
from werkzeug.utils import secure_filename
from PIL import Image
import os
import label_image  # Your custom script for prediction
import image_fuzzy_clustering as fem  # Your image processing script
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications import imagenet_utils

# Initialize Flask app
app = Flask(__name__)

# Folder to save uploaded images
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'img')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# ------------- Helper Functions -------------
def load_image(image_path):
    """Runs prediction using your label_image model."""
    return label_image.main(image_path)


def prepare_image(image, target):
    """Prepares image for prediction model."""
    if image.mode != "RGB":
        image = image.convert("RGB")

    image = image.resize(target)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = imagenet_utils.preprocess_input(image)

    return image


def save_img(img, filename):
    """Saves image to static/images folder."""
    picture_path = os.path.join(current_app.root_path, 'static/images', filename)
    image = Image.open(img)
    image.save(picture_path)
    return picture_path


# ------------- Routes -------------
@app.route('/')
@app.route('/first')
def first():
    return render_template('first.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/chart')
def chart():
    return render_template('chart.html')


@app.route('/upload')
def upload():
    return render_template('index1.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        cluster_value = request.form.get('cluster')
        file = request.files['file']
        if not file:
            return "No file uploaded.", 400

        file_path = save_img(file, file.filename)
        fem.plot_cluster_img(file_path, cluster_value)
        return render_template('success.html')
    return "Invalid request", 400


@app.route('/predict', methods=['GET', 'POST'])
def upload1():
    if request.method == 'POST':
        file = request.files['file']
        if not file or file.filename == '':
            return "No file selected.", 400

        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Get prediction
        result = load_image(file_path)
        result = result.title()  # Format result

        # Descriptions for vitamin types
        descriptions = {
            "Vitamin A": " → Deficiency of vitamin A is associated with significant morbidity and mortality from common childhood infections...",
            "Vitamin B": " → Vitamin B12 deficiency may lead to a reduction in healthy red blood cells (anaemia)...",
            "Vitamin C": " → A condition caused by a severe lack of vitamin C in the diet...",
            "Vitamin D": " → Vitamin D deficiency can lead to a loss of bone density...",
            "Vitamin E": " → Vitamin E deficiency can cause nerve and muscle damage..."
        }

        detailed_result = result + descriptions.get(result, " → Description not found.")
        os.remove(file_path)  # Delete uploaded file after prediction

        return detailed_result

    return render_template('predict.html')  # Optional fallback for GET


# ------------- Run App -------------
if __name__ == '__main__':
    app.run(debug=True)

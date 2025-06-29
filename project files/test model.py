from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load your trained model
model = load_model('model/butterfly_classifier.h5')

# Map model output to butterfly species
class_labels = ['Monarch', 'Swallowtail', 'Morpho', 'Painted Lady', 'Red Admiral']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect(request.url)
    
    file = request.files['image']
    if file.filename == '':
        return redirect(request.url)
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Image preprocessing
    img = image.load_img(filepath, target_size=(224, 224))  # use model’s expected size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Predict species
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction)
    confidence = round(np.max(prediction) * 100, 2)
    predicted_species = class_labels[class_index]

    return render_template('model_result.html',
                           predicted_species=predicted_species,
                           confidence_score=confidence,
                           image_filename=filename)

if __name__ == '__main__':
    app.run(debug=True)

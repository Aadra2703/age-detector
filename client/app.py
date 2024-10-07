from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Configure upload folder and secret key for flash messages
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.secret_key = 'your_secret_key'  # Required for flashing messages

# Load the pre-trained model
model = tf.keras.models.load_model('age_gender_model.h5')
# model = tf.keras.models.load_model('model(1).h5')


# Helper function to prepare image
def prepare_image(img):
    img = image.load_img(img, target_size=(128,128))  # Adjust size according to your model
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255.0  # Normalize if your model requires it
    return img

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_and_predict():
    # Check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    # Check if no file is selected
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    # If a file is selected
    if file:
        # Save the uploaded file
        filename = secure_filename(file.filename)
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(img_path)
        print("Image saved to:", img_path)  # Debugging
        
        # Preprocess the image
        img = prepare_image(img_path)

        # Make prediction using the loaded model
        predictions = model.predict(img)
        
        # Assuming binary gender classification and age as a regression output
        age = predictions[0][0]  # Assuming age is the first output
        gender_prob = predictions[1][0]  # Assuming gender is the second output
        gender = 'Male' if gender_prob > 0.55 else 'Female'
        
        # Display the prediction results
        return render_template('results.html', age=int(age), gender=gender, img_path=img_path)
        # return render_template('results.html', age=int(age), img_path=img_path)
# Ensure this route points to your index

# If running locally, use this entry point
if __name__ == '__main__':
    app.run(debug=True)

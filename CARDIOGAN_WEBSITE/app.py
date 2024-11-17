from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load the TensorFlow model
model = tf.keras.models.load_model(r'CARDIOGAN_WEBSITE/convnet2.h5')

# Define route to serve the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define route to handle model prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file from the request
    image_file = request.files['image']

    # Preprocess the image
    image = Image.open(image_file)
    image = image.resize((200, 200))  # Resize the image to match model input size
    image = np.array(image) / 255.0  # Normalize pixel values (assuming input range [0, 255])
    image = np.expand_dims(image, axis=0)  # Expand dimensions to match model input shape
    
    # Perform inference
    result = model.predict(image)

    # Process the result
    classes = ['Abnormal', 'Mi', 'Normal']
    classification = classes[np.argmax(result)]

    # Return the classification
    return jsonify({'classification': classification})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import cv2
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

model = load_model('test.h5')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/classify', methods=['POST'])
def classify():
    file = request.files['image']
    image = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_COLOR)
    image = cv2.resize(image, (224, 224))
    image = np.expand_dims(image, axis=0)  # Add an extra dimension to match the shape (None, 224, 224, 3)

    prediction = model.predict(image)
    if prediction[0][0] == 0:
        
        result = "wildfire cannot occur"
    else:
        result = "Yes wildfire can occur"

    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)

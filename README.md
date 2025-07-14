# Wildfire Classification

This project is a web application that uses a pre-trained deep learning model to classify images and predict whether a wildfire can occur based on the input image. The application is built with Flask and utilizes OpenCV, TensorFlow, and Keras for image processing and model inference.

## Features

  * **Image Upload:** Users can upload an image through a simple web interface.
  * **Wildfire Prediction:** The uploaded image is processed by a trained model to classify it as either "wildfire cannot occur" or "Yes wildfire can occur".
  * **User-Friendly Interface:** A basic HTML interface for uploading images and displaying results.

## Technologies Used

  * **Flask**: Web framework for the application.
  * **OpenCV (cv2)**: Used for image reading and resizing.
  * **NumPy**: For numerical operations, especially with image data.
  * **TensorFlow & Keras**: For loading and running the deep learning model.
  * **gunicorn**: (Optional) A WSGI HTTP server for deploying the Flask application.
  * **pandas**: (Although listed in `requirements.txt`, it's not directly used in `app.py` based on the provided content).

## Setup and Installation

To get this project up and running on your local machine, follow these steps:

### Prerequisites

  * Python 3.x

### 1\. Clone the repository (if applicable)

If this project is hosted on a repository, clone it to your local machine.

### 2\. Install Dependencies

Navigate to the project directory and install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

The dependencies include: `gunicorn==20.1.0`, `flask==2.2.5`, `numpy>=1.23.4`, `pandas>=2.0.0`, `opencv-python>=4.8.0.74`, `tensorflow>=2.12.0`, and `keras>=2.12.0`.

### 3\. Model File

Ensure you have the trained Keras model file named `test.h5` in the root directory of the project, next to `app.py`. The `app.py` expects to load the model from this path.

### 4\. Run the Application

You can run the Flask application using the built-in development server:

```bash
python app.py
```

The application will typically run on `http://127.0.0.1:5000/`. Open your web browser and navigate to this address.

## Usage

1.  Open your web browser and go to the application's URL (e.g., `http://127.0.0.1:5000/`).
2.  You will see a page with the title "Computer Vision Classification" and a file input field.
3.  Click "Choose File" and select an image file (e.g., `.jpg`, `.png`) from your computer.
4.  Click the "Classify" button.
5.  The application will process the image and display the classification result on a new page, indicating "Predicted Class: wildfire cannot occur" or "Predicted Class: Yes wildfire can occur".

## Project Structure

  * `app.py`: The main Flask application script.
  * `index.html`: The HTML template for the home page where users upload images.
  * `result.html`: The HTML template for displaying the classification result.
  * `requirements.txt`: Lists all Python dependencies required for the project.
  * `test.h5`: The pre-trained deep learning model file (not provided in the context, but inferred from `app.py`).

## Contributions

Feel free to fork the repository and contribute by improving the model, adding new features, or enhancing the UI.

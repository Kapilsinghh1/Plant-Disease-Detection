Plant Disease Detection is a deep learning project that identifies diseases in plant leaves using image classification. The model takes an uploaded image and predicts which plant disease class it belongs to through a Streamlit-based web interface.

Project Overview

This project uses a Convolutional Neural Network trained on images of healthy and diseased plant leaves. The trained model is used in a Streamlit app where users can upload a leaf image and get a prediction instantly.

Model Information

The model was trained on multiple plant leaf classes. It achieved high accuracy during training and validation, making it reliable for basic disease detection tasks.
The final model file is saved as trained_plant_disease_model.keras.

How to Run :

Install dependencies:
pip install -r requirements.txt


Run the Streamlit app:
python -m streamlit run main.py

Make sure the model file is placed in the same folder as main.py.


Project Pipeline (Detailed & Simple)

This project follows a complete end-to-end workflow, starting from dataset preparation to building a working Streamlit application. Below is the detailed pipeline of how the Plant Disease Detection system was developed.

1. Dataset Preparation

A large dataset of plant leaf images was used, containing both healthy and diseased leaves.
The dataset includes more than 38 classes, each representing a specific plant disease or healthy state.
The dataset was divided into:

-> Training images
-> Validation images
->Testing images
->This structure helped in training, monitoring accuracy, and final evaluation.

2. Data Preprocessing

Before training, images were preprocessed so that the model could understand them correctly.
The preprocessing steps included:

-> Resizing all images to 128 × 128 pixels
-> Converting images to NumPy arrays
-> Normalizing pixel values
-> Using data generators to load images in batches

These steps ensured faster training and prevented memory issues.

3. Model Building

A Convolutional Neural Network (CNN) was created using TensorFlow/Keras.
The model was designed to identify patterns and features from leaf images.
The architecture included:

-> Convolution layers
-> Pooling layers
-> Dense layers
Softmax output layer for multi-class classification

4. Model Training

-> The model was trained using:
-> 10 epochs
-> Training data for learning
->Validation data to monitor performance
During training, the model gradually improved in accuracy.
The final model achieved good training and validation accuracy, showing that it learned to recognize different plant diseases effectively.

5. Saving the Model

After training, the model was saved as:
trained_plant_disease_model.keras

This file is used by the Streamlit app to make predictions without retraining the model again.

6. Streamlit Application Development

A user-friendly Streamlit web app was created (main.py) to make the system easy to use.
-> The app allows users to:
-> Upload a plant leaf image
-> View the image
-> Predict the disease class
-> Display the prediction in a clean UI
Streamlit makes the project interactive and accessible without needing deep technical knowledge.

7. Loading the Model in Streamlit

When the app starts, it automatically loads the saved .keras model.
This makes prediction fast and smooth because the model is ready to use immediately.

8. Image Upload & Prediction

When a user uploads an image:
-> The image is resized and preprocessed
-> The model predicts the class index
-> The class index is matched with a disease name
-> The final result is shown to the user
This process happens in real time and gives instant output.


Challenges Faced & How I Solved Them
Challenge 1: Long Training Time

Training the full dataset took a very long time.
Solution:
I created a fast demo version using fewer images and smaller batch sizes. This helped me quickly test the model and demonstrate training without waiting for hours.

Challenge 3: Streamlit Command Not Working

Streamlit was not recognized because the PATH was not set.
Solution:
I used python -m streamlit run main.py, which worked without needing PATH settings.

Challenge 4: GitHub Large File Warning

The model file was large (76MB), and GitHub warned about file size.
Solution:
I checked that the file is under GitHub’s 100MB limit, so uploading it was safe. I also learned about Git LFS for future large files.

What I Learned From This Project :

-> How to build and train a CNN using TensorFlow/Keras
-> How to preprocess images correctly for deep learning
-> How to integrate a trained model with a real-time Streamlit app
-> How to organize project files and prepare them for GitHub
-> How to handle common issues like long training time, path errors, and large file warnings

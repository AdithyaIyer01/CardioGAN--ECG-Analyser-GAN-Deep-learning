# CardioGAN--ECG-Analyser-GAN-Deep-learning
 This project uses a deepfake-ecg model from Pulse2Pulse GAN to generate realistic deepfake ECG images and a CNN-based classifier to categorize ECGs as Normal, Abnormal, or indicative of Myocardial Infarction (MI). The web interface, built with Flask and HTML, allows users to upload ECG images, analyze them, and get instant classification results.

## Table of Contents
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Training Your Own Model](#training-your-own-model)
- [Folder Structure](#folder-structure)
- [Screenshots](#screenshots)

## Installation

1. **Clone the repository**:
Open Terminal and paste the following.
    git clone https://github.com/AdithyaIyer01/CardioGAN--ECG-Analyser-GAN-Deep-learning
    cd CardioGAN--ECG-Analyser-GAN-Deep-learning

2. **Install the required libraries**: 
Navigate to the project directory and run the following command to install all dependencies:
    pip install -r requirements.txt

## Running the Project

To run the project, follow these steps:

1. **Go to the CardioGAN Website**:
Navigate to the CARDIOGAN_WEBSITE directory:
    cd CARDIOGAN_WEBSITE
2. **Run the Flask App**:
Execute the app.py file to start the Flask web application:
    python app.py
3. Using the Website
Once the server starts, open a browser and go to http://127.0.0.1:5000/ (or the URL printed in the terminal). 
You will see a page where you can upload an ECG image of your choice or select one from the DATASET folder.
After uploading the image, click on Analyze to get the classification result: Normal, Abnormal, or MI (Myocardial Infarction).
**Note**:
The convnet2.h5 model file is already included in the project, so no changes are needed to run the app with the pre-trained model.
You can only upload images with jpeg or jpg format.

## Training Your Own Model

If you want to train your own ECG classification model, follow these steps:

1. **Download DeepFake ECG Images**:
Run the DEEPFAKE_ECG_DOWNLOADER.ipynb file to download DeepFake ECG images. This notebook will help you collect data to train the model.

2. **Separate the ECG Images (Optional)**:
If you want to split the images (to separate two ECGs from a single DeepFake image), run the ecg-separate.py file. Provide the input and output directory paths when prompted, and the images will be split accordingly.

3. **Create a Dataset**:
In the project directory, navigate to the Dataset folder. The folder is already structured with train, test, and valid subfolders. Inside each of these subfolders, you will have abnormal, normal, and mi folders.

Add the corresponding images to each folder:
train: Should contain the most images.
valid: Should have fewer images than the train folder.
test: Should have the least images.

4. **Train the Model**:
Use the ECGConvNet1.ipynb file to train your model. Provide the necessary paths for the dataset folder and other configurations when prompted.
After training, save your model as an .h5 file.

5. **Use the Trained Model**:
Replace the pre-trained convnet2.h5 in app.py with your own saved .h5 model file.
    model = tf.keras.models.load_model(r'CARDIOGAN_WEBSITE/convnet2.h5')
When you run the app.py file, the website will use your custom model to classify ECG images.

## Folder Structure

/CardioGAN--ECG-Analyser-GAN-Deep-learning
    ├── CARDIOGAN_WEBSITE/
    │   ├── app.py
    │   ├── convnet2.h5  # Pre-trained model file
    │   ├── templates/
    │   │   └── home.html
    ├── ECG_CLASSIFICATION_CODE/
    │   ├── ECGConvNet1.ipynb  # Model training notebook
    │   ├── convnet2.h5        # Pre-trained model file
    │   ├── Dataset/           # Folder containing train, test, valid datasets
    │   ├── Dataset_training/  # Folder for custom training data
    │   └── ecg-separate.py    # Script to separate ECG images
    ├── requirements.txt
    └── README.md

1. CARDIOGAN_WEBSITE/: Contains Flask app (app.py) and templates for the web application.
2. ECG_CLASSIFICATION_CODE/: Folder containing the model training code (ECGConvNet1.ipynb), the pre-trained model      (convnet2.h5), and dataset-related files.
3. Dataset/: Folder containing subfolders (train, test, valid) to store ECG images for training and validation.
4. Dataset_training/: Folder for storing the custom training data (if you want to use your own).
5. ecg-separate.py: Script to split combined DeepFake ECG images into individual ECGs.
6. ECGConvNet1.ipynb: Jupyter notebook for training the ECG classification model.

## Screenshots

![Home Page](Images/Screenshot%202024-06-11%20204453.png)
1. The home page of CardioGAN website with the upload button.

![Uploaded Image](Images/Screenshot%202024-06-11%20204609.png)
2. The uploaded image displayed to the user.

![ECG Classification](Images/Screenshot%202024-06-11%20204708.png)
3. The ECG classification of the user-uploaded ECG with links to heart disease prevention websites to refer.

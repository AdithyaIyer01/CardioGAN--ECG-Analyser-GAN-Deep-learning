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
   
 - Open Terminal and paste the following.
    ```bash
    git clone https://github.com/AdithyaIyer01/CardioGAN--ECG-Analyser-GAN-Deep-learning
    cd CardioGAN--ECG-Analyser-GAN-Deep-learning

2. **Install the required libraries**:
   
 - Navigate to the project directory and run the following command to install all dependencies:
    ```bash
    pip install -r requirements.txt

## Running the Project

To run the project, follow these steps:

1. **Go to the CardioGAN Website**:
  - Navigate to the CARDIOGAN_WEBSITE directory:
    cd CARDIOGAN_WEBSITE
2. **Run the Flask App**:
  - Execute the app.py file to start the Flask web application:
    python app.py
3. Using the Website
  Once the server starts, open a browser and go to http://127.0.0.1:5000/ (or the URL printed in the terminal). 
  You will see a page where you can upload an ECG image of your choice or select one from the DATASET folder.
  After uploading the image, click on Analyze to get the classification result: Normal, Abnormal, or MI (Myocardial Infarction).
**Note**:
 - The convnet2.h5 model file is already included in the project, so no changes are needed to run the app with the pre-trained model.
 - You can only upload images with jpeg or jpg format.

## Training Your Own Model

Follow these steps to train your own ECG classification model:

1. **Download DeepFake ECG Images**  
   Run the `DEEPFAKE_ECG_DOWNLOADER.ipynb` file to download DeepFake ECG images. This notebook will help you collect the data required to train the model.

2. **Separate the ECG Images (Optional)**  
   If the downloaded images contain two ECGs in a single image, you can split them using the `ecg-separate.py` file.  
   - Provide the input and output directory paths when prompted.  
   - The script will split the combined images into individual ECG images.

3. **Create a Dataset**  
   Navigate to the `Dataset` folder in the project directory. This folder is pre-structured with subfolders for training, testing, and validation:  
   - **train/**: For storing the majority of images used in training.  
   - **valid/**: For storing a smaller number of images used for validation.  
   - **test/**: For storing the fewest images used for testing.  

   Inside each of these subfolders, you will find subdirectories for the three classes: `abnormal`, `normal`, and `mi`. Add images corresponding to these classes into the respective subdirectories.

4. **Train the Model**  
   Use the `ECGConvNet1.ipynb` file to train your custom model:  
   - Update the dataset paths and configurations as needed.  
   - Train the model using the images in the `Dataset` folder.  
   - Once training is complete, save the model as an `.h5` file.

5. **Use the Trained Model**  
   Replace the pre-trained `convnet2.h5` file in the `app.py` script with your custom-trained `.h5` model file:  
   ```python
   model = tf.keras.models.load_model(r'CARDIOGAN_WEBSITE/convnet2.h5')


## Folder Structure

1. **CARDIOGAN_WEBSITE/**  
   This folder contains the main Flask application files:
   - `app.py`: The Flask application script to run the website.
   - `templates/`: Contains HTML files for the web application's user interface.

2. **ECG_CLASSIFICATION_CODE/**  
   This folder holds the code and resources for ECG classification:
   - `ECGConvNet1.ipynb`: Jupyter notebook for training the ECG classification model.
   - `convnet2.h5`: Pre-trained model used for classifying ECG images.
   - Dataset-related files for training and validation.

3. **Dataset/**  
   Directory structured into subfolders for organizing ECG images:
   - `train/`: Contains training images for the model.
   - `test/`: Holds test images for evaluation.
   - `valid/`: Contains validation images to fine-tune the model.

4. **Dataset_training/**  
   This folder is for storing custom training data if you wish to use your own images for training.

5. **ecg-separate.py**  
   A Python script to process and split combined DeepFake ECG images into individual ECG images.

6. **ECGConvNet1.ipynb**  
   A Jupyter notebook used to train a custom ECG classification model.


## Screenshots

![Home Page](Images/Screenshot%202024-06-11%20204453.png)
1. **The home page of CardioGAN website with the upload button.**

![Uploaded Image](Images/Screenshot%202024-06-11%20204609.png)
2. **The uploaded image displayed to the user.**

![ECG Classification](Images/Screenshot%202024-06-11%20204708.png)
3. **The ECG classification of the user-uploaded ECG with links to heart disease prevention websites to refer.**

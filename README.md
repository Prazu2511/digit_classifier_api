# Digit Classifier API

A robust application for digit recognition from images, leveraging a Random Forest Classifier trained on the MNIST dataset. This API, built using FastAPI, offers a simple and efficient interface for predicting handwritten digits.

## Table of Contents
1. [Introduction](#introduction)  
2. [Features](#features)  
3. [App Architecture](#app-architecture)  
4. [Installation Instructions](#installation-instructions)  
5. [Usage Instructions](#usage-instructions)  
6. [Challenges Faced](#challenges-faced)  
7. [Future Scope](#future-scope)  
8. [Results](#results)  
9. [Conclusion](#conclusion)

---

## Introduction

The **Digit Classifier API** is designed for recognizing handwritten digits from grayscale images. It features:  
- A **Random Forest Classifier**, trained on the MNIST dataset.  
- A lightweight and user-friendly RESTful API built using **FastAPI**.  

The API provides two primary functionalities:
- **Root Endpoint**: Displays a welcome message.  
- **Prediction Endpoint**: Accepts an image and predicts the digit.

---

## Features

- **Training Dataset**: MNIST, containing 28x28 grayscale images of digits (0-9).  
- **Preprocessing**: Input images are resized and inverted for model compatibility.  
- **Model**: Random Forest Classifier trained and stored as `mnist_model.pkl`.  
- **Performance**: High accuracy on the MNIST test dataset.

---

## App Architecture

- **Endpoints**:  
  - `/`: Welcome endpoint.  
  - `/predict-image/`: Accepts an image file and returns the digit prediction.  
- **Backend Framework**: FastAPI.  
- **Model Serving**: scikit-learn.  
- **Deployment Tool**: Uvicorn (ASGI server).

---

## Installation Instructions

### Pre-requisites
1. Python (version 3.8 or higher).  
2. Required libraries (install using `requirements.txt`).  

### Steps
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
2. Ensure the pre-trained model mnist_model.pkl is available in the project directory.
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
4. Run the API server:
   ```bash
   uvicorn main:app --reload
5. Access the API documentation at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

---

## Usage Instructions

### Starting the API
1. Run the FastAPI server:
    ```bash
   uvicorn main:app --reload
2. Access the API at: [http://127.0.0.1:8000].

### Interacting with Endpoints
- **Welcome Endpoint (/)**: Displays a welcome message.
- **Prediction Endpoint (/predict-image/)**: Accepts a grayscale image and returns the
digit prediction in JSON format.

---

## Challenges Faced

- **Model Performance:** Balancing prediction accuracy with inference speed. Random Forest was selected for its simplicity and high accuracy, but tuning its parameters for optimal performance required extensive experimentation.
- **Image Preprocessing:** Managing diverse input image formats and resolutions. A preprocessing pipeline was developed to ensure compatibility with the model while maintaining prediction accuracy.
- **API Scalability:** Ensuring the FastAPI server could handle concurrent requests efficiently without degrading performance.

---

## Future Scope

- **Enhanced Model:** Incorporating advanced deep learning techniques like Convolutional Neural Networks (CNNs) to improve accuracy and handle complex datasets.
- **Web Interface:** Developing a user-friendly frontend for seamless interaction with the API.
- **Real-Time Deployment:** Extending functionality to include live digit recognition from video feeds or camera inputs.
- **Support for Multilingual Numerals:** Expanding the API's scope to recognize handwritten digits in different numeral systems (e.g., Roman, Arabic).

---
## Results

### Testing Scenarios

- **Input Image:** A well-defined grayscale image of the digit "8".
  **Prediction:** 8

- **Input Image:** A slightly blurred image of the digit "4".
  **Prediction:** 4

- **Input Image:** A high-contrast image of the digit "9".
  **Prediction:** 9

---

## Conclusion

The Digit Classifier API exemplifies the practical application of machine learning for real-world digit recognition tasks. It successfully integrates a trained model with a robust API, offering a seamless user experience for predicting handwritten digits. The use of FastAPI ensures scalability and flexibility, making it suitable for various use cases.
Future iterations of this project could incorporate deeper models, enhanced features, and a web-based interface to expand its usability and reach.





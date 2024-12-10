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

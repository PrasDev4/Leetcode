# Shipment Delay Prediction API

This project predicts whether a shipment will be delayed based on input features like distance, origin, destination, weather conditions, traffic conditions, and more. The model is built using a **Logistic Regression Classifier**, trained on historical shipment data, and exposed via a REST API built with **Flask**.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Why Logistic Regression?](#why-logistic-regression)
3. [Features](#features)
4. [Tech Stack](#tech-stack)
5. [Setup Instructions](#setup-instructions)
6. [Usage Instructions](#usage-instructions)
7. [API Details](#api-details)
8. [Examples](#examples)
9. [License](#license)

## Project Overview

The purpose of this project is to provide a tool for predicting shipment delays to optimize logistics and improve customer satisfaction. It allows users to input shipment details and receive a prediction on whether the shipment will be delayed or not.

## Why Logistic Regression?

Logistic Regression was chosen for its simplicity, interpretability, and efficiency. It provides clear insights into feature impacts, is computationally lightweight, and delivers high accuracy comparable to Random Forest. Its suitability for smaller datasets and low risk of overfitting make it ideal for this problem.

## Features

- Predicts shipment delays based on:
  - Distance
  - Origin and destination
  - Vehicle type
  - Weather and traffic conditions
  - Day of the week and month
- Exposes the prediction functionality via a REST API.
- Supports JSON input for easy integration.

## Tech Stack

- **Python**: Data preprocessing, model training, and API development.
- **Flask**: Building the API.
- **Postman**: Testing the API.
- **Pandas**: Data manipulation and preparation.
- **Seaborn & Matplotlib**: Data visualization.

## Setup Instructions

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/Shipment-Delay-Prediction.git
   cd Shipment-Delay-Prediction
2. Install the dependencies:
   ```bash
    pip install -r requirements.txt
3. Run the Flask app:
   ```bash
   python app.py

4.Usage Instructions

Input Format
Send a POST request to the /predict endpoint with the following JSON structure:
  ```bash
{
    "Origin": "Delhi",
    "Destination": "Mumbai",
    "Distance (km)": 1400,
    "Vehicle Type": "Truck",
    "Weather Conditions": "Rain",
    "Traffic Conditions": "Moderate",
    "Day of Week": 3,
    "Month": 12,
    "Delivery Time": 48
}


Output Format
The API returns a JSON response:
```bash
{
    "Delay": "Yes"
}

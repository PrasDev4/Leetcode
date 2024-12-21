from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('shipment_model.pkl')

# Define the feature names used during training
feature_names = [
    'Distance (km)', 'Origin_Bangalore', 'Origin_Chennai', 'Origin_Delhi', 
    'Origin_Hyderabad', 'Origin_Jaipur', 'Origin_Kolkata', 'Origin_Lucknow', 
    'Origin_Mumbai', 'Origin_Pune', 'Destination_Bangalore', 
    'Destination_Chennai', 'Destination_Delhi', 'Destination_Hyderabad', 
    'Destination_Jaipur', 'Destination_Kolkata', 'Destination_Lucknow', 
    'Destination_Mumbai', 'Destination_Pune', 'Vehicle Type_Lorry', 
    'Vehicle Type_Trailer', 'Vehicle Type_Truck', 'Weather Conditions_Fog', 
    'Weather Conditions_Rain', 'Weather Conditions_Storm', 
    'Traffic Conditions_Light', 'Traffic Conditions_Moderate', 
    'Day of Week', 'Month', 'Delivery Time'
]

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    
    # Initialize a DataFrame with all zeros
    input_data = pd.DataFrame([[0] * len(feature_names)], columns=feature_names)
    
    # Map origin and destination to the appropriate feature columns
    origin = data.get('Origin', '').capitalize()
    destination = data.get('Destination', '').capitalize()
    
    if f'Origin_{origin}' in feature_names:
        input_data[f'Origin_{origin}'] = 1
    if f'Destination_{destination}' in feature_names:
        input_data[f'Destination_{destination}'] = 1

    # Set other features based on the input data
    input_data['Distance (km)'] = data.get('Distance (km)', 0)
    input_data[f"Vehicle Type_{data.get('Vehicle Type', '').capitalize()}"] = 1
    input_data[f"Weather Conditions_{data.get('Weather Conditions', '').capitalize()}"] = 1
    input_data[f"Traffic Conditions_{data.get('Traffic Conditions', '').capitalize()}"] = 1
    input_data['Day of Week'] = data.get('Day of Week', 0)
    input_data['Month'] = data.get('Month', 0)
    input_data['Delivery Time'] = data.get('Delivery Time', 0)
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Return the prediction
    return jsonify({'Delay': 'Yes' if prediction[0] == 1 else 'No'})

if __name__ == '__main__':
    app.run(debug=True)

#Import innitial dependencies
from flask import Flask, render_template, redirect, url_for, jsonify
from flask_pymongo import PyMongo
import json
import warnings
warnings.simplefilter('ignore')
import base64
import numpy as numpy
import io
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.utils import to_categorical
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder
from keras.callbacks import EarlyStopping
from keras import backend as K
from keras.models import model_from_json

# Read the csv file into a pandas DataFrame
dataset = pd.read_csv('../data/ModelData_1.csv')

app = Flask(__name__)

def get_model():
    json_file = open('modelD1.h5', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("modelD1.h5")
print("Loaded modelD1 from disk")
get_model()

def preprocess_recipe():
    X_test, y_test = train_test_split(X, y, random_state=1, stratify=y)
    X_test_scaled = X_scaler.transform(X_test)

    label_encoder = LabelEncoder()
    encoded_y_test = label_encoder.transform(y_test)
    y_test_categorical = to_categorical(encoded_y_test)
    
    # load json and create model
    json_file = open('modelD1.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("modelD1.h5")
   
    loaded_model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
    encoded_predictions = loaded_model.predict_classes(X_test_scaled[:5])
    prediction_labels = label_encoder.inverse_transform(encoded_predictions)
    print(f"Predicted classes: {prediction_labels}")
    print(f"Actual Labels: {list(y_test[:5])}")
    
 

@app.route("/predict", methods=["POST"])
def predict():
    message = request.get_json(force=True)




if __name__ == "__main__":
    app.run(debug=True, port=7000)
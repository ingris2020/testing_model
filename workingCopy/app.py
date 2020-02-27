from flask import Flask, render_template, redirect, url_for, jsonify
from flask_pymongo import PyMongo
import json
import os
#Model Dependencies
import warnings
warnings.simplefilter('ignore')
import base64
import numpy as numpy
import io
import pandas as pd
from sklearn import preprocessing
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
from keras.models import load_model


app = Flask(__name__)

def get_model():
    global model
    model = load_model("modelD1.h5")
    print("*Model Loaded")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/json")
def renderAllRecipes():
    filename = os.path.join('static', 'data', 'fix_HealthyAll2.json')
    with open(filename) as recipe_file:
        data = json.load(recipe_file)
        print(data)
        return jsonify(data)

def analyze_nutrients(total_nutrients):

    # Extract the nutrient values from the JSON
    try: 
        Servings = 1
        Calories = total_nutrients['ENERC_KCAL']['quantity']
        Fat  = total_nutrients['FAT']['quantity']
        Sat_Fat = total_nutrients['FASAT']['quantity']
        Trans_Fat = total_nutrients['FATRN']['quantity']
        Mono_Fat = total_nutrients['FAMS']['quantity']
        Poly_Fat = total_nutrients['FAPU']['quantity']
        Carbs = total_nutrients['CHOCDF']['quantity']
        Fiber = total_nutrients['FIBTG']['quantity']
        Sugar = total_nutrients['SUGAR']['quantity']
        Protein = total_nutrients['PROCNT']['quantity']
        Cholesterol = total_nutrients['CHOLE']['quantity']
        Sodium = total_nutrients['NA']['quantity']
        Calcium = total_nutrients['CA']['quantity']
        Magnesium = total_nutrients['MG']['quantity']
        Potassium = total_nutrients['K']['quantity']
        Iron = total_nutrients['FE']['quantity']
        Zinc = total_nutrients['ZN']['quantity']
        Phosphorus= total_nutrients['P']['quantity']
        Vit_A= total_nutrients['VITA_RAE']['quantity']
        Vit_C = total_nutrients['VITC']['quantity']
        B1 = total_nutrients['THIA']['quantity']
        B2 = total_nutrients['RIBF']['quantity']
        B3 = total_nutrients['NIA']['quantity']
        B6 = total_nutrients['VITB6A']['quantity']
        Folate_eq = total_nutrients['FOLDFE']['quantity']
        Folate_food = total_nutrients['FOLFD']['quantity']
        B12 = total_nutrients['VITB12']['quantity']
        Vit_D = total_nutrients['VITD']['quantity']
        Vit_E = total_nutrients['TOCPHA']['quantity']
        Vit_K = total_nutrients['VITK1']['quantity']
        Water = total_nutrients['WATER']['quantity']   
    except:
        # If a recipe is missing data, it will return here instead of trying to run the model
        return -1

    # Organize the nutrient values into an array with the proper dimensions
    print("Function: analyze_nutrients(total_nutrients):")
    print("   Building input array X ...")
    X = numpy.array([Servings, Calories, Fat, Sat_Fat, Trans_Fat, Mono_Fat, Poly_Fat, Carbs, Fiber, Sugar, Protein, Cholesterol, Sodium, Calcium, Magnesium, Potassium, Iron, Zinc, Phosphorus, Vit_A, Vit_C, B1, B2, B3, B6, Folate_eq, Folate_food, B12, Vit_D, Vit_E, Vit_K, Water])
    X = X.reshape(-1, 1)
    print(f"   Shape of X: {X.shape}")

    # Scale and normalize the results
    scaler = preprocessing.StandardScaler()
    print("   Standardizing the values in X ...")
    standardized_data = scaler.fit_transform(X)
    print(standardized_data)
    standardized_data = numpy.transpose(standardized_data)
    print(f"   Shape of standardized_data: {standardized_data.shape}")


    # Import and run the model
    print("   Importing the model ...")
    model = tf.keras.models.load_model("model_new.h5")
    print("   Model imported.")
    prediction = model.predict_classes(standardized_data)
    print(f"   Prediction: {prediction}")
    print("End Function: analyze_nutrients(total_nutrients)")

    return prediction[0]

@app.route("/recipe/<recipe_name>")
def recipe(recipe_name):
    print(f"Received request for {recipe_name} ...")

    filename = os.path.join('static', 'data', 'fix_HealthyAll2.json')
    with open(filename) as blog_file:
        foods = json.load(blog_file)       

        for food in foods:
            if food['recipe']['label'] == recipe_name:
                total_nutrients = food['recipe']['totalNutrients']
                result = analyze_nutrients(total_nutrients)

                # Decide which label to return; Error is returned if the recipe was missing nutrition data
                label = "Error in nutrient data"
                if result == 1:
                    label = "Healthy"
                elif result == 0:
                    label = "Unhealthy"
                
                print(f"{recipe_name} is {label}")

                return jsonify(label)
           
        return jsonify("Not found")


if __name__ == "__main__":
    app.run(debug=True, port=7000)
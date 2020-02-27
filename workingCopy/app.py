from flask import Flask, render_template, redirect, url_for, jsonify
from flask_pymongo import PyMongo
import json
import os
#import predict_app

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
#app.config["MONGO_URI"] = "mongodb://localhost:27017/recipe_app" 
#mongo = PyMongo(app)


@app.route("/")
def index():
    #recipe = mongo.db.recipe.find_one()
    return render_template("index.html")

@app.route("/get_model")
def model():
   
    return redirect("/", code=302)


@app.route("/json")
def renderAllRecipes():
    filename = os.path.join('static', 'data', 'AllRecipes.json')
    with open(filename) as blog_file:
        data = json.load(blog_file)
        print(data)
        return jsonify(data)

def analyze_nutrients(total_nutrients):
    Servings = 1
    Calories = total_nutrients['ENERC_KCAL']['quantity']
    Fat  = total_nutrients['FAT']['quantity']
    Sat_Fat = total_nutrients['FATSAT']['quantity']
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
    

    # X = [calories, sodium]
    X = [Servings, Fat, Sat_Fat, Trans_Fat, Mono_Fat, Poly_Fat, Carbs, Fiber, Sugar, Protein, Cholesterol, Sodium, Calcium, Magnesium,	Potassium, Iron, Zinc, Phosphorus, Vit_A, Vit_C, B1, B2, B3, B6, Folate_eq, Folate_food, B12, Vit_D, Vit_E, Vit_K, Water]

    # Run your model
    healthy = True

    return healthy

@app.route("/recipe/<recipe_name>")
def recipe(recipe_name):
    filename = os.path.join('static', 'data', 'AllRecipes.json')
    with open(filename) as blog_file:
        foods = json.load(blog_file)
        print(foods)
        
        for food in foods:
            if food['recipe']['label'] == recipe_name:
                total_nutrients = food['recipe']['totalNutrients']
                result = analyze_nutrients(total_nutrients)
                return jsonify(result)

        ##food = data.filter(fd => fd.label == recipe_name)
            
        return jsonify("Not found")


if __name__ == "__main__":
    app.run(debug=True, port=7000)
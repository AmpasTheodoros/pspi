# BEGIN CODE HERE
from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import TEXT
import numpy as np
from selenium import webdriver
# END CODE HERE

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/pspi"
CORS(app)
mongo = PyMongo(app)
mongo.db.products.create_index([("name", TEXT)])

@app.route("/search", methods=["GET"])
def search():
    # BEGIN CODE HERE
    products = mongo.db.products.find()
    result = []
    for product in products:
        result.append({
            "id": str(product["_id"]),
            "name": product["name"],
            "production": product["production"],
            "price": product["price"],
            "color": product["color"],
            "size": product["size"]
        })

    return jsonify(result)
    # END CODE HERE


@app.route("/add-product", methods=["POST"])
def add_product():
    # BEGIN CODE HERE
    product = request.json
    mongo.db.products.insert_one(product)
    return jsonify({"message": "Product added successfully"})
    # END CODE HERE


@app.route("/content-based-filtering", methods=["POST"])
def content_based_filtering():
    # BEGIN CODE HERE
    product_id = request.json["product_id"]
    product = mongo.db.products.find_one({"_id": product_id})
    if not product:
        return jsonify({"error": "Product not found"})
    similar_products = []
    return jsonify(similar_products)
    # END CODE HERE


@app.route("/crawler", methods=["GET"])
def crawler():
    # BEGIN CODE HERE
    try:
        semester = request.args.get("semester")
        url = "https://qa.auth.gr/el/x/studyguide/600000438/current"
        options = webdriver.Chrome.options.Options()
        # does not apper as window
        options.headless = True
        # setting a chrome browser
        driver = webdriver.Chrome(options=options)
        # goes to the specified url
        driver.get(url)
        driver.switch_to.frame(driver.find_element(webdriver.common.by.By.ID, "exams" + str(semester)))
        driver.switch_to.frame("2")
        res = []
        for element in driver.find_elements(webdriver.common.by.By.xpath("./child::*")):
            #takes the text from the paragraph tags
            res.append(element.get_attribute("coursetitle"))
        return jsonify(res)
    except Exception:
        return "BAD REQUEST", 400
    # END CODE HERE

if __name__ == "__main__":
    app.run()

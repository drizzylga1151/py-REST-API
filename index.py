import flask,pg8000,methods, os
from flask import request, jsonify, render_template

CATS_FOLDER = os.path.join('static', 'cats')
DOGS_FOLDER = os.path.join('static', 'dogs')

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config['UPLC_FOLDER'] = CATS_FOLDER
app.config['UPLD_FOLDER'] = DOGS_FOLDER
 
@app.route("/cat", methods=['GET'])
def api_cat():

    filename = methods.getcat()
    cat = os.path.join(app.config["UPLC_FOLDER"], filename)

    return render_template("image.html", user_image = cat)

@app.route("/dog", methods=["GET"])
def api_dog():

    filename = methods.getdog()
    dog = os.path.join(app.config["UPLD_FOLDER"], filename)

    return render_template("image.html", user_image = dog)

    
app.run('localhost',8080)


import os,random

def getcat():
    cats = os.listdir("./static/cats")

    cat = random.choice(cats)

    return cat

def getdog():

    dogs = os.listdir("./static/dogs")

    dog = random.choice(dogs)

    return dog


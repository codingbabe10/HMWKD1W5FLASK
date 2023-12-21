from flask import Flask

app = Flask(__name__)

users = {
    '1': {
        'username': 'BrendaSmith',
        'email':'BrendaSmith@aol.com'
    },
    '2': {
        'username': 'BarryCraige',
        'email': 'BarryCraige@aol.com'
    }
}

recipes = {
        '1': {
        'body' : ' Learn Delicious Recipes',
        'user_id' : '1'
    },
    '2' : {
        'body' : "Select a recipe you would like to try.",
        'user_id' : '2'
    },
    '3' : {
        'body': '5 star reviews!!!!',
        'user_id' : '1'

    }     #1. Recipe Theme. 2.key-pairs ingredients. Instructions
}         #3. CRUD operations ( create, read, update, delete)

@app.route('/recipes')
def get_recipes():
    return{'recipes': list(recipes.values())}



from flask import Flask, request
from uuid import uuid4

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
        '1' : {
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
}         #3. CRUD operations ( create, - GET,  read - PUT , update, delete)

@app.route('/user', methods=['GET'])
def user():
    return{'users': list(users.values())}, 200

@app.route('/user', methods=["POST"])
def create_user():
    json_body = request.get_json()
    users[uuid4()] = json_body
    return {'message' : f'{json_body["username"]} created'}, 201

@app.put('/user')
def update_user():
    return

@app.delete('/user')
def delete_user():
    pass

# recipe routes

@app.get('/Fennle_rhuberb_salad')
def get_posts():
    return

@app.post('/Tomato_bisque')
def create_post():
    return


@app.put('/Rosemary_filet_mignon')
def update_post():
    return

@app.delete('/Indian_lamb_stew')
def delete_post():
    return





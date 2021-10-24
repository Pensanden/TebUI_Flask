#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask,request,jsonify
from flask_mongoengine import MongoEngine

# Init app 
app = Flask(__name__)

# Init db
app.config['MONGODB_SETTINGS'] = {
    "db" : "UITeb"
}
db = MongoEngine(app)

# Models
class User(db.Document):
    name = db.StringField(required=False)
    username = db.StringField(required=True,unique=True)
    calls = db.IntField(default=0)

# Endpoints
@app.route('/api/v1/user',methods=['POST'])
def add_user():
    name = request.json['name']
    username = request.json['username']
    User(name=name,username=username,calls=0).save()
    return jsonify(User.objects(username=username).get())

@app.route('/api/v1/user',methods=['GET'])
def get_all_users():
    list_of_users = []
    for user in User.objects:
        list_of_users.append(user)        
    return jsonify(list_of_users)

@app.route('/api/v1/user/<username>',methods=['GET'])
def get_single_user(username):
    selected_user = User.objects.get_or_404(username=username)
    return jsonify(selected_user)
    
@app.route('/api/v1/user/<username>',methods=['PUT'])
def rename_user(username):
    selected_user = User.objects.get_or_404(username=username)
    changed_name = request.json['name']
    selected_user.update(set__name=changed_name)
    renamed_user = User.objects(username=username)
    return jsonify(renamed_user)

# Run Server 
if __name__ == '__main__':
    app.run(debug=True)


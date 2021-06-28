
from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session 
from flask import Response,send_file

app = Flask(__name__)

import db as db

@app.route('/')
def index():
    
    return None

@app.route('/adduser',methods = ['GET','POST'])
def add_user():
    request_data = request.json
    email = request_data["email"]
    firstname = request_data["firstname"]
    lastname = request_data["lastname"]
    password = request_data["password"]
    db.add_user(email,firstname,lastname,password)
    response = Response("User added", 200, mimetype='application/json')
    return response

@app.route('/users',methods = ['GET'])
def get_all_users():
        details = {'Users':db.get_all_users()}
        print(details)
        #for detail in details:
         #   var = detail
        #return render_template('index.html',var=details)
        return details
@app.route('/user/<email>', methods=['GET'])
def get_user(email):
    print("hello im working")
    user_details=db.get_user(email)
    if user_details == None:
        return "User not found"
    return user_details

@app.route('/user/<email>', methods=['PUT'])
def update_user(email):

    request_data = request.get_json()
    email = request_data["email"]
    firstname = request_data["firstname"]
    lastname = request_data["lastname"]
    password = request_data["password"]
    db.update_user(email,firstname,lastname,password)
    response = Response("User Updated", status=200, mimetype='application/json')
    return response

@app.route('/user/<email>',methods=['DELETE'])

def delete_user(email):
    db.delete_user(email)
    response = Response("User deleted", status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    
    app.run(debug=True)

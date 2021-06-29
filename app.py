
from flask import Flask, render_template, request, flash, redirect,url_for, jsonify, session 
from flask import Response,send_file
from email_validator import validate_email, EmailNotValidError
from string import *
app = Flask(__name__)

import db as db

@app.route('/')
def index():
    
    return '{ "Message":"welcome"}'

@app.route('/adduser',methods = ['GET','POST'])
def add_user():
    request_data = request.json
    email = request_data["email"].strip()
    firstname = request_data["firstname"].strip()
    lastname = request_data["lastname"].strip()
    password = request_data["password"].strip()
    if email == "" or firstname == "" or lastname == "" or password == "":
        response = Response("All fields are mandatory", 400, mimetype='application/json')
        return response
    try:
        valid = validate_email(email)
        email = valid.email
    except EmailNotValidError as e:
        response = Response("Enter valid email.", 400, mimetype='application/json')
        return response 
    err=db.add_user(email,firstname,lastname,password)
    if err:
        response = Response("User already exists or try with other email id", 400, mimetype='application/json')
        return response 
    response = Response("User added", 200, mimetype='application/json')
    return response

@app.route('/users',methods = ['GET'])
def get_all_users():
        details = {'Users':db.get_all_users()}
        if details == None or "" or {}:
            response = Response("No Users found.", 404, mimetype='application/json')
            return response
        return details
@app.route('/user/<email>', methods=['GET'])
def get_user(email):
    user_details=db.get_user(email)
    if user_details == None:
        response = Response("No User found.", 404, mimetype='application/json')
        return response
    return user_details

@app.route('/user/<email>', methods=['PUT'])
def update_user(email):
    
    user_details=db.get_user(email)
    if user_details == None:
        response = Response("User not found to update.", 404, mimetype='application/json')
        return response
    request_data = request.get_json()
    email = request_data["email"].strip()
    firstname = request_data["firstname"].strip()
    lastname = request_data["lastname"].strip()
    password = request_data["password"].strip()
    if email == "" or firstname == "" or lastname == "" or password == "":
        response = Response("All fields are mandatory", 400, mimetype='application/json')
        return response
    try:
        valid = validate_email(email)
        email = valid.email
    except EmailNotValidError as e:
        response = Response("Enter valid email.", 400, mimetype='application/json')
        return response 
    db.update_user(email,firstname,lastname,password)
    response = Response("User Updated", status=200, mimetype='application/json')
    return response

@app.route('/user/<email>',methods=['DELETE'])

def delete_user(email):
    
    user_details=db.get_user(email)
    if user_details == None:
        response = Response("User not found to delete.", 404, mimetype='application/json')
        return response
    db.delete_user(email)
    response = Response("User deleted", status=200, mimetype='application/json')
    return response


if __name__ == "__main__":
    
    app.run(debug=True)

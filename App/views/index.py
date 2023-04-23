from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import *
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
import os
import http.client
import json
import re

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('login.html')

@index_views.route('/home', methods=['GET'])
@login_required
def exercises():

    page = request.args.get('page', default=1, type=int) 

    
    per_page = 12  
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page

    conn = http.client.HTTPSConnection("musclewiki.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "09f6b51864msh4bb31a9d8466b4bp1a4a5cjsnf805f9baa416",
        'X-RapidAPI-Host': "musclewiki.p.rapidapi.com"
    }
    #Get exercises for main list
    conn.request("GET", "/exercises", headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    exercise = json.loads(data)

    exercise_slice = exercise[start_idx:end_idx]

    #Get attributes for filter
    conn.request("GET", "/exercises/attributes", headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    attribute = json.loads(data)

   

    
        
    return render_template('index.html', exercises=exercise_slice, page=page, attributes=attribute)
   
@index_views.route('/workouts/<workout>', methods=['GET'])
@login_required
def getSearchWorkouts(workout):

    page = request.args.get('page', default=1, type=int) 

    per_page = 12  
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page

    workout = re.sub(r"\s", "%20", workout.rstrip())
    conn = http.client.HTTPSConnection("musclewiki.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "62ef012002msh9f081cf263c1a11p1bf1e1jsn5ff435659594",
        'X-RapidAPI-Host': "musclewiki.p.rapidapi.com"
        }

    #Get exercises for main list
    conn.request("GET", "/exercises?name=" + workout, headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    exercise = json.loads(data)

    exercise_slice = exercise[start_idx:end_idx]

    #Get attributes for filter
    conn.request("GET", "/exercises/attributes", headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    attribute = json.loads(data)



    return render_template('index.html', exercises=exercise_slice, page=page, attributes=attribute)


@index_views.route('/muscles/<muscle>', methods=['GET'])
@login_required
def getWorkoutsForMuscle(muscle):

    page = request.args.get('page', default=1, type=int) 

    muscle = re.sub(r"\s", "%20", muscle.rstrip())
    per_page = 12  
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page

    conn = http.client.HTTPSConnection("musclewiki.p.rapidapi.com")
    headers = {
        'X-RapidAPI-Key': "09f6b51864msh4bb31a9d8466b4bp1a4a5cjsnf805f9baa416",
        'X-RapidAPI-Host': "musclewiki.p.rapidapi.com"
    }
    #Get exercises for main list
    conn.request("GET", "/exercises?muscle="+muscle, headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    exercise = json.loads(data)

    exercise_slice = exercise[start_idx:end_idx]

    #Get attributes for filter
    conn.request("GET", "/exercises/attributes", headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")
    attribute = json.loads(data)


    


    return render_template('index.html', exercises=exercise_slice, page=page, attributes=attribute)
   

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    #db.create_all()
    #create_user('bob', 'bobpass')
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})


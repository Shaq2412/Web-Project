from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import LoginManager, login_required, login_user, current_user, logout_user
from App.controllers import *
from.index import index_views

import http.client
import json

workouts_views = Blueprint('workouts_views', __name__, template_folder='../templates')
index_views = Blueprint('index_views', __name__, template_folder='../templates')

@workouts_views.route('/myWorkouts', methods=['GET'])
@login_required
def myWorkouts():
    routines = get_all_routines_json(current_user.id)

    show= "no"
    if not routines:
        return render_template('workouts.html')
    
    return render_template('workouts.html', routines = routines, show = show)

@workouts_views.route('/addRoutine', methods=['POST'])
@login_required
def addRoutine():
    data = request.form
    userId = current_user.id
    title = data['title']

    add_routine(title,current_user.id)
    #print("Id: " + str(current_user.id))

    return redirect('/myWorkouts')

@workouts_views.route('/addDay', methods=['POST'])
@login_required
def addDay():
    data = request.form

    title = data['day']
    routineId = data['routineId']

    add_day(title, routineId)
    
    return redirect('/myWorkouts/'+ str(routineId))

@workouts_views.route('/myWorkouts/<routineId>', methods=['GET'])
@login_required
def viewRoutine(routineId):
    
    show = "yes"
    
    routines = get_all_routines_json(current_user.id)
    days = get_all_days_json(routineId)
    
    if not days:
        print("none")
    
    workouts = get_all_json()

    if not workouts:
        workouts=[]
        print("no workouts")

    if days:
        return render_template('workouts.html', routines = routines, show=show, routineId = routineId, days = days, workouts=workouts)
    
    else:
        return render_template('workouts.html',routines = routines, show=show, routineId = routineId)


@workouts_views.route('/addWorkout/<exerciseId>', methods=['GET'])
@login_required
def addWorkoutPage(exerciseId):

    conn = http.client.HTTPSConnection("musclewiki.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "09f6b51864msh4bb31a9d8466b4bp1a4a5cjsnf805f9baa416",
        'X-RapidAPI-Host': "musclewiki.p.rapidapi.com"
    }

    conn.request("GET", "/exercises/"+ exerciseId, headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    exercise = json.loads(data)

    #Get routines for add
    routines = get_all_routines_json(current_user.id)
    if not routines:
        routines = []

    #Get Days for add
    #days = get_days_json()

    #if not days:
    #    print("none")
    #    days = []
    show="no"

    return render_template('addWorkout.html', exercise=exercise, routines = routines, show=show)

@workouts_views.route('/addWorkout/routine<routineId>/<exerciseId>', methods=['GET'])
@login_required
def selectDay(routineId, exerciseId):
   
    conn = http.client.HTTPSConnection("musclewiki.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "09f6b51864msh4bb31a9d8466b4bp1a4a5cjsnf805f9baa416",
        'X-RapidAPI-Host': "musclewiki.p.rapidapi.com"
    }

    conn.request("GET", "/exercises/"+ exerciseId, headers=headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    exercise = json.loads(data)

    show = "yes"
    #Get Days for add
    days = get_all_days_json(routineId)

    if not days:
        print("none")
        days = []

    
    return render_template('addWorkout.html', exercise=exercise, days=days, show=show, routineId = routineId)


@workouts_views.route('/addWorkout', methods=['POST'])
@login_required
def addWorkout():
    data = request.form

    workoutName = data['workoutName']
    videoURL = data['videoUrl']
    category = data['category']
    primaryTarget = data['primaryTarget']
    dayId = data['dayId']
    routineId= data['routineId']
    
    add_workout(workoutName, videoURL, category, primaryTarget, dayId)    

    return redirect('/myWorkouts/'+ routineId)

@workouts_views.route('/removeWorkout/<workoutId>', methods=['GET'])
@login_required
def removeWorkout(workoutId):

    if delete_workout(workoutId):
        flash('Workout Removed')
        return redirect('/myWorkouts')
    
    else:
        flash('Delete Unsuccessful')
        return redirect('/myWorkouts')

@workouts_views.route('/removeDay/<dayId>', methods=['GET'])
@login_required
def removeDay(dayId):

    if delete_day(dayId):
        flash('Day Removed')
        return redirect('/myWorkouts')
    
    else:
        flash('Delete Unsuccessful')
        return redirect('/myWorkouts')



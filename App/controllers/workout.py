from App.models import *
from App.database import db
from sqlalchemy.exc import IntegrityError

#__init__(self, name, videoURL, category, primary_target, day_id):
       
def create_workout(name, videoURL, category, primary_target, day_id):
    newWorkout = Workout(name=name, videoURL= videoURL, category=category, primary_target=primary_target, day_id=day_id)
    return newWorkout

def add_workout(name, videoURL, category, primary_target, day_id):
    day = Day.query.get(day_id)
    newWorkout = create_workout(name, videoURL, category, primary_target, day_id)

    try: 
        db.session.add(newWorkout)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return None
    
    day.workouts.append(newWorkout)
    try:
        db.add(day)
        db.session.commit()
    except:
        db.session.rollback()
        return None
    
    return day 

def get_all_workouts(day_id):
    user = User.query.get(day_id)
    return Workout.query.filter_by(day_id = day_id).all()

def get_all_workouts_json(routineId):
    workouts = get_all_workouts(day_id)
    if not workouts:
        return None
    
    workouts = [ workout.toJSON() for workout in workouts]
    return workouts

def get_all_json():
    workouts = Workout.query.all()
    if not workouts:
        return None

    workouts = [workout.toJSON() for workout in workouts]
    return workouts

def delete_workout(workoutId):
    workout = Workout.query.get(workoutId)
    if workout:
        db.session.delete(workout)
        db.session.commit()
        return True
    return None

def rename_Day(dayId, title):
    day = Day.query.get(dayId)
    if day:
      day.title = title
      db.session.add(day)
      db.session.commit()
      return True
    return None

def alternativeRoutine(workoutId, name, videoURL, category, primary_target, day_id):
	workout = Workout.query.get(workoutId)
	if workout:
		workout.name = name
		workout.videoURL = videoURL
		workout.category = category
		workout.primary_target = primary_target
		workout.day_id = day_id
		db.session.add(workout)
		db.session.commit()
		return True
	return None






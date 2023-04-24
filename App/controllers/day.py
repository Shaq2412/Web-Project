from App.models import *
from App.database import db
from sqlalchemy.exc import IntegrityError

#__init__(self, name, videoURL, category, primary_target, day_id):
       
def create_day(title, routineId):
    newDay = Day(title=title, routineId=routineId)
    return newDay

def add_day(title, routineId):
    routine = Routine.query.get(routineId)
    newDay = create_day(title, routineId)
    try: 
        db.session.add(newDay)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return None
    
    routine.days.append(newDay)
    try:
        db.add(routine)
        db.session.commit()
    except:
        db.session.rollback()
        return None
    
    return routine

def get_all_days(routineId):
    user = User.query.get(routineId)
    return Day.query.filter_by(routineId = routineId).all()

def get_all_days_json(routineId):
    days = get_all_days(routineId)
    if not days:
        return None
    
    days = [ day.toJSON() for day in days]
    return days

def get_days_json():
    days = Day.query.all()
    
    if not days:
        return None
    
    days = [ day.toJSON() for day in days]
    return days

def delete_day(dayId):
    day = Day.query.get(dayId)

    workouts = Workout.query.filter_by(day_id = dayId).all()

    #delete all workouts that belong to that day
    for workout in workouts:
        delete_workout(workout.id)

    if day:
        db.session.delete(day)
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


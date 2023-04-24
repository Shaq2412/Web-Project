from App.models import *
from App.database import db
from sqlalchemy.exc import IntegrityError

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

def delete_workout(workoutId):
    workout = Workout.query.get(workoutId)
    if workout:
        db.session.delete(workout)
        db.session.commit()
        return True
    return None

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
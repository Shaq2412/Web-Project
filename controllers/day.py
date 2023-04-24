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

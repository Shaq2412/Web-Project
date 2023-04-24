from App.models import *
from App.database import db
from sqlalchemy.exc import IntegrityError

def create_routine(title, userId):
    newRoutine = Routine(userId = userId, title = title)
    return newRoutine

def add_routine(title, userId):
    user = User.query.get(userId)
    newRoutine = create_routine(title, userId)

    try:
        db.session.add(newRoutine)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return None
    user.routines.append(newRoutine)
    try:
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return None
    return newRoutine    

def get_all_routines(userId):
    user = User.query.get(userId)
    return Routine.query.filter_by(userId= userId).all()

def get_all_routines_json(userId):
    routs = get_all_routines(userId)
    if not routs:
        return None
    
    routs = [ rout.toJSON() for rout in routs]
    return routs

    #routines = Routine.query.filter_by(userId = userId).first()
    #if routines:
    #    return routines.toJSON()
    #return None
        
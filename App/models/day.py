from App.database import db

class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    #numWorkouts = db.Column(db.Integer, nullable=False)
    workout = db.relationship('Workout', backref = db.backref('workout', uselist = False, lazy='joined'))

    def __init__(self, title):
        self.title = title 
    
    def toJSON(self):
        return{
            'title' : self.title,
            'workout': self.workout.toJSON()
        }
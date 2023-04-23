from App.database import db

class Day(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    #numWorkouts = db.Column(db.Integer, nullable=False)
    workouts = db.relationship('Workout', backref='day')
    routineId = db.Column(db.Integer, db.ForeignKey('routine.id'))

    def __init__(self, title, routineId):
        self.title = title 
        self.routineId = routineId
    
    def toJSON(self):
        return{
            'id' : self.id,
            'title' : self.title,
            'routineId' : self.routineId
        }
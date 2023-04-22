from App.database import db

class Routine(db.Model):

    routineId = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer, nullable = False)
    day = db.relationship('Day', backref = db.backref('day', uselist = False, lazy='joined'))

    def __init__(self, title):
        self.title = title

    def toJSON(self):
        return{
            'title' : self.title,
            'day': self.day.toJSON(),
            
        }


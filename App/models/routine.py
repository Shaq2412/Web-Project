from App.database import db

class Routine(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Integer, nullable = False)
    days = db.relationship('Day', backref='workout')

    def __init__(self, title):
        self.title = title

    def toJSON(self):
        return{
            'title' : self.title,
        }


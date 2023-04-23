from App.database import db

class Routine(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    title = db.Column(db.Integer, nullable = False)
    days = db.relationship('Day', backref='routine')

    def __init__(self, userId, title):
        self.userId = userId
        self.title = title

    def toJSON(self):
        return{
            'id' : self.id,
            'title' : self.title,
            'userId ' : self.userId
        }


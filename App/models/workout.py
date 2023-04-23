from App.database import db

class Workout(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    videoURL = db.Column(db.String, nullable = False)
    category = db.Column(db.String, nullable = False)
    #force = db.Column(db.String, nullable = False)
    #grips = db.Column(db.String, nullable = False)
    primary_target = db.Column(db.String, nullable = False)
    day_id = db.Column(db.Integer, db.ForeignKey('day.id'))

    def __init__(self, name, videoURL, category, primary_target, day_id):
        self.name = name
        self.videoURL = videoURL
        self.category = category
        self.primary_target = primary_target
        self.id = day_id

    def toJSON(self):
        return{
            'id' : self.id,
            'name' : self.name,
            'videoURL' : self.videoURL,
            'category' : self.category,
            'primary_target' : self.primary_target,
            'dayId' : day_id
        }
from App.database import db

class Workout(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    videoURL = db.Column(db.String, nullable = False)
    category = db.Column(db.String, nullable = False)
    #force = db.Column(db.String, nullable = False)
    #grips = db.Column(db.String, nullable = False)
    primary_target = db.Column(db.String, nullable = False)

    def __init__(self, name, videoURL, category, primary_target):
        self.name = name
        self.videoURL = videoURL
        self.category = category
        self.primary_target = primary_target

    def toJSON(self):
        return{
            'id' : self.id,
            'name' : self.name,
            'videoURL' : self.videoURL,
            'category' : self.category,
            'primary_target' : self.primary_target
        }
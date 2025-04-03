from app.extensions import db

class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(10))
    age_group = db.Column(db.String(10))
    favorite_genres = db.Column(db.String(100))
    favorite_channels = db.Column(db.String(100))
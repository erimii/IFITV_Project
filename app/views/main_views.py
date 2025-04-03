from flask import Blueprint, render_template, request
from app.models import UserProfile
from app.extensions import db
from app.recommend import get_recommendations

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/recommend", methods=["POST"])
def recommend():
    gender = request.form.get("gender")
    age = request.form.get("age")
    genres = request.form.getlist("genres")
    channels = request.form.getlist("channels")

    user = UserProfile(
        gender=gender,
        age_group=age,
        favorite_genres=",".join(genres),
        favorite_channels=",".join(channels)
    )
    db.session.add(user)
    db.session.commit()

    results = get_recommendations(gender, age, genres, channels)
    return render_template("result.html", recommendations=results)

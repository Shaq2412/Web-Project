from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import LoginManager, login_required, login_user, current_user, logout_user

from.index import index_views


workouts_views = Blueprint('workouts_views', __name__, template_folder='../templates')
index_views = Blueprint('index_views', __name__, template_folder='../templates')

@workouts_views.route('/category/<category>', methods=['GET'])
@login_required
def getCategoryWorkouts(category):

    return render_template('workouts.html')
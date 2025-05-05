from flask import Blueprint, render_template, request ,redirect, current_app, url_for, flash
from flask_login import LoginManager, login_user
from flask.views import MethodView

home = Blueprint('home',__name__,template_folder='templates',
                static_folder='staticHome')


class homeView(MethodView):
    def get(self):
        return render_template('home.html')


home.add_url_rule('/home', view_func=homeView.as_view('home'), methods=['GET'])
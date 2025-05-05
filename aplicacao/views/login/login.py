from flask import Blueprint, render_template, request ,redirect, current_app, url_for, flash
from flask_login import LoginManager, login_user
from models.usuario.admLogin import Usuarios
from models.usuario.aluno import AlunoModel
from flask.views import MethodView

login = Blueprint('login',__name__,template_folder='templates',
                static_folder='staticLogin')

#login_manager = LoginManager()
#login_manager.login_view = 'login.loginUser'


def load_user(user_id):
    return Usuarios.query.get(int(user_id))

class Login(MethodView):
    
    def get(self):
        return render_template('login.html')


    def post(self):
        email = request.form.get('username')
        password = request.form.get('password')
        user = Usuarios.query.filter_by(username=email).first()
        if user and user.senha == password: 
            login_user(user)
            if user.is_admin:
                return redirect(url_for('home.home'))
            else:
                pass
        user = AlunoModel.query.filter_by(email=email).first()
        if user and user.senha == password:
            login_user(user)
            return redirect(url_for('home.home'))
        else:
            flash('Credenciais inválidas.')


login.add_url_rule('/', view_func=Login.as_view('login_index'),  methods=['GET', 'POST'])
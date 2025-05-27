from flask import Blueprint, render_template, request ,redirect, current_app, url_for, flash
from flask_login import LoginManager, login_user, current_user
from models.usuario.admLogin import Usuarios
from models.usuario.aluno import AlunoModel
#from aplicacao.form.login.formLogin import formLogin
from flask.views import MethodView
from functools import wraps


login = Blueprint('login',__name__,template_folder='templates',
                static_folder='staticLogin')


login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return Usuarios.query.get(int(user_id))


class Login(MethodView):
    
    def get(self):
        return render_template('login.html')


    def post(self):
        emailUser = request.form.get('email')
        password = request.form.get('password')
        print(emailUser)
        print(password)
        user = Usuarios.query.filter_by(email=emailUser).first()
        if user and user.senha == password:
            login_user(user)
            print("passou o log do usuarios")
            return redirect(url_for('home.home'))
    
        user = AlunoModel.query.filter_by(email=emailUser).first()
        if user and user.senha == password:
            login_user(user)
            return redirect(url_for('homeAluno.alunosHome'))
    
        flash('Credenciais inválidas.')
        return redirect(url_for('login.loginEntrar'))





login.add_url_rule('/', view_func=Login.as_view('loginEntrar'),  methods=['GET', 'POST'])
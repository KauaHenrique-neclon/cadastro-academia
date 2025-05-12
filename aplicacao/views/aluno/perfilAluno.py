from flask import Blueprint, render_template, request ,redirect, current_app, url_for, flash
from flask_login import LoginManager, login_user
from models.usuario.aluno import AlunoModel
from flask.views import MethodView





perfilAluno = Blueprint('perfilAluno',__name__,template_folder='templates',
                        static_folder='staticHomeAluno')



class AlunoPerfil(MethodView):
    def get(self):
        dadosAluno = AlunoModel.query.filter_by()
        return render_template('perfilAluno.html')
    

perfilAluno.add_url_rule('/alunoPerfil', view_func=AlunoPerfil.as_view('alunoPerfil'), methods=['GET'])
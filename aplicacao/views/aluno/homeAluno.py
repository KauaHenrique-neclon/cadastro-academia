from flask import Blueprint, render_template, request ,redirect, current_app, url_for, flash
from flask_login import LoginManager, login_user, current_user
from models.usuario.aluno import AlunoModel
from flask.views import MethodView

homeAluno = Blueprint('homeAluno',__name__, template_folder='templates',
                       static_folder='staticHomeAluno')

class AlunosHome(MethodView):
    def get(self):
        alunoId = current_user.id
        dadosAlunos = AlunoModel.query.filter_by(id=alunoId)
        contexto = {'dadosAlunos':dadosAlunos}
        return render_template('homeAlunos.html')
    

homeAluno.add_url_rule('/alunosHome', view_func=AlunosHome.as_view('alunosHome'), methods=['GET'])
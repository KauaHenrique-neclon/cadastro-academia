from flask import Blueprint, render_template, request ,redirect, current_app, url_for, flash
from flask_login import LoginManager, login_user
from models.usuario.aluno import AlunoModel
from flask.views import MethodView
from configuracao.banco import db


usuarioTabela = Blueprint('usuarioTabela',__name__,template_folder='templates',
                          static_folder='staticTabelas')


class TabelaUsuario(MethodView):


    def get(self):
        if id is None:
            dadosUsuario = AlunoModel.query.all()
            contexto = {'dadosUsuario': dadosUsuario}
            return render_template('tabelaUsuario.html', contexto=contexto)
        else:
            contexto = {'dadosUsuario': 'Erro'}
            return render_template('tabelaUsuario.html', contexto=contexto)
    


    def post(self):
        idUsuario = request.POST.get('user_id')
        if idUsuario:
            usuario = AlunoModel.query.filter_by(id=idUsuario).first()
            if usuario:
                usuario.is_active = not usuario.is_active
                db.session.commit()
                if usuario.is_active:
                    flash(f"Usuário {usuario.id} ativado com sucesso!")
                else:
                    flash(f"Usuário {usuario.id} desativado com sucesso!")
                return redirect(url_for('tabelaUsuario.tabelaUsuario'))
            else:
                flash("Usuário não encontrado!")
                return redirect(url_for('tabelaUsuario.tabelaUsuario'))
        else:
            flash("Usuário não encontrado!")
            return redirect(url_for('tabelaUsuario.tabelaUsuario'))

#usuarioTabela.add_url_rule('/tabelaUsuario/', view_func=TabelaUsuario.as_view('listaUsuarios'), methods=['GET'])
usuarioTabela.add_url_rule('/tabelaUsuario', view_func=TabelaUsuario.as_view('tabelaUsuario'), methods=['POST','GET'])
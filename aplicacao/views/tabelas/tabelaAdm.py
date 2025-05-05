from flask import Blueprint, render_template, request ,redirect, current_app, url_for, flash
from flask_login import LoginManager, login_user
from models.usuario.admLogin import Usuarios
from flask.views import MethodView
from configuracao.banco import db


admTabela = Blueprint('admTabela',__name__,template_folder='templates', 
                      static_folder='staticTabelas')


class TabelaAdm(MethodView):



    def get(self):
        dadosAdm = Usuarios.query.all()
        contexto = {'dados': dadosAdm}
        return render_template('tabelaAdm.html', contexto)
    


    def post(self):
        idAdm = request.POST.get('idAdm')
        admDados = Usuarios.query.filter_by(id=idAdm).first()
        if admDados:
            admDados.is_active = not admDados.is_active
            db.session.commit()
            if admDados.is_active:
                flash(f"Adm {admDados.id} ativado com sucesso!")
            else:
                flash(f"Adm {admDados.id} desativado com sucesso!")
            return redirect(url_for('tabelaAdm'))
        else:
            flash("Adm não encontrado!")
            return redirect(url_for('tabelaAdm'))




admTabela.add_url_rule('/tabelaAdm', view_func=TabelaAdm.as_view('tabelaAdm'), methods=['GET','POST'])
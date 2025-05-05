from flask import Blueprint, render_template, request ,redirect, current_app, url_for, flash
from flask_login import LoginManager, login_user
from models.financeiro.financeiro import pagamentos
from flask.views import MethodView
from configuracao.banco import db


pagamentoTabela = Blueprint('pagamentoTabela',__name__,template_folder='templates',
                            static_folder='staticTabelas')


class TabelaPagamentos(MethodView):
    def get(self):
        dadosPagamentos = pagamentos.query.all()
        contexto = {'dadosPagamentos': dadosPagamentos}
        return render_template('tabelaPagamentos.html', context=contexto)


pagamentoTabela.add_url_rule('/tabelaPagamentos', view_func=TabelaPagamentos.as_view('tabelaPagamentos'), methods=['GET'])
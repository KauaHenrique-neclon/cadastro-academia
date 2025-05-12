from models.financeiro.financeiro import pagamentos
from flask import render_template, redirect, Blueprint, request, flash
from models.financeiro.financeiro import pagamentos
from models.usuario.aluno import AlunoModel
from flask.views import MethodView
import datetime
from aplicacao.decorador.verificarAdm import verificarAdm
#from aplicacao.form.financeiro.formFinanceiro import formFinanceiro
from configuracao.banco import db


pagamento = Blueprint('pagamento',__name__,template_folder='templates',
                    static_folder='staticFinanceiro')




class pagamentoEfetado(MethodView):


    @verificarAdm
    def post(self):
        idPagamentoPegado = request.form.get('idPagamento')
        formaPagamento = request.form.get('formaDePagamento')
        if idPagamentoPegado and formaPagamento:
            pagamento = pagamentos.query.get(idPagamentoPegado)
            if pagamento:
                pagamento.datapagamento = datetime.date.today()
                pagamento.formadepagamento = formaPagamento
                pagamento.status = 'pago'
                db.session.commit()
            else:
                flash('Não foi encontrado pedencias')
        else:
            flash('Preencha todos os campos')


    @verificarAdm
    def get(self):
        #form = formFinanceiro()
        status = request.values.get('escolher')
        dadosStatus = []
        dadosUsuario = []
        contexto = {}
        if status:
            try:
                dadosStatus = pagamentos.query.filter_by(status=status).all()
                if dadosStatus:
                    idAluno = [pagamento.aluno_id for pagamento in dadosStatus]
                    dadosUsuario = AlunoModel.query.filter(AlunoModel.id.in_(idAluno)).all()
                    contexto = {'dadosStatus':dadosStatus,
                                'dadosAlunos':dadosUsuario
                                #'form':form
                                }
            except Exception as e:
                contexto = {'dadosStatus':[],
                        'dadosAlunos':[]}
        return render_template('efetuarPagamento.html', **contexto)


class dashboard(MethodView):

    @verificarAdm
    def post(self):
        pass


    @verificarAdm
    def get(self):
        alunos = AlunoModel.query.filter_by(is_active='True')
        return render_template('dashboardFina.html',aluno=alunos)


pagamento.add_url_rule('/efetuarPagamento',view_func=pagamentoEfetado.as_view('efetuarPagamento'), methods=['POST','GET'])
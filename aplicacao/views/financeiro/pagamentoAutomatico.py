from models.usuario.aluno import AlunoModel
from models.financeiro.financeiro import pagamentos
from datetime import date, timedelta, datetime
from configuracao.banco import db





def calculaVencimento():
    hoje = datetime.today()
    if hoje.day > 10:
        vencimento = hoje.replace(day=10) + timedelta(days=30)
        vencimento = vencimento.replace(day=10)
    else:
        vencimento = hoje.replace(day=10)
    return vencimento.date()




def criarPagamentoAutomatico():
    alunos = AlunoModel.query.all()
    for aluno in alunos:
        pagamentoExistente = pagamentos.query.filter(
        pagamentos.aluno_id == aluno.id,
        pagamentos.datapagamento.month == date.today().month,
        pagamentos.datapagamento.year == date.today().year,
        pagamentos.status == 'pendente'
        ).first()
        if pagamentoExistente is None:
            novoDebito = pagamentos(
                aluno_id = aluno.id,
                valor = 120.00,
                formadepagamento = 'Não Pago',
                status = 'pedende',
                vencimento = calculaVencimento()
            )
            db.session.add(novoDebito)
            db.session.commit()
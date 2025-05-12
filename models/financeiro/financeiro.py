from configuracao.banco import db
from models.usuario.aluno import AlunoModel
import datetime

class pagamentos(db.Model):
    __tablename__ = 'pagamentos'

    id = db.Column(db.Integer,primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('alunoModel.id'), nullable=False)
    aluno = db.relationship('AlunoModel', back_populates='pagamentos')
    datapagamento = db.Column(db.Date)
    vencimento = db.Column(db.Date)
    valor = db.Column(db.Float, nullable=False)
    formadepagamento = db.Column(db.String(30), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def __init__(self, aluno_id, datapagamento, vencimento, valor):
        self.aluno_id = aluno_id
        self.datapagamento = datapagamento
        self.vencimento = vencimento
        self.valor = valor

    def getIdPagamento(self):
        return self.id

    def __repr__(self):
        return f'<Pagamento {self.id} - {self.valor}>'
from configuracao.banco import db
from models.usuario.aluno import AlunoModel
import datetime

class pagamentos(db.Model):
    __tablename__ = 'pagamentos'

    id = db.Column(db.Integer,primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('Alunos.id'), nullable=False)
    aluno = db.relationship('Aluno', back_populates='pagamentos')
    datapagamento = db.Column(db.Date)
    vencimento = db.Column(db.Date)
    valor = db.Column(db.Float, nullable=False)
    formadepagamento = db.Column(db.String(30), nullable=False)
    status = db.Column(db.String(20), nullable=False)

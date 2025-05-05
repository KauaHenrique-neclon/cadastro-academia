from configuracao.banco import db
import datetime


class AlunoModel(db.Model):
    __tablename__ = 'alunoModel'

    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(240),nullable=False)
    datacriacao = db.Column(db.Date,default=datetime.date.today)
    bairro = db.Column(db.String(60), nullable=False)
    rua = db.Column(db.String(60),nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    #fotoUsuario

    # Relação com pagamentos
    pagamentos = db.relationship('Pagamento', back_populates='aluno')
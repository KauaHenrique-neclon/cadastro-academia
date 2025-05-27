from configuracao.banco import db
from datetime import date
from flask_bcrypt import bcrypt


class AlunoModel(db.Model):
    __tablename__ = 'alunomodel'

    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(240),nullable=False)
    datacriacao = db.Column(db.Date,default=date.today)
    bairro = db.Column(db.String(60), nullable=False)
    rua = db.Column(db.String(60),nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    role = db.Column(db.String(20), default='aluno')
    #fotoUsuario

    # Relação com pagamentos
    pagamentos = db.relationship('pagamentos', back_populates='aluno')

    def __init__(self, nome, senha, email, bairro, rua, numero, is_active=True, role='aluno'):
        self.nome = nome
        self.password = bcrypt.generate_password_hash(senha).decode('utf-8')
        self.email = email
        self.bairro = bairro
        self.rua = rua
        self.numero = numero
        self.is_active = is_active
        self.role = role

    
    def get_id(self):
        return self.id
    
    def __repr__(self):
        return f"Dados('{self.nome}')"
    
    def getPassword(self):
        return self.password
    
    def check_password(self, password):
        return self.senha == password
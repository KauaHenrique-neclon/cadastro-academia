from configuracao.banco import db
import datetime
from flask_login import UserMixin
from werkzeug.security import check_password_hash

class Usuarios(db.Model, UserMixin):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer,primary_key=True)
    nome = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(255),nullable=False, unique=True)
    senha = db.Column(db.String(30),nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    datacriacao = db.Column(db.Date,default=datetime.date.today)
    is_admin = db.Column(db.Boolean, default=True)
    admSuper = db.Column(db.Boolean, default=False)
    role = db.Column(db.String(20), default='admin')

    def __init__(self, nome, senha, email, is_active,admSuper, role='admin'):
        self.email = email
        self.senha = senha
        self.nome = nome
        self.is_active = is_active
        self.admSuper = admSuper
        self.role = role
    
    def get_id(self):
        return self.id
    
    def __repr__(self):
        return f"Dados('{self.nome}')"
    
    def check_password(self, password):
        return self.senha == password
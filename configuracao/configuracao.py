import secrets

class configura:
    # configuracao do banco de dsdos
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:5115@localhost/cadastro"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # chave secreta 
    SECRET_KEY = secrets.token_hex(16)
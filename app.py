from flask import Flask, send_from_directory
from apscheduler.schedulers.background import BackgroundScheduler
import os
from flask_migrate import Migrate
from flask_login import LoginManager
from configuracao.configuracao import configura
from configuracao.banco import db

from aplicacao.views.login.login import login, login_manager
from aplicacao.views.home.home import home
from aplicacao.views.cadastro.cadastroCliente import cadastro
from aplicacao.views.financeiro.pagamento import pagamento
from aplicacao.views.financeiro.pagamentoAutomatico import criarPagamentoAutomatico
from aplicacao.views.tabelas.tabelaUsuario import usuarioTabela
from aplicacao.views.tabelas.tabelaAdm import admTabela
from aplicacao.views.tabelas.tabelaPagamentos import pagamentoTabela
from aplicacao.views.aluno.homeAluno import homeAluno
from aplicacao.views.aluno.perfilAluno import perfilAluno



def AppFlask():

    app = Flask(__name__)
    app.config.from_object(configura)
    db.__init__(app)
    migrate = Migrate(app, db)
    app.jinja_loader.searchpath.append(os.path.join(app.root_path, 'aplicacao/include/templates'))



    login_manager.init_app(app) 
    login_manager.login_view = 'login.loginEntrar'

    routes = [
        (login, None),
        (home, None),
        (cadastro, '/cadastro'),
        (pagamento, '/pagamento'),
        (usuarioTabela, '/usuarioTabela'),
        (admTabela, '/tabelasAdm'),
        (pagamentoTabela,'/tabelaPagamentos'),
        (homeAluno,'/homeAluno'),
        (perfilAluno,'/perfilAluno'),
        ]

    for blueprint, prefix in routes:
        app.register_blueprint(blueprint, url_prefix=prefix)

    
    # configurando para novo static pq o flask é bucha
    @app.route('/include/static/<path:filename>')
    def serveStatic(filename):
        return send_from_directory('aplicacao/include/static/', filename)
    
    scheduler = BackgroundScheduler()
    scheduler.add_job(criarPagamentoAutomatico, 'cron', day=1, hour=0, minute=0)

    with app.app_context():
        try:
            db.create_all()
            print("Tabelas criadas com sucesso.")
        except Exception as e:
            print(f"Erro ao criar tabelas: {e}")

    return app 

"""


flask db init
flask db migrate -m "Mensagem da migração"
flask db upgrade


"""


app = AppFlask()
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, send_from_directory
from apscheduler.schedulers.background import BackgroundScheduler
import os
from flask_migrate import Migrate
from configuracao.configuracao import configura
from configuracao.banco import db

from aplicacao.views.login.login import login
from aplicacao.views.home.home import home
from aplicacao.views.cadastro.cadastroCliente import cadastro
from aplicacao.views.financeiro.pagamento import pagamento
from aplicacao.views.financeiro.pagamentoAutomatico import criarPagamentoAutomatico
from aplicacao.views.tabelas.tabelaUsuario import usuarioTabela
from aplicacao.views.tabelas.tabelaAdm import admTabela
from aplicacao.views.tabelas.tabelaPagamentos import pagamentoTabela

def AppFlask():

    app = Flask(__name__)
    app.config.from_object(configura)
    db.__init__(app)
    migrate = Migrate(app, db)
    app.jinja_loader.searchpath.append(os.path.join(app.root_path, 'aplicacao/include/templates'))

    """app.register_blueprint(login)
    app.register_blueprint(home)
    app.register_blueprint(cadastro,url_prefix='/cadastro')
    app.register_blueprint(pagamento,url_prefix='/pagamento')
    app.register_blueprint(usuarioTabela,prefix='/usuarioTabela')
    app.register_blueprint(admTabela ,prefix='/tabelas-adm')"""



    routes = [
        (login, None),
        (home, None),
        (cadastro, '/cadastro'),
        (pagamento, '/pagamento'),
        (usuarioTabela, '/usuarioTabela'),
        (admTabela, '/tabelas-adm'),
        (pagamentoTabela,'/pagamentotabela'),
        ]

    for blueprint, prefix in routes:
        app.register_blueprint(blueprint, url_prefix=prefix)

    #login_manager.init_app(app)

    
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
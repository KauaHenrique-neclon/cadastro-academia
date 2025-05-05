from flask import Blueprint, render_template, redirect, request, flash
from models.usuario.aluno import AlunoModel
from configuracao.banco import db
from flask.views import MethodView
from aplicacao.form.cadastro.formCadastro import cadastroForm


cadastro = Blueprint('cadastro',__name__, template_folder='templates',
                    static_folder='staticCadastro')


class cadastroAluno(MethodView):
    def get(self):
        form = cadastroForm()
        return render_template('cadastrarCliente.html',form=form)
    


    def post(self):
        form = cadastroForm()
        if form.validate_on_submit():
            novoAluno = AlunoModel(
                nome = form.nome.data,
                email = form.email.data,
                password = form.password.data,
                datacriacao = form.datacriacao.data,
                bairro = form.bairro.data,
                rua = form.rua.data,
                numero = form.numero.data
            )
            db.session.add(novoAluno)
            db.session.commit()
        flash('Cadastro concluido.')
    




cadastro.add_url_rule('/cadastroAluno',view_func=cadastroAluno.as_view('cadastroAluno'))
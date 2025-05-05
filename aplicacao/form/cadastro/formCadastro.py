from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, EmailField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Email


class cadastroForm(FlaskForm):
    nome = StringField('nome',validators=[DataRequired()],render_kw={"class": "input"}) #render_kw significa passar uma classe para o form
    email = EmailField('email',validators=[Email()], render_kw={"class":"input"})
    password = PasswordField('senha', validators=[DataRequired()],render_kw={"class":"input"})
    datacriacao = DateField('datacriacao', validators=[DataRequired()],render_kw={"class":"input"})
    bairro = StringField('bairro',validators=[DataRequired()],render_kw={"class":"input"})
    rua = StringField('rua',validators=[DataRequired()],render_kw={"class":"input"})
    numero = IntegerField('numero',validators=[DataRequired()],render_kw={"class":"input"})
    submit = SubmitField('Cadastrar', render_kw={"class": "btnSubmit"})
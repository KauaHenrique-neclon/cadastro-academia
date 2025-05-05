from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, EmailField, IntegerField, PasswordField, FloatField
from wtforms.validators import DataRequired, Email




class formFinanceiro(FlaskForm):
    aluno_id = IntegerField('aluno_id',validators=[DataRequired],render_kw={"class": "input"})
    datapagamento = DateField('datapagamento',validators=[DataRequired],render_kw={"class": "input"})
    vencimento = DateField('vencimento',validators=[DateField],render_kw={"class": "input"})
    valor = FloatField('valor',validators=[DataRequired],render_kw={"class": "input"})
    formadepagamento = StringField('formadepagamento',validators=[DataRequired],render_kw={"class": "input"})
    status = StringField('status',validators=[DataRequired],render_kw={"class": "input"})
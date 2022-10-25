from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class FormularioLogin(FlaskForm):
    usuario = StringField('Usuário', validators=[DataRequired(message="Usuário obrigatório!")])
    senha = PasswordField('Senha', validators=[DataRequired(message="Senha obrigatória!"),
                        Length(min=4, message='A senha deve ter no mínimo %(min)d dígitos.')])
    lembrar = BooleanField('Lembrar')
    enviar = SubmitField('Conectar')

class FormularioCurso(FlaskForm):
    nome = StringField('Curso', validators=[DataRequired(message="Curso obrigatório!")])
    enviar = SubmitField('Salvar')

class FormularioDisciplina(FlaskForm):
    nome = StringField('Disciplina',
                        validators=[DataRequired(message="Disciplina obrigatória!")])
    enviar = SubmitField('Salvar')                   



from app import login
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return Usuario.query.get(int(id))

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    senha_hash = db.Column(db.String(128))
    def __repr__(self):
        return '<Usuário {}>'.format(self.usuario)
    def set_senha(self, senha):

        self.senha_hash = generate_password_hash(senha)
    def check_senha(self, senha):

        return check_password_hash(self.senha_hash, senha)

class Curso(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     nome = db.Column(db.String(40))
     disciplinas = db.relationship('Disciplina', backref='curso')
     
     def __repr__(self):
        return f'<Curso "{self.nome}">'

class Disciplina(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      nome = db.Column(db.String(40))
      curso_id = db.Column(db.Integer, db.ForeignKey('curso.id'))

      def __repr__(self):
         return f'<Disciplina "{self.nome}">'       

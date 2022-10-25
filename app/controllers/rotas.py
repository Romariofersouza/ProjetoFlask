from flask import render_template, flash, redirect, url_for
from app import app,  db
from app.models.formularios import FormularioLogin, FormularioCurso, FormularioDisciplina
from flask_login import current_user, login_user
from app.models.modelos import Usuario, Curso, Disciplina
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse



@app.route('/')
@app.route('/index')
@login_required
def index():
    usuario = {'nome': 'Romário'}
    # return render_template('index.html', titulo='* Flask *', usuario=usuario)
    # return render_template('index.html', usuario=usuario)
    disciplinas = [
        {'nome': 'Introdução ao Python'},
        {'nome': 'Introdução ao Flask'}
    ]
    return render_template('index.html', titulo='* Flask *',
                        usuario=usuario, disciplinas=disciplinas)

@app.route('/login', methods=['GET', 'POST'] )
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    formulario = FormularioLogin()
    if formulario.validate_on_submit():
        usuario = Usuario.query.filter_by(usuario=formulario.usuario.data).first()
        if usuario is None or not usuario.check_senha(formulario.senha.data):
            flash('Nome de usuário ou senha inválidos')
            return redirect(url_for('login'))
        login_user(usuario, remember=formulario.lembrar.data)
        proxima_pagina = request.args.get('next')
        if not proxima_pagina or url_parse(proxima_pagina).netloc != '':
            proxima_pagina = url_for('index')
        return redirect(proxima_pagina)
    return render_template('login.html', titulo='Conexão', formulario=formulario)  

@app.route('/logout')
def logout():
 logout_user()
 return redirect(url_for('index')) 

@app.route('/cursos')
@login_required
def cursos():
 cursos = Curso.query.all()
 return render_template('cursos.html', cursos=cursos)     


@app.route('/incluir_curso', methods = ['GET', 'POST'])
@login_required
def incluir_curso():
    formulario = FormularioCurso()
    if formulario.validate_on_submit():
        curso = Curso(nome = formulario.nome.data)
        db.session.add(curso)
        db.session.commit()
        flash('O novo curso foi adicionado com sucesso!')
        return redirect(url_for('cursos'))
    return render_template('manutencaoCurso.html', titulo='Curso',
                            operacao='Inclusão de curso', formulario=formulario)

@app.route('/<int:id>/editar_curso', methods = ['GET', 'POST'])
@login_required
def editar_curso(id):
    formulario = FormularioCurso()
    if request.method == 'GET':
        curso = Curso.query.filter_by(id=id).first()
        formulario.nome.data = curso.nome
        return render_template('manutencaoCurso.html', titulo='Curso',
                                operacao='Edição de curso', formulario=formulario)

    if request.method == 'POST':
        nome = formulario.nome.data
        Curso.query.filter_by(id=id).update({"nome": nome})
        db.session.commit()
        flash('Curso editado com sucesso!')
        return redirect(url_for('cursos'))



@app.route('/<int:id>/excluir_curso')
@login_required
def excluir_curso(id):
    curso = Curso.query.filter_by(id=id).first()
    if curso.disciplinas:
        flash('É necessário primeiro realizar a exclusão das disciplinas!')
    else:
        db.session.delete(curso)
        db.session.commit()
        flash('O curso foi excluído com sucesso!')
    return redirect(url_for('cursos'))

            

@app.route('/<int:idCurso>/cadastrar_disciplinas')
@login_required
def cadastrar_disciplinas(idCurso):
    curso = Curso.query.filter_by(id=idCurso).first()
    return render_template('disciplinas.html', cursoNome=curso.nome,
                            disciplinas=curso.disciplinas)

@app.route('/<int:idCurso>/incluir_disciplina', methods = ['GET', 'POST'])
@login_required
def incluir_disciplina(idCurso):
    formulario = FormularioDisciplina()
    if formulario.validate_on_submit():
        disciplina = Disciplina(nome = formulario.nome.data, curso_id = idCurso)
        db.session.add(disciplina)
        db.session.commit()
        flash('A nova disciplina foi adicionado com sucesso!')
        return redirect('/' + str(idCurso) + '/cadastrar_disciplinas')
    return render_template('manutencaoDisciplina.html', titulo='Disciplina',
                            operacao='Inclusão de disciplina', formulario=formulario)

@app.route('/<int:idCurso>/<int:idDisciplina>/editar_disciplina', methods = ['GET', 'POST'])
@login_required
def editar_disciplina(idCurso, idDisciplina):
    formulario = FormularioDisciplina()
    if request.method == 'GET':
        disciplina = Disciplina.query.filter_by(curso_id = idCurso, id = idDisciplina).first()
        formulario.nome.data = disciplina.nome
        return render_template('manutencaoDisciplina.html', titulo='Disciplina',
                                operacao='Edição de disciplina', formulario=formulario)
    if request.method == 'POST':
        nome = formulario.nome.data
        Disciplina.query.filter_by(curso_id = idCurso,
                                    id = idDisciplina).update({"nome": nome})
        db.session.commit()
        flash('Disciplina editado com sucesso!')
        return redirect('/' + str(idCurso) + '/cadastrar_disciplinas')

@app.route('/<int:idCurso>/<int:idDisciplina>/excluir_disciplina', methods = ['GET', 'POST'])
@login_required
def excluir_disciplina(idCurso, idDisciplina):
    disciplina = Disciplina.query.filter_by(curso_id = idCurso, id = idDisciplina).first()
    db.session.delete(disciplina)
    db.session.commit()
    flash('A disciplina foi excluída com sucesso!')
    return redirect('/' + str(idCurso) + '/cadastrar_disciplinas')



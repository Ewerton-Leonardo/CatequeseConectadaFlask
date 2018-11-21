from app import app, db
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user

from app.models.forms import LoginForm, CadastroCatequistaForm, CadastroComunidadeForm, RoteiroForm, TesteForm
from app.models.tables import Catequista, Comunidade, Roteiro


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['get', 'post'])
def login():
    form_login = LoginForm(request.form)
    flash(form_login.errors, 'invalido')
    if form_login.validate_on_submit():
        cqt = Catequista.query.filter_by(username=form_login.username.data).first()
        if cqt and cqt.senha == form_login.senha.data:
            login_user(cqt)
            flash("Logado", 'sucesso')
            return redirect(url_for('pagina-inicial'))
        else:
            flash("Usuário não cadastrado ou senha inválida", 'erro')
    else:
        flash(form_login.errors, 'invalido')
    return render_template('login.html', form_login=form_login)


@app.route('/cadastro-catequista', methods=['get', 'post'])
def cadastro_catequista():
    form_catequista = CadastroCatequistaForm(request.form)
    form_catequista.comunidade.choices = [(row.id, row.nome)
                                          for row in Comunidade.query.order_by(Comunidade.nome).all()]
    if form_catequista.validate_on_submit():
        existe_cqt = Catequista.query.filter_by(username=form_catequista.username.data).first()
        if not existe_cqt:
            cqt = Catequista(form_catequista.username.data, form_catequista.senha.data, form_catequista.nome.data,
                             form_catequista.comunidade.data, form_catequista.tipo1.data,
                             form_catequista.tipo2.data, form_catequista.coordenacao.data)
            db.session.add(cqt)
            db.session.commit()
            flash('Cadastrado', 'sucesso')
        else:
            flash('Nome de usuário já cadastrado', 'erro')
    else:
        flash(form_catequista.errors, 'invalido')

    return render_template('cadastro-catequista.html', form_catequista=form_catequista)


@app.route('/cadastro-comunidade', methods=['get', 'post'])
def cadastro_comunidade():
    form = CadastroComunidadeForm(request.form)
    existe_com = Comunidade.query.filter_by(nome=form.nome.data, paroquia=form.paroquia.data, diocese=form.diocese.data)
    if not existe_com:
        comunidade = Comunidade(form.diocese.data, form.paroquia.data, form.nome.data, form.logradouro.data, form.bairro.data, form.cidade.data, form.estado.data, form.numero)
        db.session.add(comunidade)
        db.session.commit()
        flash('Comunidade cadastrada', 'sucesso')
    else:
        flash('Comunidade já cadastrada', 'erro')
    return render_template('cadastro-comunidade.html', form=form)


@app.route('/pagina-inicial')
@login_required
def pagina_inicial():
    return render_template('pagina-inicial.html', user=current_user)


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)

@app.route('/add-roteiro', methods=['get', 'post'])
@login_required
def add_roteiro():
    form = RoteiroForm(request.form)
    if form.validate_on_submit() and request.method == 'POST':
        # roteiro = Roteiro()
        pass


@app.route('/teste', methods=['get', 'post'])
def teste():
    form = TesteForm()
    form.comunidade.choices = [(row.id, 'Comunidade ' + row.nome + ', ' + row.paroquia + ', ' + row.diocese)
                                          for row in Comunidade.query.all()]
    flash(str(form.errors) + str(form.validate()), 'invalido')
    if form.validate_on_submit():
        flash('Deu certo', 'sucesso')
    return render_template('teste.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi deslogado')
    return redirect(url_for('index'))

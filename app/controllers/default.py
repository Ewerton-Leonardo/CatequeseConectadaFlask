from app import app, db
from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_user, logout_user, login_required, current_user

from app.models.forms import LoginForm, CatequistaForm, ComunidadeForm, TipoCatequeseForm, CodigoTurmaForm, \
    CatequizandoForm, DioceseForm, TesteForm
from app.models.tables import Catequista, Catequizando, Comunidade, TipoCatequese, FichaCatequista, User, Turma

from app.services.user_services import UserDAO
from app.services.catequista_services import CatequistaDAO
from app.services.catequizando_services import CatequizandoDAO
from app.services.comunidade_services import ComunidadeDAO
from app.services.encontro_services import EncontroDAO
from app.services.roteiro_services import RoteiroDAO
from app.services.turma_services import TurmaDAO
from app.services.tipo_catequese_services import TipoCatequeseDAO

from datetime import date

app.jinja_env.globals['date_today'] = date.today()


@app.route('/index')
@app.route('/')
def index():
    if current_user.is_active:
        user = UserDAO.query_user_id(current_user.id_user)
        if user.tipo == 'Catequista':
            ficha = CatequistaDAO.query_ficha_catequista(user.id)
            return render_template('templates_catequista/pagina_inicial.html', ficha=ficha, user=user)
        elif user.tipo == 'Catequizando':
            return render_template('templates_catequizando/pagina_inicial.html', user=user)

    else:
        return render_template('index.html')


@app.route('/login', methods=['get', 'post'])
def login():
    if current_user.is_active:
        return redirect(url_for('index'))

    form_login = LoginForm(request.form)

    if form_login.validate_on_submit() and request.method == 'POST':
        user = UserDAO.query_username(form_login.username.data)

        if user and user.senha == form_login.senha.data:
            login_user(user)
            flash("Logado", 'sucesso')
            return redirect(url_for('index'))

        else:
            flash("Usuário não cadastrado ou senha inválida", 'erro')

    elif form_login.errors != {} and form_login.is_submitted():
        for erro in form_login.errors:
            flash(form_login.errors[erro][0], 'erro')

    return render_template('login.html', form_login=form_login)


@app.route('/cadastro/catequista', methods=['get', 'post'])
def cadastro_catequista():
    if current_user.is_active:
        return redirect(url_for('index'))
    form_catequista = CatequistaForm(request.form)
    comunidades_query = ComunidadeDAO.query_order_comunidades()
    if not comunidades_query:
        flash('Antes de cadastrar-se adicione sua comunidade', 'info')
        return redirect(url_for('cadastro_comunidade'))
    form_catequista.comunidade.choices = [('', '')]
    comunidade_form = DioceseForm()
    comunidade_form.diocese_select.choices = [('', 'Selecione a diocese')]
    for row in ComunidadeDAO.query_dioceses():
        comunidade_form.diocese_select.choices.append((row.diocese, row.diocese))
    comunidade_form.paroquia_select.choices = []
    if form_catequista.validate_on_submit() and request.method == 'POST':
        existe_user = UserDAO.query_username(form_catequista.username.data)
        if not existe_user:
            user = User(username=form_catequista.username.data,
                        senha=form_catequista.senha.data,
                        tipo='Catequista')
            db.session.add(user)
            db.session.commit()
            if form_catequista.coordenacao.data == 'True':
                form_catequista.coordenacao.data = True
            else:
                form_catequista.coordenacao.data = False
            user = UserDAO.query_username(user.username)
            cqt = Catequista(
                id_user=user.id,
                nome=form_catequista.nome.data,
                id_comunidade=form_catequista.comunidade.data,
                data_nasc=form_catequista.data_nasc.data,
                coordernacao=form_catequista.coordenacao.data
            )
            db.session.add(cqt)
            db.session.commit()
            flash('Cadastrado', 'sucesso')
            return redirect(url_for('login'))

        else:
            flash('Nome de usuário já cadastrado', 'erro')

    elif form_catequista.errors != {} and form_catequista.is_submitted():
        for erro in form_catequista.errors:
            flash(form_catequista.errors[erro][0], 'erro')
            flash(type(form_catequista.comunidade.data), 'erro')

    return render_template('cadastro_catequista.html', form_catequista=form_catequista, comunidade_form=comunidade_form)


@app.route('/cadastro/catequizando', defaults={'codigo': None}, methods=['get', 'post'])
@app.route('/cadastro/catequizando/<codigo>', methods=['get', 'post'])
def cadastro_catequizando(codigo):
    if TurmaDAO.query_codigo_turma(codigo):
        turma = TurmaDAO.query_codigo_turma(codigo)
        if turma:
            form_catequizando = CatequizandoForm(request.form)
            if form_catequizando.validate_on_submit() and request.method == 'POST':
                existe_user = UserDAO.query_username(form_catequizando.username.data)
                if not existe_user:
                    user = User(username=form_catequizando.username.data,
                                senha=form_catequizando.senha.data,
                                tipo='Catequizando')
                    db.session.add(user)
                    db.session.commit()
                    user = UserDAO.query_username(user.username)
                    cqz = Catequizando(id_user=user.id,
                                       id_comunidade=turma.id_comunidade,
                                       id_turma=turma.id,
                                       nome=form_catequizando.nome.data)
                    db.session.add(cqz)
                    db.session.commit()
            return render_template('cadastro_catequizando.html', form_catequizando=form_catequizando, codigo=codigo)
        else:
            flash('Código inválido, tente novamente', 'erro')
            return redirect(url_for('cadastro_catequizando'))
    else:
        form_codigo = CodigoTurmaForm(request.form)
        if form_codigo.validate_on_submit() and request.method == 'POST':
            if TurmaDAO.query_codigo_turma(form_codigo.codigo.data):
                return redirect(url_for('cadastro_catequizando', codigo=form_codigo.codigo.data))
            else:
                flash('Código inválido, tente novamente', 'erro')
                form_codigo.codigo.data = ''
        elif form_codigo.errors != {} and form_codigo.is_submitted():
            flash(form_codigo.errors, 'erro')
        return render_template('cadastro_catequizando.html', form_codigo=form_codigo)


@app.route('/cadastro/comunidade', methods=['get', 'post'])
def cadastro_comunidade():
    form = ComunidadeForm(request.form)
    form_select = DioceseForm()
    form_select.diocese_select.choices = [('', 'Selecione a diocese')]
    for row in ComunidadeDAO.query_dioceses():
        form_select.diocese_select.choices.append((row.diocese, row.diocese))
    form_select.paroquia_select.choices = []
    if form.validate_on_submit() and request.method == 'POST':
        existe_com = ComunidadeDAO.query_comunidade(form.nome.data, form.paroquia.data, form.diocese.data)

        if not existe_com:
            comunidade = Comunidade(diocese=form.diocese.data, paroquia=form.paroquia.data, nome=form.nome.data)
            db.session.add(comunidade)
            db.session.commit()
            flash('Comunidade cadastrada', 'sucesso')
            return redirect(url_for('index'))

        else:
            flash('Comunidade já cadastrada', 'erro')

    elif form.errors != {} and form.is_submitted():
        for erro in form.errors:
            flash(form.errors[erro], 'erro')

    return render_template('cadastro_comunidade.html', form=form, form_select=form_select)


@app.route('/comunidades/<paroquia>/<diocese>')
def comunidades(paroquia, diocese):
    comunidades = ComunidadeDAO.query_comunidades_diocese_paroquia(diocese, paroquia)

    comunidadesArray = []
    for comunidade in comunidades:
        comObt = {}
        comObt['id_com'] = comunidade.id
        comObt['nome'] = comunidade.nome
        comObt['paroquia'] = comunidade.paroquia
        comObt['diocese'] = comunidade.diocese
        comunidadesArray.append(comObt)

    return jsonify({'comunidades': comunidadesArray})


@app.route('/paroquias/<diocese>')
def paroquias(diocese):
    paroquias = ComunidadeDAO.query_paroquias_diocese(diocese)
    paroquiasArray = []
    for paroquia in paroquias:
        paroquiasArray.append(paroquia.paroquia)

    return jsonify({'paroquias': paroquiasArray})


@app.route('/tipos_de_catequese', methods=['get', 'post'])
def tipos_de_catequese():
    tipos_de_catequese_dict = TipoCatequeseDAO.query_tipos_catequeses_all()
    form = TipoCatequeseForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        existe_tipo_catequese = TipoCatequeseDAO.query_tipo_catequese_nome(form.nome.data)
        if existe_tipo_catequese:
            flash("Tipo de catequese já existe", 'erro')
        else:
            tipo_de_catequese = TipoCatequese(nome=form.nome.data)
            db.session.add(tipo_de_catequese)
            db.session.commit()
            flash('Tipo de catequese adicionado', 'sucesso')
        return redirect(url_for('tipos_de_catequese'))

    elif form.errors != {} and form.is_submitted():
        for erro in form.errors:
            flash(form.errors[erro][0], 'erro')

    return render_template('tipos_de_catequese.html',
                           form=form, tipos_de_catequese_dict=tipos_de_catequese_dict)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você foi deslogado')
    return redirect(url_for('index'))


@app.route('/teste', methods=['get', 'post'])
def teste():
    dioceses = ComunidadeDAO.query_dioceses()
    dict = {}
    for diocese in dioceses:
        cont_paroquias = 0
        paroquias = ComunidadeDAO.query_paroquias_diocese(diocese.diocese)
        for paroquia in paroquias:
            if cont_paroquias > 0:
                dict[diocese.diocese].update({paroquia.paroquia: []})
            else:
                cont_paroquias += 1
                dict[diocese.diocese] = {paroquia.paroquia: []}
            comunidades_all = ComunidadeDAO.query_comunidades_diocese_paroquia(diocese.diocese, paroquia.paroquia)
            for comunidade in comunidades_all:
                dict[diocese.diocese][paroquia.paroquia].append(comunidade.nome)

    return jsonify(dict)

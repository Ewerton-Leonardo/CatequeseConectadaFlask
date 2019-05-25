from app import app, db
from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import logout_user, login_required, current_user
import functools

from app.models.forms import FichaCatequistaForm, RoteiroForm, TurmaForm, FichaCatequizandoForm, EncontroForm, \
    EditarRoteiroForm, EditarFichaCatequistaForm, EditarFichaCatequizandoForm, EditarTurmaForm, EditarEncontroForm, CatequistaTipoCatequeseForm
from app.models.tables import Catequista, Roteiro, FichaCatequista, Turma, FichaCatequizando, Encontro, CatequistaTipoCatequese

from app.services.roteiro_services import RoteiroDAO
from app.services.user_services import UserDAO
from app.services.tipo_catequese_services import TipoCatequeseDAO
from app.services.catequista_services import CatequistaDAO
from app.services.turma_services import TurmaDAO
from app.services.catequizando_services import CatequizandoDAO
from app.services.encontro_services import EncontroDAO


def autenticacao_catequista(f):
    @functools.wraps(f)
    def funcao_decorada(*args, **kwargs):
        user = UserDAO.query_user_id(current_user.id_user)
        if user.tipo != 'Catequista':
            abort(401)
        return f(*args, **kwargs)
    return funcao_decorada


@app.route('/adicionar_ficha_catequista/add', methods=['get', 'post'])
@login_required
@autenticacao_catequista
def adicionar_ficha_catequista():
    form_ficha = FichaCatequistaForm(request.form)
    tem_ficha = False
    query_ficha = CatequistaDAO.query_ficha_catequista(current_user.id)

    if query_ficha:
        tem_ficha = True

    if request.method == 'POST' and form_ficha.validate_on_submit():
        ficha = FichaCatequista(
            id_catequista=current_user.id,
            id_comunidade=current_user.id_comunidade,
            nome_completo=form_ficha.nome_completo.data,
            data_nasc=form_ficha.data_nasc.data,
            ano_entrada=form_ficha.ano_entrada.data,
            escolaridade=form_ficha.escolaridade.data,
            telefone=form_ficha.telefone.data,
            whatsapp=form_ficha.whatsapp.data,
            logradouro=form_ficha.logradouro.data,
            bairro=form_ficha.bairro.data,
            cidade=form_ficha.cidade.data,
            estado=form_ficha.estado.data,
            numero_casa=form_ficha.numero_casa.data,
            ponto_referencia=form_ficha.ponto_referencia.data,
            crismado=form_ficha.crismado.data
        )
        db.session.add(ficha)
        db.session.commit()

        flash('Ficha adicionada', 'sucesso')
        return redirect(url_for('index'))

    if form_ficha.errors != {} and form_ficha.is_submitted():
        for erro in form_ficha.errors:
            flash(form_ficha.errors[erro][0], 'erro')

    return render_template('templates_catequista/cadastro_ficha_catequista.html',
                           user=current_user,
                           form_ficha=form_ficha,
                           tem_ficha=tem_ficha)


@app.route('/perfil')
@login_required
@autenticacao_catequista
def perfil():
    return render_template('templates_catequista/perfil.html', user=current_user)


@app.route('/tipo_de_catequese/catequista', methods=['get', 'post'])
@login_required
@autenticacao_catequista
def catequista_tipo_catequese():
    form = CatequistaTipoCatequeseForm(request.form)
    tipos_catequeses = TipoCatequeseDAO.query_order_tipo_catequese()
    catequista_tipos_catequeses = TipoCatequeseDAO.query_tipos_catequeses_catequista(current_user.id)
    if catequista_tipos_catequeses:
        for tipo_catequese in catequista_tipos_catequeses:
            for tipo in tipos_catequeses:
                if tipo_catequese.id_tipo_catequese == tipo.id:
                    tipos_catequeses.remove(tipo)
    form.tipo_catequese.choices = [(row.id, row.nome) for row in tipos_catequeses]

    if form.validate_on_submit() and request.method == 'POST':
        var_catequista_tipo_catequese = CatequistaTipoCatequese(id_catequista=current_user.id,
                                                                id_tipo_catequese=form.tipo_catequese.data)
        db.session.add(var_catequista_tipo_catequese)
        db.session.commit()
        return redirect(url_for('catequista_tipo_catequese'))
    elif form.errors != {} and form.is_submitted():
        for erro in form.errors:
            flash(form.errors[erro][0], 'erro')
    return render_template('templates_catequista/relacionar_tipo_catequese.html', form=form)


'''
####################################################################
                          ROTAS DE ROTEIRO
####################################################################
'''


@app.route('/roteiro/')
@app.route('/roteiro/all')
@login_required
@autenticacao_catequista
def roteiros():
    dict_roteiros = RoteiroDAO.query_roteiros_comunidade(current_user.id_comunidade, ).order_by('tema').all()
    return render_template('templates_catequista/list_roteiros.html',
                           dict_roteiros=dict_roteiros)


@app.route('/roteiro/publico')
def roteiros_publicos():
    dict_roteiros = RoteiroDAO.query_roteiros_publicos()
    return render_template('templates_catequista/list_roteiros_publicos.html',
                           dict_roteiros=dict_roteiros)


@app.route('/roteiro/add', methods=['get', 'post'])
@login_required
@autenticacao_catequista
def adicionar_roteiro():
    form = RoteiroForm(request.form)
    form.tipo.choices = [(row.id, row.nome) for row in TipoCatequeseDAO.query_tipos_catequeses_catequista(current_user.id)]

    if form.validate_on_submit() and request.method == 'POST':
        roteiro = Roteiro(
            id_catequista=current_user.id,
            id_comunidade=current_user.id_comunidade,
            tipo=form.tipo.data,
            tema=form.tema.data,
            ambiente=form.ambiente.data,
            acolhida=form.acolhida.data,
            oracao_inicial=form.oracao_inicial.data,
            dinamica=form.dinamica.data,
            motivacao=form.motivacao.data,
            leituras=form.leituras.data,
            desenvolvimento=form.desenvolvimento.data,
            atividade=form.atividade.data,
            compromisso=form.compromisso.data,
            avisos=form.avisos.data,
            oracao_final=form.oracao_final.data,
            observacoes=form.observacoes.data,
            publico=form.publico.data
        )
        RoteiroDAO.add_roteiro(roteiro)
        return redirect(url_for('roteiros'))

    elif form.errors != {} and form.is_submitted():
        for erro in form.errors:
            flash(form.errors[erro][0], 'erro')

    return render_template('templates_catequista/adicionar_roteiro.html', form=form)


@app.route('/roteiro/<int:id_roteiro>/view')
@app.route('/roteiro/<int:id_roteiro>/')
@login_required
@autenticacao_catequista
def visualizar_roteiro(id_roteiro):
    roteiro = RoteiroDAO.query_roteiro(id_roteiro)
    autor = CatequistaDAO.query_catequista_id(roteiro.id_catequista)

    return render_template('templates_catequista/view_roteiro.html',
                           roteiro=roteiro,
                           autor=autor)


@app.route('/roteiro/<int:id_roteiro>/edit', methods=['get', 'post'])
@login_required
@autenticacao_catequista
def editar_roteiro(id_roteiro):
    roteiro = RoteiroDAO.query_roteiro_catequista(id_roteiro, current_user.id, True)
    form_roteiro = EditarRoteiroForm(formdata=request.form, obj=roteiro)
    form_roteiro.tipo.choices = [(current_user.tipo_catequese_1, current_user.tipo_catequese_1), (current_user.tipo_catequese_2, current_user.tipo_catequese_2)]

    if form_roteiro.validate_on_submit() and request.method == 'POST':
        flash(form_roteiro.tema.data, 'erro')
        RoteiroDAO.update(roteiro, form_roteiro)
        return redirect(url_for('visualizar_roteiro', id_roteiro=id_roteiro))

    elif form_roteiro.errors != {} and form_roteiro.is_submitted():
        for erro in form_roteiro.errors:
            flash(form_roteiro.errors[erro][0], 'erro')

    elif roteiro is None:
        flash('Roteiro não encontrado', 'erro')
        abort(404)

    return render_template('templates_catequista/editar_roteiro.html',
                           roteiro=roteiro,
                           form_roteiro=form_roteiro)


@app.route('/roteiro/<int:id_roteiro>/delete')
@login_required
@autenticacao_catequista
def apagar_roteiro(id_roteiro):
    roteiro = RoteiroDAO.query_roteiro_catequista(id_roteiro, current_user.id, True)
    RoteiroDAO.delete(roteiro)

    if not RoteiroDAO.query_roteiro_catequista(id_roteiro, current_user.id):
        flash('Roteiro apagado', 'sucesso')
        return redirect(url_for('roteiros'))


'''
########################################################################
                            ROTAS DE TURMA
########################################################################
'''


@app.route('/turma/all')
@app.route('/turma/')
@login_required
@autenticacao_catequista
def turmas():
    dict_turmas = TurmaDAO.query_turmas(current_user.id_comunidade)
    return render_template('templates_catequista/list_turmas.html', dict_turmas=dict_turmas)


@app.route('/turma/add', methods=['get', 'post'])
@login_required
@autenticacao_catequista
def adicionar_turma():
    form = TurmaForm(request.form)
    tipos_catequeses = TipoCatequeseDAO.query_tipos_catequeses_catequista(current_user.id)
    form.tipo.choices = [(row.id_tipo_catequese, TipoCatequeseDAO.query_tipo_catequese_id(row.id_tipo_catequese).nome) for row in tipos_catequeses]

    if request.method == 'POST' and form.validate_on_submit():
        turma = Turma(id_comunidade=current_user.id_comunidade,
                      nome=form.nome.data,
                      ano=form.ano.data,
                      id_tipo_catequese=form.tipo.data)
        db.session.add(turma)
        db.session.commit()
        return redirect(url_for('turmas'))

    elif form.errors != {} and form.is_submitted():
        for erro in form.errors:
            flash(form.errors[erro][0], 'erro')

    return render_template('templates_catequista/adicionar_turma.html', form=form)


@app.route('/turma/<int:id_turma>/edit', methods=['get', 'post'])
@login_required
@autenticacao_catequista
def editar_turma(id_turma):
    turma = TurmaDAO.query_turma(id_turma, current_user.id_comunidade, True)
    form = EditarTurmaForm(formdata=request.form, obj=turma)
    form.tipo.choices = [(current_user.tipo_catequese_1, current_user.tipo_catequese_1), (current_user.tipo_catequese_2, current_user.tipo_catequese_2)]

    if form.validate_on_submit() and request.method == 'POST':
        turma.nome = form.nome.data
        turma.ano = form.ano.data
        db.session.commit()
        return redirect(url_for('visualizar_turma', id_turma=id_turma))

    elif form.errors != {} and form.is_submitted():
        for erro in form.errors:
            flash(form.errors[erro][0], 'erro')

    elif turma is None:
        flash('Roteiro não encontrado', 'erro')
        abort(404)

    return render_template('templates_catequista/editar_turma.html', turm=turma, form=form)


@app.route('/turma/<int:id_turma>/view')
@app.route('/turma/<int:id_turma>/')
@login_required
@autenticacao_catequista
def visualizar_turma(id_turma):
    turma = TurmaDAO.query_turma(id_turma, current_user.id_comunidade, True)
    catequizandos = CatequizandoDAO.query_order_fichas_catequizandos(id_turma)
    return render_template('templates_catequista/view_turma.html', turma=turma, catequizandos=catequizandos)


'''
########################################################################
                    ROTAS DE FICHA CATEQUIZANDO
########################################################################
'''


@app.route('/turma/<int:id_turma>/ficha_catequizando/add', methods=['get', 'post'])
@login_required
@autenticacao_catequista
def adicionar_ficha_catequizando(id_turma):
    turma = TurmaDAO.query_turma(id_turma, current_user.id_comunidade, True)
    form = FichaCatequizandoForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        ficha_catequizando = FichaCatequizando(
            id_comunidade=current_user.id_comunidade,
            nome=form.nome_completo.data,
            data_nasc=form.data_nasc.data,
            nome_mae=form.nome_mae.data,
            nome_pai=form.nome_pai.data,
            batizado=form.batizado.data,
            eucaristia=form.eucaristia.data,
            escolaridade=form.escolaridade.data,
            logradouro=form.logradouro.data,
            bairro=form.bairro.data,
            cidade=form.cidade.data,
            estado=form.estado.data,
            numero_casa=form.numero_casa.data,
            ponto_referencia=form.ponto_referencia.data,
            telefone=form.telefone.data,
            whatsapp=form.whatsapp.data,
            data_inscricao=form.data_inscricao.data,
            id_turma=id_turma
        )
        db.session.add(ficha_catequizando)
        turma.atualizar_qt_catequizandos()
        db.session.commit()
        return redirect(url_for('visualizar_turma', id_turma=id_turma))

    elif form.errors != {} and form.is_submitted():
        for erro in form.errors:
            flash(form.errors[erro][0], 'erro')

    return render_template('templates_catequista/adicionar_ficha_catequizando.html', form=form)


@app.route('/turma/<int:id_turma>/ficha_catequizando/<int:id_ficha_catequizando>/edit', methods=['get', 'post'])
@login_required
@autenticacao_catequista
def editar_ficha_catequizando(id_turma, id_ficha_catequizando):
    ficha_catequizando = CatequizandoDAO.query_ficha_catequizando_comunidade(id_ficha_catequizando, current_user.id_comunidade, id_turma, True)
    form = EditarFichaCatequizandoForm(formdata=request.form, obj=ficha_catequizando)

    if form.validate_on_submit() and request.method == 'POST':
        ficha_catequizando.nome = form.nome.data
        ficha_catequizando.data_nasc = form.data_nasc.data
        ficha_catequizando.nome_mae = form.nome_mae.data
        ficha_catequizando.nome_pai = form.nome_pai.data
        ficha_catequizando.batizado = form.batizado.data
        ficha_catequizando.eucaristia = form.eucaristia.data
        ficha_catequizando.escolaridade = form.escolaridade.data
        ficha_catequizando.logradouro = form.logradouro.data
        ficha_catequizando.bairro = form.bairro.data
        ficha_catequizando.cidade = form.cidade.data
        ficha_catequizando.estado = form.estado.data
        ficha_catequizando.numero_casa = form.numero_casa.data
        ficha_catequizando.ponto_referencia = form.ponto_referencia.data
        ficha_catequizando.telefone = form.telefone.data
        ficha_catequizando.whatsapp = form.whatsapp.data
        db.session.commit()
        return redirect(url_for('visualizar_turma', id_turma=id_turma))

    elif form.errors != {} and form.is_submitted():
        for erro in form.errors:
            flash(form.errors[erro][0], 'erro')

    elif ficha_catequizando is None:
        flash('Roteiro não encontrado', 'erro')
        abort(404)

    return render_template('templates_catequista/editar_ficha_catequizando.html', roteiro=ficha_catequizando, form=form)


@app.route('/turma/<int:id_turma>/ficha_catequizando/<int:id_ficha_catequizando>/view')
@app.route('/turma/<int:id_turma>/ficha_catequizando/<int:id_ficha_catequizando>/')
@login_required
@autenticacao_catequista
def visualizar_ficha_catequizando(id_turma, id_ficha_catequizando):
    turma = TurmaDAO.query_turma(id_turma, current_user.id_comunidade, True)
    catequizando = CatequizandoDAO.query_fichas_catequizandos(id_ficha_catequizando, turma.id)
    return render_template('templates_catequista/ficha_catequizando.html', turma=turma, catequizando=catequizando)


@app.route('/turma/<int:id_turma>/ficha_catequizando/<int:id_ficha_catequizando>/delete')
@login_required
def apagar_ficha_catequizando(id_turma, id_ficha_catequizando):
    turma = TurmaDAO.query_turma(id_turma, current_user.id_comunidade, True)
    catequizando = CatequizandoDAO.query_ficha_catequizando_turma(id_ficha_catequizando, id_turma, True)

    if catequizando and current_user.coordenacao:
        db.session.delete(catequizando)
        turma.atualizar_qt_catequizandos()
        db.session.commit()
        flash('Ficha apagada', 'sucesso')
        return redirect(url_for('visualizar_turma', id_turma=id_turma))


'''
########################################################################
                          ROTAS DE ENCONTRO
########################################################################
'''


@app.route('/turma/<int:id_turma>/encontro/all')
@app.route('/turma/<int:id_turma>/encontro/')
@login_required
@autenticacao_catequista
def encontros(id_turma):
    turma = TurmaDAO.query_turma(id_turma, current_user.id_comunidade, True)
    dict_encontros = EncontroDAO.query_encontros(current_user.id_comunidade, id_turma, True)
    return render_template('templates_catequista/list_encontros.html', turma=turma, dict_encontros=dict_encontros)


@app.route('/turma/<int:id_turma>/encontro/add', methods=['get', 'post'])
@login_required
@autenticacao_catequista
def adicionar_encontro(id_turma):
    form = EncontroForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        encontro = Encontro(
            id_comunidade=current_user.id_comunidade,
            id_turma=id_turma,
            tema=form.tema.data,
            data=form.data.data,
            numero=form.numero.data,
            leitura=form.leitura.data,
            atividade=form.atividade.data,
            compromisso=form.compromisso.data,
            avisos=form.avisos.data
        )
        db.session.add(encontro)
        db.session.commit()
        flash('Encontro adicionado', 'sucesso')
        return redirect(url_for('encontros', id_turma=id_turma))

    elif form.errors != {} and form.is_submitted():
        for erro in form.errors:
            flash(form.errors[erro][0], 'erro')

    return render_template('templates_catequista/adicionar_encontro.html', form=form)


@app.route('/turma/<int:id_turma>/encontro/<int:id_encontro>/edit', methods=['get', 'post'])
@login_required
@autenticacao_catequista
def editar_encontro(id_turma, id_encontro):
    encontro = EncontroDAO.query_encontro(id_encontro, current_user.id_comunidade, id_turma, True)
    form = EditarEncontroForm(formdata=request.form, obj=encontro)

    if form.validate_on_submit() and request.method == 'POST':
        encontro.tema = form.tema.data
        encontro.data = form.data.data
        encontro.numero = form.numero.data
        encontro.leitura = form.leitura.data
        encontro.atividade = form.atividade.data
        encontro.compromisso = form.compromisso.data
        encontro.avisos = form.avisos.data
        db.session.commit()
        return redirect(url_for('visualizar_encontro', id_turma=id_turma, id_encontro=id_encontro))

    elif form.errors != {} and form.is_submitted():
        for erro in form.errors:
            flash(form.errors[erro][0], 'erro')

    elif encontro is None:
        flash('Encontro não encontrado', 'erro')
        abort(404)

    return render_template('templates_catequista/editar_encontro.html', encontro=encontro, form=form)


@app.route('/turma/<int:id_turma>/encontro/<int:id_encontro>/view')
@app.route('/turma/<int:id_turma>/encontro/<int:id_encontro>/')
@login_required
@autenticacao_catequista
def visualizar_encontro(id_turma, id_encontro):
    turma = TurmaDAO.query_turma(id_turma, current_user.id_comunidade, True)
    encontro = EncontroDAO.query_encontro_turma(id_encontro, current_user.id_comunidade, id_turma, True)
    return render_template('templates_catequista/view_encontro.html', turma=turma, encontro=encontro)

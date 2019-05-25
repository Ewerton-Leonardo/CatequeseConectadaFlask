from app import app, db
from flask import render_template, flash, redirect, url_for, request, abort
from flask_login import logout_user, login_required, current_user

from app.services.encontro_services import EncontroDAO
from app.services.turma_services import TurmaDAO


@app.route('/encontros_catequizando')
@login_required
def encontros_catequizando():
    encontros = EncontroDAO.query_encontros_id_turma(current_user.id_turma)
    return render_template("templates_catequizando/encontros.html", encontros=encontros)


@app.route('/turma_catequizando')
@login_required
def turma_catequizando():
    turma = TurmaDAO.query_catequizando_turma(current_user.id_turma, current_user.id_comunidade)
    return render_template("templates_catequizando/turma.html", turma=turma)

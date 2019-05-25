from app.models.tables import Turma, FichaCatequizando
from app.models.forms import TurmaForm
from app import db


class TurmaDAO:
    @classmethod
    def adicionar(cls, turma: Turma):
        db.session.add(turma)
        db.session.commit()

    @classmethod
    def update(cls, turma: Turma, form_turma: TurmaForm):
        turma.nome = form_turma.nome.data
        turma.ano = form_turma.ano.data
        turma.tipo = form_turma.tipo.data
        db.session.commit()

    @classmethod
    def delete(cls, turma: Turma):
        db.session.delete(turma)
        db.session.commit()

    @classmethod
    def query_turma(cls, id_turma, id_comunidade, not_found=False):
        if not_found:
            turma = Turma.query.filter_by(id=id_turma, id_comunidade=id_comunidade).first_or_404()
        else:
            turma = Turma.query.filter_by(id=id_turma, id_comunidade=id_comunidade).first()
        if turma:
            return turma
        else:
            return False

    @classmethod
    def query_codigo_turma(cls, codigo, not_found=False):
        if not_found:
            turma = Turma.query.filter_by(codigo=codigo).first_or_404()
        else:
            turma = Turma.query.filter_by(codigo=codigo).first()
        if turma:
            return turma
        else:
            return False

    @classmethod
    def query_turmas(cls, id_comunidade):
        turmas = Turma.query.filter_by(id_comunidade=id_comunidade).all()
        if turmas:
            return turmas
        else:
            return False

    @classmethod
    def query_catequizando_turma(cls, id_turma, id_comunidade):
        catequizandos = FichaCatequizando.query.filter_by(id_turma=id_turma, id_comunidade=id_comunidade).all()
        if catequizandos:
            return catequizandos
        else:
            return False

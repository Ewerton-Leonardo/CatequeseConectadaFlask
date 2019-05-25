from app.models.tables import Encontro
from app.models.forms import EncontroForm
from app import db


class EncontroDAO:
    @classmethod
    def adicionar(cls, encontro: Encontro):
        db.session.add(encontro)
        db.session.commit()

    @classmethod
    def update(cls, encontro: Encontro, form_encontro: EncontroForm):
        encontro.tema = form_encontro.tema.data
        encontro.data = form_encontro.data.data
        encontro.numero = form_encontro.numero.data
        encontro.leitura = form_encontro.leitura.data
        encontro.atividade = form_encontro.atividade.data
        encontro.compromisso = form_encontro.compromisso.data
        encontro.avisos = form_encontro.avisos.data
        db.session.commit()

    @classmethod
    def delete(cls, encontro: Encontro):
        db.session.delete(encontro)
        db.session.commit()

    @classmethod
    def query_encontros_id_turma(cls, id_turma):
        encontros = Encontro.query.filter_by(id_turma=id_turma).all()
        if encontros:
            return encontros
        else:
            return False

    @classmethod
    def query_encontro(cls, id_encontro, id_comunidade, id_turma, not_found=False):
        if not_found:
            encontro = Encontro.query.filter_by(id=id_encontro, id_comunidade=id_comunidade, id_turma=id_turma).first_or_404()
        else:
            encontro = Encontro.query.filter_by(id=id_encontro, id_comunidade=id_comunidade, id_turma=id_turma).first()
        if encontro:
            return encontro
        else:
            return False

    @classmethod
    def query_encontros(cls, id_comunidade, id_turma, not_found=False):
        encontros = Encontro.query.filter_by(id_comunidade=id_comunidade, id_turma=id_turma).all()
        if encontros:
            return encontros
        else:
            return False

    @classmethod
    def query_encontro_turma(cls, id_encontro, id_comunidade, id_turma, not_found=False):
        if not_found:
            encontro = Encontro.query.filter_by(id=id_encontro, id_comunidade=id_comunidade, id_turma=id_turma).first_or_404()
        else:
            encontro = Encontro.query.filter_by(id=id_encontro, id_comunidade=id_comunidade, id_turma=id_turma).first()
        if encontro:
            return encontro
        else:
            return False

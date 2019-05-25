from app.models.tables import Catequista, FichaCatequista
from app.models.forms import CatequistaForm
from app import db


class CatequistaDAO:
    @classmethod
    def adicionar(cls, catequista: Catequista):
        db.session.add(catequista)
        db.session.commit()

    @classmethod
    def update(cls, catequista: Catequista, form_catequista: CatequistaForm):
        catequista.nome = form_catequista.nome.data
        catequista.coordenacao = form_catequista.coordenacao.data
        db.session.commit()

    @classmethod
    def delete(cls, catequista: Catequista):
        db.session.delete(catequista)
        db.session.commit()

    @classmethod
    def query_coordenador(cls, id_comunidade, not_found=False):
        if not_found:
            coordenador = Catequista.query.filter_by(id_comunidade=id_comunidade, coordenador=True).first_or_404()
        else:
            coordenador = Catequista.query.filter_by(id_comunidade=id_comunidade, coordenador=True).first()
        if coordenador:
            return coordenador
        else:
            return False

    @classmethod
    def query_catequista_user(cls, id_user, not_found=False):
        if not_found:
            catequista = Catequista.query.filter_by(id_user=id_user).first_or_404()
        else:
            catequista = Catequista.query.filter_by(id_user=id_user).first()
        if catequista:
            return catequista
        else:
            return False

    @classmethod
    def query_catequista_id(cls, id_catequista, not_found=False):
        if not_found:
            catequista = Catequista.query.filter_by(id=id_catequista).first_or_404()
        else:
            catequista = Catequista.query.filter_by(id=id_catequista).first()
        if catequista:
            return catequista
        else:
            return False

    @classmethod
    def query_ficha_catequista(cls, id_catequista, not_found=False):
        if not_found:
            ficha_catequista = FichaCatequista.query.filter_by(id_catequista=id_catequista).first_or_404()
        else:
            ficha_catequista = FichaCatequista.query.filter_by(id_catequista=id_catequista).first()
        if ficha_catequista:
            return ficha_catequista
        else:
            return False

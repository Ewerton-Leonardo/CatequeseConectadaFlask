from app.models.tables import Comunidade
from app.models.forms import ComunidadeForm
from app import db


class ComunidadeDAO:
    @classmethod
    def adicionar(cls, comunidade: Comunidade):
        db.session.add(comunidade)
        db.session.commit()

    @classmethod
    def update(cls, comunidade: Comunidade, form_comunidade: ComunidadeForm):
        comunidade.diocese = form_comunidade.diocese.data
        comunidade.paroquia = form_comunidade.paroquia.data
        comunidade.nome = form_comunidade.nome.data
        db.session.commit()

    @classmethod
    def delete(cls, comunidade: Comunidade):
        db.session.delete(comunidade)
        db.session.commit()

    @classmethod
    def query_comunidade(cls, nome, paroquia, diocese, not_found=False):
        if not_found:
            comunidade = Comunidade.query.filter_by(nome=nome, paroquia=paroquia, diocese=diocese).first_or_404()
        else:
            comunidade = Comunidade.query.filter_by(nome=nome, paroquia=paroquia, diocese=diocese).first()
        if comunidade:
            return comunidade
        else:
            return False

    @classmethod
    def query_dioceses(cls):
        comunidades = Comunidade.query.with_entities(Comunidade.diocese).distinct()
        if comunidades:
            return comunidades
        else:
            return False

    @classmethod
    def query_paroquias_diocese(cls, diocese):
        comunidades = Comunidade.query.filter_by(diocese=diocese).with_entities(Comunidade.paroquia).distinct()
        if comunidades:
            return comunidades
        else:
            return False

    @classmethod
    def query_comunidades_diocese_paroquia(cls, diocese, paroquia):
        comunidades = Comunidade.query.filter_by(diocese=diocese, paroquia=paroquia).all()
        if comunidades:
            return comunidades
        else:
            return False

    @classmethod
    def query_order_comunidades(cls):
        comunidades = Comunidade.query.order_by(Comunidade.nome).all()
        if comunidades:
            return comunidades
        else:
            return False

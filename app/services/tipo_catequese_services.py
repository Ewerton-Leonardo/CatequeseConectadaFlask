from app.models.tables import TipoCatequese, CatequistaTipoCatequese
from app.models.forms import TipoCatequeseForm
from app import db


class TipoCatequeseDAO:
    @classmethod
    def adicionar(cls, tipo_catequese: TipoCatequese):
        db.session.add(tipo_catequese)
        db.session.commit()

    @classmethod
    def update(cls, tipo_catequese: TipoCatequese, form_tipo_catequese: TipoCatequeseForm):
        tipo_catequese.nome = form_tipo_catequese.nome.data
        db.session.commit()

    @classmethod
    def delete(cls, tipo_catequese: TipoCatequese):
        db.session.delete(tipo_catequese)
        db.session.commit()

    @classmethod
    def query_tipo_catequese_nome(cls, nome, not_found=False):
        if not_found:
            tipo_catequese = TipoCatequese.query.filter_by(nome=nome).first_or_404()
        else:
            tipo_catequese = TipoCatequese.query.filter_by(nome=nome).first()
        if tipo_catequese:
            return tipo_catequese
        else:
            return False

    @classmethod
    def query_tipo_catequese_id(cls, id, not_found=False):
        if not_found:
            tipo_catequese = TipoCatequese.query.filter_by(id=id).first_or_404()
        else:
            tipo_catequese = TipoCatequese.query.filter_by(id=id).first()
        if tipo_catequese:
            return tipo_catequese
        else:
            return False

    @classmethod
    def query_tipos_catequeses_all(cls):
        tipos_catequeses = TipoCatequese.query.all()
        if tipos_catequeses:
            return tipos_catequeses
        else:
            return False

    @classmethod
    def query_tipos_catequeses_catequista(cls, id_catequista):
        tipos_catequeses_catequista = CatequistaTipoCatequese.query.filter_by(id_catequista=id_catequista).all()

        if tipos_catequeses_catequista:
            return tipos_catequeses_catequista
        else:
            return False

    @classmethod
    def query_order_tipo_catequese(cls):
        tipos_catequeses = TipoCatequese.query.order_by(TipoCatequese.nome).all()
        if tipos_catequeses:
            return tipos_catequeses
        else:
            return False

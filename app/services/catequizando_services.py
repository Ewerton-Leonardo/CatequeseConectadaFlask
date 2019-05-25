from app.models.tables import FichaCatequizando, Catequizando
from app.models.forms import FichaCatequizandoForm, EditarFichaCatequizandoForm, CatequizandoForm
from app import db


class CatequizandoDAO:
    @classmethod
    def add_roteiro(cls, catequizando: Catequizando):
        db.session.add(catequizando)
        db.session.commit()

    @classmethod
    def update(cls, catequizando: Catequizando, form_catequizando: CatequizandoForm):
        catequizando.nome = form_catequizando.nome.data
        db.session.commit()

    @classmethod
    def delete(cls, catequizando: Catequizando):
        db.session.delete(catequizando)
        db.session.commit()

    @classmethod
    def query_catequizando(cls, id_user, not_found=False):
        if not_found:
            catequizando = Catequizando.query.filter_by(id_user=id_user).first_or_404()
        else:
            catequizando = Catequizando.query.filter_by(id_user=id_user).first()
        if catequizando:
            return catequizando
        else:
            return False

    @classmethod
    def adicionar_ficha(cls, ficha_catequizando: FichaCatequizando):
        db.session.add(ficha_catequizando)
        db.session.commit()

    @classmethod
    def update_ficha(cls, ficha_catequizando: FichaCatequizando, form_ficha_catequizando: FichaCatequizandoForm):
        ficha_catequizando.nome = form_ficha_catequizando.nome_completo.data
        ficha_catequizando.data_nasc = form_ficha_catequizando.data_nasc.data
        ficha_catequizando.nome_mae = form_ficha_catequizando.nome_mae.data
        ficha_catequizando.nome_pai = form_ficha_catequizando.nome_pai.data
        ficha_catequizando.batizado = form_ficha_catequizando.batizado.data
        ficha_catequizando.eucaristia = form_ficha_catequizando.eucaristia.data
        ficha_catequizando.escolaridade = form_ficha_catequizando.escolaridade.data
        ficha_catequizando.logradouro = form_ficha_catequizando.logradouro.data
        ficha_catequizando.bairro = form_ficha_catequizando.bairro.data
        ficha_catequizando.cidade = form_ficha_catequizando.cidade.data
        ficha_catequizando.estado = form_ficha_catequizando.estado.data
        ficha_catequizando.numero_casa = form_ficha_catequizando.numero_casa.data
        ficha_catequizando.ponto_referencia = form_ficha_catequizando.ponto_referencia.data
        ficha_catequizando.telefone = form_ficha_catequizando.telefone.data
        ficha_catequizando.whatsapp = form_ficha_catequizando.whatsapp.data
        db.session.commit()

    @classmethod
    def delete_ficha(cls, ficha_catequizando: FichaCatequizando):
        db.session.delete(ficha_catequizando)
        db.session.commit()

    @classmethod
    def query_ficha_catequizando(cls, id_ficha_catequizando, not_found=False):
        if not_found:
            ficha_catequizando = FichaCatequizando.query.filter_by(cls, id=id_ficha_catequizando).first_or_404()
        else:
            ficha_catequizando = FichaCatequizando.query.filter_by(cls, id=id_ficha_catequizando).first()
        if ficha_catequizando:
            return ficha_catequizando
        else:
            return False

    @classmethod
    def query_ficha_catequizando_turma(cls, id_ficha_catequizando, id_turma, not_found=False):
        if not_found:
            ficha_catequizando = FichaCatequizando.query.filter_by(cls, id=id_ficha_catequizando, id_turma=id_turma).first_or_404()
        else:
            ficha_catequizando = FichaCatequizando.query.filter_by(cls, id=id_ficha_catequizando, id_turma=id_turma).first()
        if ficha_catequizando:
            return ficha_catequizando
        else:
            return False

    @classmethod
    def query_fichas_catequizandos(cls, id_comunidade, id_turma, not_found=False):
        if not_found:
            fichas = FichaCatequizando.query.filter_by(id_comunidade=id_comunidade, id_turma=id_turma).first_or_404()
        else:
            fichas = FichaCatequizando.query.filter_by(id_comunidade=id_comunidade, id_turma=id_turma).first()
        if fichas:
            return fichas
        else:
            return False

    @classmethod
    def query_order_fichas_catequizandos(cls, id_turma, not_found=False):
        if not_found:
            fichas = FichaCatequizando.query.filter_by(id_turma=id_turma).order_by('nome').all_or_404()
        else:
            fichas = FichaCatequizando.query.filter_by(id_turma=id_turma).order_by('nome').all()
        if fichas:
            return fichas
        else:
            return False

    @classmethod
    def query_ficha_catequizando_comunidade(cls, id_ficha_catequizando, id_comunidade, id_turma, not_found=False):
        if not_found:
            ficha_catequizando = FichaCatequizando.query.filter_by(cls, id=id_ficha_catequizando,
                                                                   id_turma=id_turma).first_or_404()
        else:
            ficha_catequizando = FichaCatequizando.query.filter_by(cls, id=id_ficha_catequizando,
                                                                   id_turma=id_turma).first()
        if ficha_catequizando:
            return ficha_catequizando
        else:
            return False

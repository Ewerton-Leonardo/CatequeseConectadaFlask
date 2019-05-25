from app.models.tables import Roteiro
from app.models.forms import RoteiroForm
from app import db


class RoteiroDAO:
    @classmethod
    def add_roteiro(cls, roteiro: Roteiro):
        db.session.add(roteiro)
        db.session.commit()

    @classmethod
    def update(cls, roteiro: Roteiro, form_roteiro: RoteiroForm):
        roteiro.tema = form_roteiro.tema.data
        roteiro.tipo = form_roteiro.tipo.data
        roteiro.ambiente = form_roteiro.ambiente.data
        roteiro.acolhida = form_roteiro.acolhida.data
        roteiro.oracao_inicial = form_roteiro.oracao_inicial.data
        roteiro.dinamica = form_roteiro.dinamica.data
        roteiro.motivacao = form_roteiro.motivacao.data
        roteiro.leituras = form_roteiro.leituras.data
        roteiro.desenvolvimento = form_roteiro.desenvolvimento.data
        roteiro.atividade = form_roteiro.atividade.data
        roteiro.compromisso = form_roteiro.compromisso.data
        roteiro.avisos = form_roteiro.avisos.data
        roteiro.oracao_final = form_roteiro.oracao_final.data
        roteiro.observacoes = form_roteiro.observacoes.data
        roteiro.publico = form_roteiro.publico.data
        db.session.commit()

    @classmethod
    def delete(cls, roteiro: Roteiro):
        db.session.delete(roteiro)
        db.session.commit()

    @classmethod
    def load_update_form_roteiro(cls, form_roteiro: RoteiroForm, roteiro: Roteiro):
        form_roteiro.tema.data = roteiro.tema
        form_roteiro.tipo.data = roteiro.tipo
        form_roteiro.ambiente.data = roteiro.ambiente
        form_roteiro.acolhida.data = roteiro.acolhida
        form_roteiro.oracao_inicial.data = roteiro.oracao_inicial
        form_roteiro.dinamica.data = roteiro.dinamica
        form_roteiro.motivacao.data = roteiro.motivacao
        form_roteiro.leituras.data = roteiro.leituras
        form_roteiro.desenvolvimento.data = roteiro.desenvolvimento
        form_roteiro.atividade.data = roteiro.atividade
        form_roteiro.compromisso.data = roteiro.compromisso
        form_roteiro.avisos.data = roteiro.avisos
        form_roteiro.oracao_final.data = roteiro.oracao_final
        form_roteiro.observacoes.data = roteiro.observacoes

    @classmethod
    def query_roteiro(cls, id_roteiro, not_found=False):
        if not_found:
            roteiro = Roteiro.query.filter_by(id=id_roteiro).first_or_404()
        else:
            roteiro = Roteiro.query.filter_by(id=id_roteiro).first()
        if roteiro:
            return roteiro
        else:
            return False

    @classmethod
    def query_roteiros_comunidade(cls, id_comunidade, id_tipo_catequese):
        roteiros = Roteiro.query.filter_by(id_comunidade=id_comunidade, id_tipo_catequese=id_tipo_catequese).all()
        if roteiros:
            return roteiros
        else:
            return False

    @classmethod
    def query_roteiros_publicos(cls):
        roteiros_publicos = Roteiro.query.filter_by(publico='Público').order_by('tema').all()
        if roteiros_publicos:
            return roteiros_publicos
        else:
            return False

    @classmethod
    def query_roteiro_catequista(cls, id_roteiro, id_catequista, not_found=False):
        if not_found:
            roteiro = Roteiro.query.filter_by(id=id_roteiro, id_catequista=id_catequista).first_or_404()
        else:
            roteiro = Roteiro.query.filter_by(id=id_roteiro, id_catequista=id_roteiro).first()
        if roteiro:
            return roteiro
        else:
            return False

from app.models.tables import Catequista, Catequizando, Comunidade, Encontro, Roteiro, FichaCatequista, FichaCatequizando, Turma, TipoCatequese, User


def query_username(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return user
    else:
        return False


def query_user_id(id_user):
    user = User.query.filter_by(id=id_user).first()
    if user:
        return user
    else:
        return False


def query_catequista(id_user):
    catequista = Catequista.query.filter_by(id_user=id_user).first()
    if catequista:
        return catequista
    else:
        return False


def query_comunidade(nome, paroquia, diocese):
    comunidade = Comunidade.query.filter_by(nome=nome, paroquia=paroquia, diocese=diocese).first()
    if comunidade:
        return comunidade
    else:
        return False


def query_tipo_catequese(nome):
    tipo_catequese = TipoCatequese.query.filter_by(nome=nome).first()
    if tipo_catequese:
        return tipo_catequese
    else:
        return False


def query_coordenador(id_comunidade):
    coordenador = Catequista.query.filter_by(id_comunidade=id_comunidade, coordenador=True).first()
    if coordenador:
        return coordenador
    else:
        return False


def query_catequizando(id_user):
    catequizando = Catequizando.query.filter_by(id_user=id_user).first()
    if catequizando:
        return catequizando
    else:
        return False








def query_ficha_catequista(id_catequista):
    ficha_catequista = FichaCatequista.query.filter_by(id_catequista=id_catequista).first()
    if ficha_catequista:
        return ficha_catequista
    else:
        return False


def query_ficha_catequizando(id_ficha_catequizando):
    ficha_catequizando = FichaCatequizando.query.filter_by(id=id_ficha_catequizando).first()
    if ficha_catequizando:
        return ficha_catequizando
    else:
        return False


def query_fichas_catequizandos(id_comunidade, id_turma):
    fichas = FichaCatequizando.query.filter_by(id_comunidade=id_comunidade, id_turma=id_turma).first()
    if fichas:
        return fichas
    else:
        return False

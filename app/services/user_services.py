from app.models.tables import Catequista, Catequizando, Comunidade, Encontro, Roteiro, FichaCatequista, FichaCatequizando, Turma, TipoCatequese, User


class UserDAO:
    @classmethod
    def query_username(cls, username, not_found=False):
        if not_found:
            user = User.query.filter_by(username=username).first_or_404()
        else:
            user = User.query.filter_by(username=username).first()
        if user:
            return user
        else:
            return False

    @classmethod
    def query_user_id(cls, id_user, not_found=False):
        if not_found:
            user = User.query.filter_by(id=id_user).first_or_404()
        else:
            user = User.query.filter_by(id=id_user).first()
        if user:
            return user
        else:
            return False









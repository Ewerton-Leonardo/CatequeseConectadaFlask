from app import db
from app import lm
from datetime import date, datetime
import random


@lm.user_loader
def load_user(user_id):
    user = User.query.filter(User.id == user_id).first()
    if user.tipo == 'Catequista':
        return Catequista.query.filter(Catequista.id_user == user_id).first()
    elif user.tipo == 'Catequizando':
        return Catequizando.query.filter(Catequizando.id_user == user_id).first()
    else:
        return user


class Comunidade(db.Model):
    __tablename__ = 'comunidade'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    diocese = db.Column(db.String(20), nullable=False)
    paroquia = db.Column(db.String(30), nullable=False)
    nome = db.Column(db.String(30), nullable=False)

    def __init__(self,
                 diocese: str,
                 paroquia: str,
                 nome: str):
        self.diocese = diocese
        self.paroquia = paroquia
        self.nome = nome


class TipoCatequese(db.Model):
    __tablename__ = 'tipo_catequese'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(25), unique=True, nullable=False)

    def __init__(self, nome: str):
        self.nome = nome


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    senha = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.String(30), nullable=False)
    
    def __init__(self,
                 username: str,
                 senha: str,
                 tipo: str):
        self.username = username
        self.senha = senha
        self.tipo = tipo

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)


class Catequista(db.Model):
    __tablename__ = 'catequista'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    data_nasc = db.Column(db.Date, nullable=False)
    id_comunidade = db.Column(db.Integer, db.ForeignKey('comunidade.id'), nullable=False)
    coordenacao = db.Column(db.Boolean, nullable=False)

    comunidade = db.relationship('Comunidade', foreign_keys=id_comunidade)
    user = db.relationship('User', foreign_keys=id_user)

    def __init__(self,
                 id_user: int,
                 nome: str,
                 data_nasc: date,
                 id_comunidade: int,
                 coordernacao: bool):
        self.id_user = id_user
        self.nome = nome
        self.data_nasc = data_nasc
        self.id_comunidade = id_comunidade
        self.coordenacao = coordernacao

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False


class CatequistaTipoCatequese(db.Model):
    __tablename__ = 'catequista_tipo_catequese'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_catequista = db.Column(db.Integer, db.ForeignKey('catequista.id'), nullable=False)
    id_tipo_catequese = db.Column(db.Integer, db.ForeignKey('tipo_catequese.id'), nullable=False)

    catequista = db.relationship('Catequista', foreign_keys=id_catequista)
    tipo_catequese = db.relationship('TipoCatequese', foreign_keys=id_tipo_catequese)

    def __init__(self, id_catequista, id_tipo_catequese):
        self.id_catequista = id_catequista
        self.id_tipo_catequese = id_tipo_catequese


class FichaCatequista(db.Model):
    __tablename__ = 'ficha_catequista'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_catequista = db.Column(db.Integer, db.ForeignKey('catequista.id'), unique=True, nullable=False)
    id_comunidade = db.Column(db.Integer, db.ForeignKey('comunidade.id'), nullable=False)
    nome_completo = db.Column(db.String(50), nullable=False)
    data_nasc = db.Column(db.Date, nullable=False)
    ano_entrada = db.Column(db.Integer, nullable=False)
    escolaridade = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=True)
    whatsapp = db.Column(db.String(20), nullable=True)
    logradouro = db.Column(db.String(60), nullable=False)
    bairro = db.Column(db.String(30), nullable=False)
    cidade = db.Column(db.String(30), nullable=False)
    estado = db.Column(db.String(20), nullable=False)
    numero_casa = db.Column(db.String(15), nullable=False)
    ponto_referencia = db.Column(db.String(50), nullable=False)
    crismado = db.Column(db.String(3), nullable=False)

    catequista = db.relationship('Catequista', foreign_keys=id_catequista)
    comunidade = db.relationship('Comunidade', foreign_keys=id_comunidade)

    def __init__(self,
                 id_catequista: int,
                 id_comunidade: int,
                 nome_completo: str,
                 data_nasc: date,
                 ano_entrada: int,
                 escolaridade: str,
                 telefone: str,
                 whatsapp: str,
                 logradouro: str,
                 bairro: str,
                 cidade: str,
                 estado: str,
                 numero_casa: str,
                 ponto_referencia: str,
                 crismado: bool):
        self.id_catequista = id_catequista
        self.id_comunidade = id_comunidade
        self.nome_completo = nome_completo
        self.data_nasc = data_nasc
        self.ano_entrada = ano_entrada
        self.escolaridade = escolaridade
        self.telefone = telefone
        self.whatsapp = whatsapp
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.numero_casa = numero_casa
        self.ponto_referencia = ponto_referencia
        self.crismado = crismado


class Turma(db.Model):
    __tablename__ = 'turma'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_comunidade = db.Column(db.Integer, db.ForeignKey('comunidade.id'), nullable=False)
    codigo = db.Column(db.String(6), nullable=False, unique=True)
    nome = db.Column(db.String(100), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    id_tipo_catequese = db.Column(db.Integer, db.ForeignKey('tipo_catequese.id'), nullable=False)
    qt_catequizandos = db.Column(db.Integer, nullable=False, default=0)

    comunidade = db.relationship('Comunidade', foreign_keys=id_comunidade)
    tipo_catequese = db.relationship('TipoCatequese', foreign_keys=id_tipo_catequese)

    def __init__(self, id_comunidade, nome, ano, id_tipo_catequese):
        self.id_comunidade = id_comunidade
        self.codigo = self.gerar_codigo()
        self.nome = nome
        self.ano = ano
        self.id_tipo_catequese = id_tipo_catequese

    def atualizar_qt_catequizandos(self):
        self.qt_catequizandos = FichaCatequizando.query.filter_by(id_turma=self.id).count()

    @staticmethod
    def gerar_codigo():
        letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(letras) for i in range(6))


class FichaCatequizando(db.Model):
    __tablename__ = 'ficha_catequizando'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_comunidade = db.Column(db.Integer, db.ForeignKey('comunidade.id'), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    data_nasc = db.Column(db.Date, nullable=False)
    nome_mae = db.Column(db.String(50), nullable=False)
    nome_pai = db.Column(db.String(50), nullable=False)
    batizado = db.Column(db.String(3), nullable=False)
    eucaristia = db.Column(db.String(3))
    escolaridade = db.Column(db.String, nullable=False)
    logradouro = db.Column(db.String(60), nullable=False)
    bairro = db.Column(db.String(30), nullable=False)
    cidade = db.Column(db.String(30), nullable=False)
    estado = db.Column(db.String(20), nullable=False)
    numero_casa = db.Column(db.String, nullable=False)
    ponto_referencia = db.Column(db.String, nullable=False)
    telefone = db.Column(db.String(15), nullable=False)
    whatsapp = db.Column(db.String(15))
    data_inscricao = db.Column(db.Date, nullable=False)
    id_turma = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)

    comunidade = db.relationship('Comunidade', foreign_keys=id_comunidade)
    turma = db.relationship('Turma', foreign_keys=id_turma)

    def __init__(self,
                 id_comunidade: int,
                 nome: str,
                 data_nasc: date,
                 nome_mae: str,
                 nome_pai: str,
                 batizado: str,
                 eucaristia: str,
                 escolaridade: str,
                 logradouro: str,
                 bairro: str,
                 cidade: str,
                 estado: str,
                 numero_casa: str,
                 ponto_referencia: str,
                 telefone: str,
                 whatsapp: str,
                 data_inscricao: date,
                 id_turma: int):
        self.id_comunidade = id_comunidade
        self.nome = nome
        self.data_nasc = data_nasc
        self.nome_mae = nome_mae
        self.nome_pai = nome_pai
        self.batizado = batizado
        self.eucaristia = eucaristia
        self.escolaridade = escolaridade
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.numero_casa = numero_casa
        self.ponto_referencia = ponto_referencia
        self.telefone = telefone
        self.whatsapp = whatsapp
        self.data_inscricao = data_inscricao
        self.id_turma = id_turma


class Catequizando(db.Model):
    __tablename__ = 'catequizando'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    id_turma = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)
    id_comunidade = db.Column(db.Integer, db.ForeignKey('comunidade.id'), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    data_nasc = db.Column(db.Date, nullable=False)

    user = db.relationship('User', foreign_keys=id_user)
    comunidade = db.relationship('Comunidade', foreign_keys=id_comunidade)

    def __init__(self,
                 id_user,
                 id_turma,
                 id_comunidade,
                 nome,
                 data_nasc):
        self.id_user = id_user
        self.id_turma = id_turma
        self.id_comunidade = id_comunidade
        self.nome = nome
        self.data_nasc = data_nasc

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False


class Roteiro(db.Model):
    __tablename__ = 'roteiro'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_catequista = db.Column(db.Integer, db.ForeignKey('catequista.id'), nullable=False)
    id_comunidade = db.Column(db.Integer, db.ForeignKey('comunidade.id'), nullable=False)
    id_tipo_catequese = db.Column(db.Integer, db.ForeignKey('tipo_catequese.id'), nullable=False)
    tema = db.Column(db.String(50), nullable=False)
    ambiente = db.Column(db.Text, nullable=True)
    acolhida = db.Column(db.Text, nullable=True)
    oracao_inicial = db.Column(db.Text, nullable=True)
    dinamica = db.Column(db.Text, nullable=True)
    motivacao = db.Column(db.Text, nullable=True)
    leituras = db.Column(db.Text, nullable=True)
    desenvolvimento = db.Column(db.Text, nullable=True)
    atividade = db.Column(db.Text, nullable=True)
    compromisso = db.Column(db.Text, nullable=True)
    avisos = db.Column(db.Text, nullable=True)
    oracao_final = db.Column(db.Text, nullable=True)
    observacoes = db.Column(db.Text, nullable=True)
    publico = db.Column(db.String(10), nullable=False)
    data_now = db.Column(db.Date, nullable=False, default=date.today())

    catequista = db.relationship('Catequista', foreign_keys=id_catequista)
    comunidade = db.relationship('Comunidade', foreign_keys=id_comunidade)
    tipo_catequese = db.relationship('TipoCatequese', foreign_keys=id_tipo_catequese)

    def __init__(self,
                 id_catequista: int,
                 id_comunidade: int,
                 tema: str,
                 ambiente: str,
                 acolhida: str,
                 oracao_inicial: str,
                 dinamica: str,
                 motivacao: str,
                 leituras: str,
                 desenvolvimento: str,
                 atividade: str,
                 compromisso: str,
                 avisos: str,
                 oracao_final: str,
                 observacoes: str,
                 tipo: str,
                 publico: bool):
        self.id_catequista = id_catequista
        self.id_comunidade=id_comunidade
        self.tema = tema
        self.ambiente = ambiente
        self.acolhida = acolhida
        self.oracao_inicial = oracao_inicial
        self.dinamica = dinamica
        self.motivacao = motivacao
        self.leituras = leituras
        self.desenvolvimento = desenvolvimento
        self.atividade = atividade
        self.compromisso = compromisso
        self.avisos = avisos
        self.oracao_final = oracao_final
        self.observacoes = observacoes
        self.tipo = tipo
        self.data_now = date.today()
        self.publico = publico


class Notificacao(db.Model):
    __tablename__ = 'notificacao'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_emissor = db.Column(db.Integer, db.ForeignKey('catequista.id'), nullable=False)
    id_comunidade = db.Column(db.Integer, db.ForeignKey('comunidade.id'), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)
    assunto = db.Column(db.String(30), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)

    emissor = db.relationship('Catequista', foreign_keys=id_emissor)
    comunidade = db.relationship('Comunidade', foreign_keys=id_comunidade)

    def __init__(self,
                 id_emissor: int,
                 id_comunidade: int,
                 data_hora: datetime,
                 assunto: str,
                 mensagem: str):
        self.id_emissor = id_emissor
        self.id_comunidade = id_comunidade
        self.data_hora = data_hora
        self.assunto = assunto
        self.mensagem = mensagem


class Encontro(db.Model):
    __tablename__ = 'encontro'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_comunidade = db.Column(db.Integer, db.ForeignKey('comunidade.id'), nullable=False)
    id_turma = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)
    tema = db.Column(db.String(30), nullable=False)
    data = db.Column(db.Date, nullable=False)
    numero = db.Column(db.Integer, nullable=True)
    leitura = db.Column(db.Text, nullable=True)
    atividade = db.Column(db.Text, nullable=True)
    compromisso = db.Column(db.Text, nullable=True)
    avisos = db.Column(db.Text, nullable=True)

    comunidade = db.relationship('Comunidade', foreign_keys=id_comunidade)
    turma = db.relationship('Turma', foreign_keys=id_turma)

    def __init__(self,
                 id_comunidade: int,
                 id_turma: int,
                 tema: str,
                 data: str,
                 numero: int,
                 leitura: str,
                 atividade: str,
                 compromisso: str,
                 avisos: str):
        self.id_comunidade = id_comunidade
        self.id_turma = id_turma
        self.tema = tema
        self.data = data
        self.numero = numero
        self.leitura = leitura
        self.atividade = atividade
        self.compromisso = compromisso
        self.avisos = avisos


'''
class Frequencia(db.Model):
    __tablename__ = 'frequencia'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_encontro = db.Column(db.Integer, db.ForeignKey('encontro.id'), nullable=False)
    id_catequizando = db.Column(db.Integer, db.ForeignKey('ficha_catequizando.id'), nullable=False)
    presenca = db.Column(db.String(15), nullable=False)

    encontro = db.relationship('Encontro', foreign_keys=id_encontro)
    catequizando = db.relationship('FichaCatequizando', foreign_keys=id_catequizando)

    def __init__(self,
                 id_encontro: int,
                 id_catequizando: int,
                 presenca: str):
        self.id_encontro = id_encontro
        self.id_catequizando = id_catequizando
        self.presenca = presenca
'''


def get_idade(data_nasc):
    data_hoje = date.today()
    idade = data_hoje.year - data_nasc.year
    if data_nasc.month > data_hoje.month:
        idade -= 1
    elif data_nasc.month == data_hoje.month:
        if data_nasc.day < data_hoje.day:
            idade -= 1
    return idade




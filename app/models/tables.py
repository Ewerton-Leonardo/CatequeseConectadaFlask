from app import db
from datetime import date, datetime


class Comunidade(db.Model):
    __tablename__ = 'comunidade'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    diocese = db.Column(db.String(20), nullable=False)
    paroquia = db.Column(db.String(30), nullable=False)
    nome = db.Column(db.String(30), nullable=False)
    logradouro = db.Column(db.String(60), nullable=True)
    bairro = db.Column(db.String(30), nullable=True)
    cidade = db.Column(db.String(30), nullable=False)
    estado = db.Column(db.String(20), nullable=False)
    numero = db.Column(db.String(15), nullable=True)

    def __init__(self,
                 diocese: str,
                 paroquia: str,
                 nome: str,
                 logradouro: str,
                 bairro: str,
                 cidade: str,
                 estado: str,
                 numero: str):
        self.diocese = diocese
        self.paroquia = paroquia
        self.nome = nome
        self.logradouro = logradouro
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.numero = numero


class Catequista(db.Model):
    __tablename__ = 'catequista'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, unique=True)
    username = db.Column(db.String(20), primary_key=True)
    senha = db.Column(db.String(30), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    id_comunidade = db.Column(db.Integer, db.ForeignKey('comunidade.id'), nullable=False)
    tipo1 = db.Column(db.String(20), nullable=False)
    tipo2 = db.Column(db.String(20), nullable=True)
    coordenacao = db.Column(db.Boolean, nullable=False)

    comunidade = db.relationship('Comunidade', foreign_keys=id_comunidade)

    def __init__(self,
                 username: str,
                 senha: str,
                 nome: str,
                 id_comunidade: str,
                 tipo1: str,
                 tipo2: str,
                 coordernacao: bool):
        self.username = username
        self.senha = senha
        self.nome = nome
        self.id_comunidade = id_comunidade
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.coordenacao = coordernacao

    @property
    def is_autheticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymus(self):
        return False

    def get_id(self):
        return str(self.id)


class FichaCatequista(db.Model):
    __tablename__ = 'ficha_catequista'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_catequista = db.Column(db.Integer, db.ForeignKey('catequista.id'), unique=True, nullable=False)
    id_comunidade = db.Column(db.Integer, db.ForeignKey('comunidade.id'), nullable=False)
    nome_completo = db.Column(db.String(50), nullable=False)
    data_nasc = db.Column(db.Date, nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    ano_entrada = db.Column(db.Integer, nullable=False)
    escolaridade = db.Column(db.String(20), nullable=False)
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
                 id_catequista: str,
                 id_comunidade: str,
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


class FichaCatequisando(db.Model):
    __tablename__ = 'ficha_catequisando'

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
    telefone1 = db.Column(db.String(15), nullable=False)
    telefone2 = db.Column(db.String(15))
    whatsapp = db.Column(db.String(15))
    data_inscricao = db.Column(db.Date, nullable=False)
    ano_turma = db.Column(db.String(20), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)

    comunidade = db.relationship('Comunidade', foreign_keys=id_comunidade)

    def __init__(self,
                 id_comunidade: str,
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
                 telefone1: str,
                 telefone2: str,
                 whatsapp: str,
                 frequencia: float,
                 data_inscricao: date,
                 ano_turma: str,
                 tipo: str):
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
        self.telefone1 = telefone1
        self.telefone2 = telefone2
        self.whatsapp = whatsapp
        self.frequencia = frequencia
        self.data_inscricao = data_inscricao
        self.ano_turma = ano_turma
        self.tipo = tipo


class Roteiro(db.Model):
    __tablename__ = 'roteiro'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_catequista = db.Column(db.Integer, db.ForeignKey('catequista.id'), nullable=False)
    tema = db.Column(db.String(30), nullable=False)
    observacoes = db.Column(db.Text, nullable=False)
    data_now = db.Column(db.Date, nullable=False, default=date.today())

    catequista = db.relationship('Catequista', foreign_keys=id_catequista)

    def __init__(self,
                 id_catequista: str,
                 tema: str,
                 tipo: str,
                 anotacoes: str,
                 publico: bool):
        self.id_catequista = id_catequista
        self.data_now = date.today()
        self.tipo = tipo
        self.tema = tema
        self.anotacoes = anotacoes
        self.publico = publico


class Notificacao(db.Model):
    __tablename__ = 'notificacao'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_emissor = db.Column(db.Integer, db.ForeignKey('catequista.id'), nullable=False)
    id_comunidade = db.Column(db.Integer, db.ForeignKey('comunidade.id'), nullable=False)
    data_hora = db.Column(db.DateTime, nullable=False)
    assunto = db.Column(db.String(20), nullable=False)
    mensagem = db.Column(db.Text, nullable=False)

    emissor = db.relationship('Catequista', foreign_keys=id_emissor)
    comunidade = db.relationship('Comunidade', foreign_keys=id_comunidade)

    def __init__(self,
                 id_emissor: str,
                 id_comunidade: str,
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
    ano_turma = db.Column(db.String, nullable=False)
    tema = db.Column(db.String(30), nullable=False)
    data = db.Column(db.Date, nullable=False)
    numero = db.Column(db.Integer, nullable=True)
    leitura = db.Column(db.Text, nullable=True)
    atividade = db.Column(db.Text, nullable=True)
    compromisso = db.Column(db.Text, nullable=True)
    avisos = db.Column(db.Text, nullable=True)

    comunidade = db.relationship('Comunidade', foreign_keys=id_comunidade)

    def __init__(self,
                 id_comunidade: str,
                 ano_turma: str,
                 tema: str,
                 data: str,
                 numero: int,
                 leitura: str,
                 atividade: str,
                 compromisso: str,
                 avisos: str):
        self.id_comunidade = id_comunidade
        self.ano_turma = ano_turma
        self.tema = tema
        self.data = data
        self.numero = numero
        self.leitura = leitura
        self.atividade = atividade
        self.compromisso = compromisso
        self.avisos = avisos


class Frequencia(db.Model):
    __tablename__ = 'frequencia'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_encontro = db.Column(db.Integer, db.ForeignKey('encontro.id'), nullable=False)
    id_catequisando = db.Column(db.Integer, db.ForeignKey('ficha_catequisando.id'), nullable=False)
    presenca = db.Column(db.String(15), nullable=False)

    encontro = db.relationship('Encontro', foreign_keys=id_encontro)
    catequisando = db.relationship('FichaCatequisando', foreign_keys=id_catequisando)

    def __init__(self,
                 id_encontro: str,
                 id_catequisando: str,
                 presenca: bool):
        self.id_encontro = id_encontro
        self.id_catequisando = id_catequisando
        self.presenca = presenca


def getIdade(data_nasc):
    data_hoje = date.today()
    idade = data_hoje.year - data_nasc.year
    if data_nasc.month > data_hoje.month:
        idade -= 1
    elif data_nasc.month == data_hoje.month:
        if data_nasc.day < data_hoje.day:
            idade -= 1
    return idade
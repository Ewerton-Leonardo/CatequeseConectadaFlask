from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, DateField, IntegerField, RadioField, HiddenField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class CadastroComunidadeForm(FlaskForm):
    nome = StringField('Nome da comunidade', validators=[DataRequired()])
    paroquia = StringField('Paróquia', validators=[DataRequired()])
    diocese = StringField('Diocese', validators=[DataRequired()])
    logradouro = StringField('Rua/Avenida', validators=[DataRequired(), Length(min=8, max=60)])
    bairro = StringField('Bairro', validators=[DataRequired(), Length(min=1, max=30)])
    cidade = StringField('Cidade', validators=[DataRequired(), Length(min=5, max=30)])
    estado = StringField('Estado', validators=[DataRequired(), Length(min=4, max=20)])
    numero = StringField('Número da casa', validators=[DataRequired(), Length(min=1, max=15)])


class CadastroCatequistaForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    nome = StringField('Nome', validators=[DataRequired()])
    comunidade = SelectField('Comunidade', validators=[DataRequired()], coerce=int)
    tipo1 = StringField('Tipo 1', validators=[DataRequired()])
    tipo2 = StringField('Tipo 2')
    coordenacao = RadioField('Você é coordenador?', coerce=bool, choices=[(True, 'Sim'), (False, 'Não')])


class FichaCatequistaForm(FlaskForm):
    nome_completo = StringField('Nome completo', validators=[DataRequired(), Length(min=10, max=50)])
    data_nasc = DateField('Data de nascimento', validators=[DataRequired()])
    ano_entrada = IntegerField('Ano de entrada como catequista', validators=[DataRequired(), Length(min=4, max=4)])
    escolaridade = StringField('Ecolaridade', validators=[DataRequired(), Length(min=1, max=20)])
    telefone = StringField('Número de telefone/celular', validators=[DataRequired(), Length(min=8, max=20)])
    whatsapp = StringField('Número do WhatsApp', validators=[DataRequired(), Length(min=8, max=20)])
    logradouro = StringField('Rua/Avenida', validators=[DataRequired(), Length(min=8, max=60)])
    bairro = StringField('Bairro', validators=[DataRequired(), Length(min=1, max=30)])
    cidade = StringField('Cidade', validators=[DataRequired(), Length(min=5, max=30)])
    estado = StringField('Estado', validators=[DataRequired(), Length(min=4, max=20)])
    numero_casa = StringField('Número da casa', validators=[DataRequired(), Length(min=1, max=15)])
    ponto_referencia = StringField('Ponto de referência', validators=[DataRequired(), Length(min=0, max=50)])
    crismado = RadioField('É crismado?', choices=[('Sim', 'Sim'), ('Não', 'Não')], validators=[DataRequired()])


class FichaCatequisandoForm(FlaskForm):
    nome_completo = StringField('Nome completo', validators=[DataRequired(), Length(min=10, max=50)])
    data_nasc = DateField('Data de nascimento', validators=[DataRequired()])
    nome_mae = StringField('Nome da mãe', validators=[DataRequired()])
    nome_pai = StringField('Nome da pai', validators=[DataRequired()])
    batizado = RadioField('É batizado?', choices=[('Sim', 'Sim'), ('Não', 'Não')], validators=[DataRequired()])
    eucaristia = RadioField('Já fez a primeira eucaristia?', choices=[('Sim', 'Sim'), ('Não', 'Não')], validators=[DataRequired()])
    escolaridade = StringField('Escolaridade', validators=[DataRequired(), Length(min=1, max=20)])
    logradouro = StringField('Rua/Avenida', validators=[DataRequired(), Length(min=8, max=60)])
    bairro = StringField('Bairro', validators=[DataRequired(), Length(min=1, max=30)])
    cidade = StringField('Cidade', validators=[DataRequired(), Length(min=5, max=30)])
    estado = StringField('Estado', validators=[DataRequired(), Length(min=4, max=20)])
    numero_casa = StringField('Número da casa', validators=[DataRequired(), Length(min=1, max=15)])
    ponto_referencia = StringField('Ponto de referência', validators=[DataRequired(), Length(min=0, max=50)])
    telefone1 = StringField('Número de telefone/celular 1', validators=[DataRequired(), Length(min=8, max=20)])
    telefone2 = StringField('Número de telefone/celular 2', validators=[DataRequired(), Length(min=8, max=20)])
    whatsapp = StringField('Número do WhatsApp', validators=[DataRequired(), Length(min=8, max=20)])
    data_inscricao = DateField('Data de inscrição', validators=[DataRequired()])
    ano_turma = StringField('Nome ou ano da turma', validators=[DataRequired()])


class RoteiroForm(FlaskForm):
    tema = StringField('Tema', validators=DataRequired())
    conteudo = TextAreaField('Conteúdo', validators=DataRequired())


class EncontroForm(FlaskForm):
    ano_turma = SelectField('Nome ou ano da Turma', validators=DataRequired())
    tema = StringField('Tema', validators=DataRequired())
    data = DateField('Data do encontro', validators=DataRequired())
    numero = IntegerField('Número do encontro')
    leitura = TextAreaField('Leitura(s)')
    atividade = TextAreaField('Atividade')
    compromisso = TextAreaField('Compromisso')
    avisos = TextAreaField('Avisos')


class NotificacaoForm(FlaskForm):
    assunto = StringField('Assunto')
    mensagem = TextAreaField('Mensagem')


class LoginForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])


class TesteForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired('nefknk')])
    senha = PasswordField('Senha')
    nome = StringField('Nome', validators=[DataRequired('mfele')])
    comunidade = SelectField('Comunidade')
    tipo1 = StringField('Tipo 1', validators=[DataRequired('fmemkl')])
    tipo2 = StringField('Tipo 2')
    coordenacao = BooleanField('Você é coordenador?')
    enviar = SubmitField('Enviar')

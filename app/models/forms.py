from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, RadioField, HiddenField, SelectField, SubmitField, SelectFieldBase, widgets
from wtforms.compat import text_type
from copy import copy
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange, InputRequired
from wtforms.fields.html5 import DateField, TelField, IntegerField
from datetime import date


class SelectFieldNoValidate(SelectField):
    def __init__(self, label=None, validators=None, coerce=text_type, choices=None, **kwargs):
        super().__init__(label, validators, coerce, choices, **kwargs)

    def pre_validate(self, form):
        pass


class ComunidadeForm(FlaskForm):
    title_form = "Cadastro comunidade"
    nome = StringField('Nome da comunidade', validators=[DataRequired(message='Campo nome da comunidade requerido'), Length(min=2, max=50, message='Número de caracteres do campo nome da comunidade deve estar entre 2 e 50')])
    paroquia = StringField('Paróquia', validators=[DataRequired(message='Campo paróquia requerido'), Length(min=2, max=50, message='Número de caracteres do campo paróquia deve estar entre 2 e 50')])
    diocese = StringField('Diocese', validators=[DataRequired(message='Campo diocese requerido'), Length(min=2, max=50, message='Número de caracteres do campo diocese_dft deve estar entre 2 e 50')])
    submit = SubmitField('Cadastrar comunidade')


class DioceseForm(FlaskForm):
    diocese_select = SelectField('Diocese')
    paroquia_select = SelectField('Paróquia')
    comunidade_select = SelectField()


class TipoCatequeseForm(FlaskForm):
    title_form = "Adicionar tipo de catequese"
    nome = StringField('Nome da catequese', validators=[DataRequired('Campo nome da catequese requerido'), Length(min=4, max=25, message='Número de caracteres do campo nome da catequese deve estar entre 4 e 25')])
    submit = SubmitField('Adicionar')


class CatequistaTipoCatequeseForm(FlaskForm):
    title_form = "Relacionar tipo de catequese"
    tipo_catequese = SelectField('Tipo de catequese', coerce=int, validators=[DataRequired(message='Campo tipo de catequese requerido')])
    submit = SubmitField('Adicionar')


class CatequistaForm(FlaskForm):
    title_form = "Cadastro catequista"
    username = StringField('Nome de usuário', validators=[DataRequired(message='Campo nome de usuário requerido'), Length(min=4, max=20, message='Número de caracteres do campo  deve estar entre 4 e 20')])
    senha = PasswordField('Senha', validators=[DataRequired(message='Campo senha requerido'), Length(min=6, max=30, message='Número de caracteres do campo  deve estar entre 6 e 30')])
    confirma_senha = PasswordField('Confirma senha', validators=[DataRequired(message='Campo confirma senha requerido'), EqualTo('senha', message='Senhas não conferem')])
    nome = StringField('Nome', validators=[DataRequired(message='Campo nome requerido'), Length(min=3, max=50, message='Número de caracteres do campo  deve estar entre 3 e 50')])
    data_nasc = DateField('Data de nascimento', validators=[DataRequired(message='Campo data de nascimento requerido')])
    comunidade = SelectField('Comunidade', validators=[DataRequired(message='Campo comunidade requerido')])
    coordenacao = RadioField('Você é coordenador?', validators=[InputRequired(message='Campo coordenação requerido')], choices=[('True', 'Sim'), ('False', 'Não')])
    submit = SubmitField('Cadastrar-se')


class FichaCatequistaForm(FlaskForm):
    title_form = "Ficha do catequista"
    nome_completo = StringField('Nome completo', validators=[DataRequired(message='Campo nome completo requerido'), Length(min=10, max=50, message='Número de caracteres do campo  deve estar entre 10 e 50')])
    data_nasc = DateField('Data de nascimento', validators=[DataRequired(message='Campo data de nascimento requerido')])
    ano_entrada = SelectField('Ano de entrada como catequista', validators=[DataRequired(message='Campo ano de entrada como catequista requerido')], choices=[(ano, ano) for ano in range(date.today().year, date.today().year-80, -1)])
    escolaridade = StringField('Ecolaridade', validators=[DataRequired(message='Campo escolaridade requerido'), Length(min=4, max=50, message='Número de caracteres do campo  deve estar entre 4 e 50')])
    telefone = TelField('Nº telefone/celular', validators=[Length(min=8, max=20, message='Número de caracteres do campo  deve estar entre 8 e 20')])
    whatsapp = StringField('Nº WhatsApp', validators=[Length(min=8, max=20, message='Número de caracteres do campo  deve estar entre 8 e 20')])
    logradouro = StringField('Rua/Avenida', validators=[DataRequired(message='Campo rua/avenida requerido'), Length(min=8, max=60, message='Número de caracteres do campo  deve estar entre 8 e 60')])
    bairro = StringField('Bairro', validators=[DataRequired(message='Campo bairro requerido'), Length(min=4, max=30, message='Número de caracteres do campo  deve estar entre 4 e 30')])
    cidade = StringField('Cidade', validators=[DataRequired(message='Campo cidade requerido'), Length(min=4, max=30, message='Número de caracteres do campo  deve estar entre 4 e 30')])
    estado = StringField('Estado', validators=[DataRequired(message='Campo estado requerido'), Length(min=4, max=20, message='Número de caracteres do campo  deve estar entre 4 e 20')])
    numero_casa = StringField('Nº casa/Complemento', validators=[DataRequired(message='Campo número da casa requerido'), Length(min=1, max=15, message='Número de caracteres do campo  deve estar entre 1 e 15')])
    ponto_referencia = StringField('Ponto de referência', validators=[DataRequired(message='Campo ponto de referência requerido'), Length(min=0, max=150, message='Número de caracteres do campo  deve estar entre 0 e 150')])
    crismado = RadioField('É crismado?', choices=[('Sim', 'Sim'), ('Não', 'Não')], validators=[DataRequired(message='Campo crismado requerido')])
    submit = SubmitField('Cadastrar')


class EditarFichaCatequistaForm(FlaskForm):
    title_form = "Editar ficha do catequista"
    nome_completo = StringField('Nome completo', validators=[DataRequired(message='Campo nome completo requerido'), Length(min=10, max=50, message='Número de caracteres do campo  deve estar entre 10 e 50')])
    escolaridade = StringField('Ecolaridade', validators=[DataRequired(message='Campo escolaridade requerido'), Length(min=4, max=50, message='Número de caracteres do campo  deve estar entre 4 e 50')])
    telefone = TelField('Número de telefone/celular', validators=[Length(min=8, max=20, message='Número de caracteres do campo  deve estar entre 8 e 20')])
    whatsapp = StringField('Número do WhatsApp', validators=[Length(min=8, max=20, message='Número de caracteres do campo  deve estar entre 8 e 20')])
    logradouro = StringField('Rua/Avenida', validators=[DataRequired(message='Campo rua/avenida requerido'), Length(min=8, max=60, message='Número de caracteres do campo  deve estar entre 8 e 60')])
    bairro = StringField('Bairro', validators=[DataRequired(message='Campo bairro requerido'), Length(min=4, max=30, message='Número de caracteres do campo  deve estar entre 4 e 30')])
    cidade = StringField('Cidade', validators=[DataRequired(message='Campo cidade requerido'), Length(min=4, max=30, message='Número de caracteres do campo  deve estar entre 4 e 30')])
    estado = StringField('Estado', validators=[DataRequired(message='Campo estado requerido'), Length(min=4, max=20, message='Número de caracteres do campo  deve estar entre 4 e 20')])
    numero_casa = StringField('Número da casa', validators=[DataRequired(message='Campo número da casa requerido'), Length(min=1, max=15, message='Número de caracteres do campo  deve estar entre 1 e 15')])
    ponto_referencia = StringField('Ponto de referência', validators=[DataRequired(message='Campo ponto de referência requerido'), Length(min=0, max=150, message='Número de caracteres do campo  deve estar entre 0 e 150')])
    crismado = RadioField('É crismado?', choices=[('Sim', 'Sim'), ('Não', 'Não')], validators=[DataRequired(message='Campo crismado requerido')])
    submit = SubmitField('Salvar')


class CodigoTurmaForm(FlaskForm):
    title_form = "Código da Turma"
    codigo = StringField(validators=[DataRequired(message='Campo código requerido'), Length(min=6, max=6, message='Número de caracteres do campo código deve ser 6')])
    submit = SubmitField('Enviar')


class CatequizandoForm(FlaskForm):
    title_form = "Cadastro catequizando"
    username = StringField('Nome de usuário', validators=[DataRequired(message='Campo nome de usuário requerido'), Length(min=4, max=20, message='Número de caracteres do campo  deve estar entre 4 e 20')])
    senha = PasswordField('Senha', validators=[DataRequired(message='Campo senha requerido'), Length(min=6, max=30, message='Número de caracteres do campo  deve estar entre 6 e 30')])
    confirma_senha = PasswordField('Confirma senha', validators=[DataRequired(message='Campo confirma senha requerido'), EqualTo('senha', message='Senhas não conferem')])
    nome = StringField('Nome', validators=[DataRequired(message='Campo nome requerido'), Length(min=3, max=50, message='Número de caracteres do campo  deve estar entre 3 e 50')])
    data_nasc = DateField('Data de nascimento', validators=[DataRequired(message='Campo data de nascimento requerido')])
    submit = SubmitField('Cadastrar-se')


class TurmaForm(FlaskForm):
    title_form = "Cadastro turma"
    nome = StringField('Nome da turma', validators=[DataRequired(message='Campo nome da turma requerido'), Length(min=1, max=100, message='Número de caracteres do campo  deve estar entre 1 e 100')])
    ano = SelectField('Ano de início', coerce=int, validators=[DataRequired(message='Campo ano de início requerido')], choices=[(ano, ano) for ano in range(date.today().year+1, date.today().year-20, -1)])
    tipo = SelectField('Tipo de catequese', coerce=int, validators=[DataRequired(message='Campo tipo de catequese requerido')])
    submit = SubmitField('Cadastrar')


class EditarTurmaForm(FlaskForm):
    title_form = "Editar turma"
    nome = StringField('Nome da turma', validators=[DataRequired(message='Campo nome da turma requerido'), Length(min=1, max=100, message='Número de caracteres do campo  deve estar entre  e ')])
    ano = SelectField('Ano de início', validators=[DataRequired(message='Campo ano de início requerido')], choices=[(ano, ano) for ano in range(date.today().year+1, date.today().year-20, -1)])
    tipo = SelectField('Tipo de catequese', coerce=str, validators=[DataRequired(message='Campo tipo de catequese requerido')])
    submit = SubmitField('Salvar')


class FichaCatequizandoForm(FlaskForm):
    title_form = "Cadastro ficha do catequizando"
    nome_completo = StringField('Nome completo', validators=[DataRequired(message='Campo nome completo requerido'), Length(min=10, max=50, message='Número de caracteres do campo  deve estar entre 10 e 50')])
    data_nasc = DateField('Data de nascimento', validators=[DataRequired(message='Campo data de nascimento requerido')])
    nome_mae = StringField('Nome da mãe', validators=[DataRequired(message='Campo nome da mãe requerido')])
    nome_pai = StringField('Nome da pai', validators=[DataRequired(message='Campo nome do pai requerido')])
    batizado = RadioField('É batizado?', choices=[('Sim', 'Sim'), ('Não', 'Não')], validators=[DataRequired(message='Campo batizado requerido')])
    eucaristia = RadioField('Já fez a primeira eucaristia?', choices=[('Sim', 'Sim'), ('Não', 'Não')], validators=[DataRequired(message='Campo eucaristia requerido')])
    escolaridade = StringField('Escolaridade', validators=[DataRequired(message='Campo escolaridade requerido'), Length(min=1, max=20, message='Número de caracteres do campo  deve estar entre 1 e 20')])
    logradouro = StringField('Rua/Avenida', validators=[DataRequired(message='Campo rua/avenida requerido'), Length(min=8, max=60, message='Número de caracteres do campo  deve estar entre 8 e 60')])
    bairro = StringField('Bairro', validators=[DataRequired(message='Campo bairro requerido'), Length(min=4, max=30, message='Número de caracteres do campo  deve estar entre 4 e 30')])
    cidade = StringField('Cidade', validators=[DataRequired(message='Campo cidade requerido'), Length(min=4, max=30, message='Número de caracteres do campo  deve estar entre 4 e 30')])
    estado = StringField('Estado', validators=[DataRequired(message='Campo estado requerido'), Length(min=4, max=20, message='Número de caracteres do campo  deve estar entre 4 e 20')])
    numero_casa = StringField('Número da casa', validators=[DataRequired(message='Campo número da casa requerido'), Length(min=1, max=15, message='Número de caracteres do campo  deve estar entre 1 e 15')])
    ponto_referencia = StringField('Ponto de referência', validators=[DataRequired(message='Campo ponto de referência requerido'), Length(min=0, max=150, message='Número de caracteres do campo  deve estar entre 0 e 150')])
    telefone = StringField('Número de telefone/celular', validators=[DataRequired(message='Campo telefone/celular requerido'), Length(min=8, max=20, message='Número de caracteres do campo  deve estar entre 8 e 20')])
    whatsapp = StringField('Número do WhatsApp', validators=[DataRequired(message='Campo whatsapp requerido'), Length(min=8, max=20, message='Número de caracteres do campo  deve estar entre 8 e 20')])
    data_inscricao = DateField('Data de inscrição', validators=[DataRequired(message='Campo data de inscrição requerido')])
    submit = SubmitField('Cadastrar')


class EditarFichaCatequizandoForm(FlaskForm):
    title_form = "Editar ficha do catequizando"
    nome = StringField('Nome completo', validators=[DataRequired(message='Campo nome completo requerido'), Length(min=10, max=50, message='Número de caracteres do campo  deve estar entre 10 e 50')])
    data_nasc = DateField('Data de nascimento', validators=[DataRequired(message='Campo data de nascimento requerido')])
    nome_mae = StringField('Nome da mãe', validators=[DataRequired(message='Campo nome da mãe requerido')])
    nome_pai = StringField('Nome da pai', validators=[DataRequired(message='Campo nome do pai requerido')])
    batizado = RadioField('É batizado?', choices=[('Sim', 'Sim'), ('Não', 'Não')], validators=[DataRequired(message='Campo batizado requerido')])
    eucaristia = RadioField('Já fez a primeira eucaristia?', choices=[('Sim', 'Sim'), ('Não', 'Não')], validators=[DataRequired(message='Campo eucaristia requerido')])
    escolaridade = StringField('Escolaridade', validators=[DataRequired(message='Campo escolaridade requerido'), Length(min=1, max=20, message='Número de caracteres do campo  deve estar entre 1 e 20')])
    logradouro = StringField('Rua/Avenida', validators=[DataRequired(message='Campo rua/avenida requerido'), Length(min=8, max=60, message='Número de caracteres do campo  deve estar entre 8 e 60')])
    bairro = StringField('Bairro', validators=[DataRequired(message='Campo bairro requerido'), Length(min=4, max=30, message='Número de caracteres do campo  deve estar entre 4 e 30')])
    cidade = StringField('Cidade', validators=[DataRequired(message='Campo cidade requerido'), Length(min=4, max=30, message='Número de caracteres do campo  deve estar entre 4 e 30')])
    estado = StringField('Estado', validators=[DataRequired(message='Campo estado requerido'), Length(min=4, max=20, message='Número de caracteres do campo  deve estar entre 4 e 20')])
    numero_casa = StringField('Número da casa', validators=[DataRequired(message='Campo número da casa requerido'), Length(min=1, max=15, message='Número de caracteres do campo  deve estar entre 1 e 15')])
    ponto_referencia = StringField('Ponto de referência', validators=[DataRequired(message='Campo ponto de referência requerido'), Length(min=0, max=150, message='Número de caracteres do campo  deve estar entre 0 e 150')])
    telefone = StringField('Número de telefone/celular', validators=[DataRequired(message='Campo telefone/celular requerido'), Length(min=8, max=20, message='Número de caracteres do campo  deve estar entre 8 e 20')])
    whatsapp = StringField('Número do WhatsApp', validators=[DataRequired(message='Campo whatsapp requerido'), Length(min=8, max=20, message='Número de caracteres do campo  deve estar entre 8 e 20')])
    submit = SubmitField('Salvar')


class RoteiroForm(FlaskForm):
    title_form = "Adicionar roteiro"
    tipo = SelectField('Catequese', coerce=str)
    tema = StringField('Tema', validators=[DataRequired(message='Campo tema requerido'), Length(min=2, max=50, message='Número de caracteres do campo  deve estar entre 2 e 50')])
    ambiente = TextAreaField('Ambiente')
    acolhida = TextAreaField('Acolhida')
    oracao_inicial = TextAreaField('Oração Inicial')
    dinamica = TextAreaField('Dinâmica')
    motivacao = TextAreaField('Motivação ou Colocação do Tema')
    leituras = TextAreaField('Leituras')
    desenvolvimento = TextAreaField('Desenvolvimento')
    atividade = TextAreaField('Atividade')
    compromisso = TextAreaField('Compromisso')
    avisos = TextAreaField('Avisos')
    oracao_final = TextAreaField('Oração Final')
    observacoes = TextAreaField('Observações')
    publico = RadioField('Público ou Privado?', validators=[DataRequired(message='Campo público ou privado requerido')], coerce=str, choices=[('Público', 'Público'), ('Privado', 'Privado')])
    submit = SubmitField('Cadastrar')


class EditarRoteiroForm(FlaskForm):
    title_form = "Editar encontro"
    tema = StringField('Tema', validators=[DataRequired(message='Campo tema requerido'), Length(min=2, max=50, message='Número de caracteres do campo  deve estar entre 2 e 50')])
    tipo = SelectField('Catequese', coerce=str)
    ambiente = TextAreaField('Ambiente')
    acolhida = TextAreaField('Acolhida')
    oracao_inicial = TextAreaField('Oração Inicial')
    dinamica = TextAreaField('Dinâmica')
    motivacao = TextAreaField('Motivação ou Colocação do Tema')
    leituras = TextAreaField('Leituras')
    desenvolvimento = TextAreaField('Desenvolvimento')
    atividade = TextAreaField('Atividade')
    compromisso = TextAreaField('Compromisso')
    avisos = TextAreaField('Avisos')
    oracao_final = TextAreaField('Oração Final')
    observacoes = TextAreaField('Observações')
    publico = RadioField('Público ou Privado?', validators=[DataRequired(message='Campo público ou privado requerido')], coerce=str, choices=[('Público', 'Público'), ('Privado', 'Privado')])
    submit = SubmitField('Salvar')


class EncontroForm(FlaskForm):
    title_form = "Adicionar encontro"
    tema = StringField('Tema', validators=[DataRequired(message='Campo tema requerido'), Length(min=2, max=50, message='Número de caracteres do campo  deve estar entre 2 e 50')])
    data = DateField('Data', validators=[DataRequired(message='Campo data do encontro requerido')])
    numero = IntegerField('Número')
    leitura = TextAreaField('Leitura(s)')
    atividade = TextAreaField('Atividade')
    compromisso = TextAreaField('Compromisso')
    avisos = TextAreaField('Avisos')
    submit = SubmitField('Cadastrar')


class EditarEncontroForm(FlaskForm):
    title_form = "Editar encontro"
    tema = StringField('Tema', validators=[DataRequired(message='Campo tema requerido'), Length(min=2, max=50, message='Número de caracteres do campo  deve estar entre 2 e 50')])
    data = DateField('Data do encontro', validators=[DataRequired(message='Campo data do encontro requerido')])
    numero = IntegerField('Número')
    leitura = TextAreaField('Leitura(s)')
    atividade = TextAreaField('Atividade')
    compromisso = TextAreaField('Compromisso')
    avisos = TextAreaField('Avisos')
    submit = SubmitField('Salvar')


class NotificacaoForm(FlaskForm):
    assunto = StringField('Assunto', validators=[DataRequired(message='Campo assunto requerido'), Length(min=1, max=50, message='Número de caracteres do campo  deve estar entre 1 e 50')])
    mensagem = TextAreaField('Mensagem', validators=[DataRequired(message='Campo mensagem requerido'), Length(min=5, max=250, message='Número de caracteres do campo  deve estar entre 5 e 250')])
    submit = SubmitField('Enviar notificação')


class FrequenciaForm(FlaskForm):
    presenca = RadioField('Situação', validators=[DataRequired('Campo situação requerido')], choices=[('Presente', 'Presente'), ('Ausente', 'Ausente')])


class LoginForm(FlaskForm):
    title_form = "Login"
    username = StringField('Nome de usuário', validators=[DataRequired(message='Campo nome de usuário requerido')])
    senha = PasswordField('Senha', validators=[DataRequired(message='Campo senha requerido')])
    submit = SubmitField('Login')


class TesteForm(FlaskForm):
    username = StringField('Nome de usuário', validators=[DataRequired(message='Campo nome de usuário requerido'), Length(min=4, max=20, message='Número de caracteres do campo  deve estar entre 4 e 20')])
    senha = PasswordField('Senha', validators=[DataRequired(message='Campo senha requerido')])
    nome = StringField('Nome', validators=[DataRequired(message='Campo nome requerido')])
    comunidade = SelectField('Comunidade')
    tipo1 = StringField('Tipo 1', validators=[DataRequired(message='Campo tipo 1 requerido')])
    tipo2 = StringField('Tipo 2')
    coordenacao = BooleanField('Você é coordenador?')
    presenca = RadioField('Situação', validators=[DataRequired('Campo situação requerido')], choices=[('Presente', 'Presente'), ('Ausente', 'Ausente')])
    enviar = SubmitField('Enviar')

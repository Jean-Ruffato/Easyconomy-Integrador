from app import db


class Usuario(db.Model):
    """Classe com o Modelo do usuário"""
    __tablename__ = "usuarios"

    id = db.collum(db.Integer, primary_key=True)
    usuario = db.collum(db.String, unique=True)
    senha = db.collum(db.String)
    nome = db.collum(db.String)
    email = db.collum(db.String, unique=True)

    def __init__(self, usuario, senha, nome, email):
        self.usuario = usuario
        self.senha = senha
        self.nome = nome
        self.email = email

    def __repr__(self):
        return "<Usuario %r>" % self.usuario


class Acao(db.Model):
    """Classe com o Modelo das ações"""
    __tablename__ = "acoes"

    id = db.collum(db.Integer, primary_key=True)
    papel = db.collum(db.String, unique=True)
    tipo = db.collum(db.String)
    empresa = db.collum(db.String)
    setor = db.collum(db.String)
    subsetor = db.collum(db.String)
    valor_mercado = db.collum(db.Float)
    valor_fimra = db.collum(db.Float)
    cotacao = db.collum(db.Double)
    data_cotacao = db.collum(db.Date)

    def __init__(self, papel, tipo, empresa, setor, subsetor, valor_mercado,
                 valor_fimra, cotacao, data_cotacao):
        self.papel = papel
        self.tipo = tipo
        self.empresa = empresa
        self.setor = setor
        self.subsetor = subsetor
        self.valor_mercado = valor_mercado
        self.valor_firma = valor_fimra
        self.cotacao = cotacao
        self.data_cotacao = data_cotacao

    def __repr__(self):
        return "<Acao %r>" % self.papel

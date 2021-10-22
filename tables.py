from app import db  

class User(db.Model): #primeira tabela
    __tablename__ = "users" #tabelas

    id = db.Column(db.Integer, primary_key = True) #cada usuario precisa de um id unico
    username = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String, unique = True)

    def __init__(self, username, password, name, email) #campos obrigatorios
        self.username = username #aqui eu tô associando o que eu vou receber nos campos
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self): #representation // pra poder mostrar os registros no banco de dados de uma forma mais organizada
        return "<user %r>" % self.username

class Post(db.Model): #segunda tabela
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) #to referenciando pra tabela de usuarios

    user = db.relationship('User', foreign_keys = user.id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
    
    def __repr__(self):
        return "<Post %r>" % self.id

class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship('User',foreign_keys = user.id)
    follower = db.relationship('User',foreign_keys = follower.id )

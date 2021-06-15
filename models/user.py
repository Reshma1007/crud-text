from models import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    title = db.Column(db.String(128))
    content = db.Column(db.String(98))

    def __init__(self, name, title, content):
        self.name = name
        self.title = title
        self.content = content


db.create_all()

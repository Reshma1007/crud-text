from models import db


class Feed(db.Model):
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

    @staticmethod
    def get_user(_id):
        users = Feed.query.get(_id)
        return users

    @staticmethod
    def get_all_users():
        users = Feed.query.all()
        return users

    @staticmethod
    def create_feed(
            name,
            title,
            content
    ):
        users = Feed(
            name=name,
            title=title,
            content=content
        )
        db.session.add(users)
        db.session.commit()

    @staticmethod
    def update_users(_id, name, title, content):
        users = Feed.query.get(_id)
        users.name = name
        users.title = title
        users.content = content
        db.session.add(users)
        db.session.commit()


    @staticmethod
    def del_user(_id):
        users = Feed.query.get_or_404(_id)
        db.session.delete(users)
        db.session.commit()

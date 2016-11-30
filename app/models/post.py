from app.services.database import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    body = db.Column(db.String(256))
    date_created = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    __tablename__ = 'posts'

    def __repr__(self):
        return '<Post %r>' % self.body
from news_blog import db


class News(db.Model):
    __tablename__ = 'game_news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    date = db.Column(db.Text)
    descr = db.Column(db.Text)
    image_link = db.Column(db.Text)
    article_link = db.Column(db.Text)

    def __repr__(self):
        return '<Entry id={id} title={title!r}>'.format(id=self.id, title=self.title)


def init():
    db.create_all()


from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    icon = db.Column(db.String(50), nullable=False)
    feeds = db.relationship('Feed', backref='animal', lazy=True)

    def __repr__(self):
        return f'<Animal {self.name}>'

class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feed_name = db.Column(db.String(50), nullable=False)
    preparation = db.Column(db.String(500), nullable=False)
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)

    def __repr__(self):
        return f'<Feed {self.name}>'

def create_tables():
    db.create_all()
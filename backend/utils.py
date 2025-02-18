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

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    farm_type = db.Column(db.String(50), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    size = db.Column(db.String(50), nullable=True)
    phone = db.Column(db.String(20), nullable=True)
    profile_image_url = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'farm_type': self.farm_type,
            'location': self.location,
            'size': self.size,
            'phone': self.phone,
            'profile_image_url': self.profile_image_url
        }
    
def create_tables():
    db.create_all()

    
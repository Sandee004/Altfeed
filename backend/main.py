import json
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

# Animal Model
class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    icon = db.Column(db.String(50), nullable=False)

    # One-to-many relationship with Feed
    feeds = db.relationship('Feed', backref='animal', lazy=True)

    def __repr__(self):
        return f'<Animal {self.name}>'

# Feed Model
class Feed(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    feed_name = db.Column(db.String(50), nullable=False)
    preparation = db.Column(db.String(500), nullable=False)

    # Foreign key for the Animal table
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)

    def __repr__(self):
        return f'<Feed {self.name}>'

# Sample data for animals
def animal_seed():
    # Insert animals into the database
    cattle = Animal(name="Cattle", icon="🐄")
    poultry = Animal(name="Poultry", icon="🐔")
    goat = Animal(name="Goat", icon="🐐")

    db.session.add_all([cattle, poultry, goat])  # Add all animals at once
    db.session.commit()

    print("Animals seeded successfully!")

# Sample batch insert for feeds
def feed_seed():
    # Collecting feed data for poultry as an example
    poultry = Animal.query.filter_by(name="Poultry").first()

    if not poultry:
        print("Poultry animal not found.")
        return

    feeds = [
        {
            "feed_name": "Poultry Starter",
            "preparation": json.dumps([
                "High-protein feed for chicks",
                "Feed 2-3 kg per day."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Poultry Grower",
            "preparation": json.dumps([
                "Feed for growing chickens",
                "Feed 3-4 kg per day."
            ]),
            "animal_id": poultry.id
        }
        # Add more feeds as needed
    ]
    
    # Insert all feeds at once
    db.session.bulk_insert_mappings(Feed, feeds)
    db.session.commit()

    print("Feeds seeded successfully!")

@app.route('/api/animals', methods=['GET'])
def get_animals():
    animals = Animal.query.all()  # Query all animals
    return jsonify([{"name": animal.name, "icon": animal.icon} for animal in animals])

# API route to get feeds for a specific animal
@app.route('/feeds/<animal>', methods=['GET'])
def get_feeds(animal):
    animal_obj = Animal.query.filter_by(name=animal.capitalize()).first()

    if animal_obj:
        feeds = Feed.query.filter_by(animal_id=animal_obj.id).all()
        return jsonify([{
            "name": feed.feed_name,
            "instructions": json.loads(feed.preparation)
        } for feed in feeds])
    else:
        return jsonify({"error": "Animal not found"}), 404


@app.route("/api/feeds/<animal>/<feed_name>", methods=["GET"])
def get_feed_details(animal, feed_name):
    animal_data = Animal.query.filter(db.func.lower(Animal.name) == animal.lower()).first()

    if not animal_data:
        return jsonify({"message": "Animal not found"}), 404

    formatted_feed_name = feed_name.replace("-", " ")

    feed = Feed.query.filter(
        db.func.lower(Feed.feed_name) == formatted_feed_name.lower(),
        Feed.animal_id == animal_data.id
    ).first()

    if feed:
        preparation_steps = json.loads(feed.preparation)

        return jsonify({
            "id": feed.id,
            "feed_name": feed.feed_name,
            "preparation": preparation_steps,
            "animal_id": feed.animal_id
        }), 200
    else:
        return jsonify({"message": "Feed not found"}), 404

# Function to seed the database with animals and feeds
def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()  # Create tables if they don't exist
        animal_seed()     # Seed animals
        feed_seed()       # Seed feeds

if __name__ == '__main__':
    seed_database()  # Seed the database when starting the app
    app.run(debug=True)

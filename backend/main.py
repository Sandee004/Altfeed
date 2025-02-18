from flask import Flask, jsonify
from flask_cors import CORS
from utils import db, create_tables, Animal, Feed
from animals_seed import seed_animals
from feed_cattle_seed import feed_cattle_seed
from feed_poultry_seed import feed_poultry_seed
from feed_goat_seed import feed_goat_seed
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)  # Initialize the db with the app
CORS(app)



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


def seed_database():
    with app.app_context():
        db.drop_all()
        create_tables()
        seed_animals()
        feed_cattle_seed()
        feed_poultry_seed()
        feed_goat_seed()

if __name__ == '__main__':
    seed_database()
    app.run(debug=True)

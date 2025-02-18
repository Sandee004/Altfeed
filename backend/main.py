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

    db.session.add_all([cattle, poultry, goat])
    db.session.commit()

    print("Animals seeded successfully!")


def feed_cattle_seed():
    cattle = Animal.query.filter_by(name="Cattle").first()

    if not cattle:
        print("Cattle animal not found.")
        return

    cattle_feeds = [
        {
            "feed_name": "Moringa Leaves",
            "preparation": json.dumps([
                "Collect fresh Moringa leaves.",
                "Dry the leaves under shade to retain nutrients.",
                "Grind the dried leaves into powder.",
                "Store in an airtight container."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Cassava Peels",
            "preparation": json.dumps([
                "Collect fresh cassava peels.",
                "Wash thoroughly to remove dirt and toxins.",
                "Sun-dry the peels for 2-3 days.",
                "Grind the dried peels into powder.",
                "Mix with other feeds for balanced nutrition."
            ]),
            "animal_id": cattle.id
        }, 
        {
            "feed_name": "Brewers Grains",
            "preparation": json.dumps([
                "Obtain fresh brewers grains from a brewery.",
                "Ensure the grains are free from mold.",
                "Mix with regular feed for cattle.",
                "Feed immediately or store in a cool place."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Banana Peels",
            "preparation": json.dumps([
                "Collect ripe banana peels.",
                "Wash thoroughly to remove dirt and residues.",
                "Sun-dry for 2-3 days until fully dry.",
                "Grind into powder or chop into small pieces.",
                "Mix with other feed ingredients."
            ]),
            "animal_id": cattle.id
        },
        # ... (Rest of your feed data in the same dictionary format)
        {
            "feed_name": "Pineapple Waste",
            "preparation": json.dumps([
                "Collect pineapple peels and cores.",
                "Dry under the sun until moisture is removed.",
                "Chop into small pieces or grind into powder.",
                "Mix with other cattle feeds."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Sugarcane Tops",
            "preparation": json.dumps([
                "Harvest fresh sugarcane tops.",
                "Chop into small pieces for easy consumption.",
                "Can be fed fresh or slightly wilted."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Sweet Potato Vines",
            "preparation": json.dumps([
                "Collect fresh sweet potato vines.",
                "Sun-dry for 2-3 days.",
                "Chop into smaller pieces.",
                "Mix with other feed components."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Coconut Husk and Shell Residue",
            "preparation": json.dumps([
                "Obtain husks and shell residues from coconut processing.",
                "Sun-dry thoroughly.",
                "Grind into powder.",
                "Mix with molasses for better palatability."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Palm Kernel Cake",
            "preparation": json.dumps([
                "Obtain by-product from palm oil extraction.",
                "Can be fed directly or mixed with other feeds.",
                "Ensure no mold contamination before feeding."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Cassava Leaves",
            "preparation": json.dumps([
                "Harvest young cassava leaves.",
                "Sun-dry to reduce cyanide content.",
                "Crush into powder or chop finely.",
                "Mix with other forages or concentrate feeds."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Groundnut Haulms",
            "preparation": json.dumps([
                "Collect leftover stems and leaves from groundnut harvest.",
                "Sun-dry to preserve nutrients.",
                "Chop into smaller pieces.",
                "Mix with other roughages or concentrates."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Water Hyacinth",
            "preparation": json.dumps([
                "Harvest water hyacinth from water bodies.",
                "Wash to remove contaminants.",
                "Sun-dry or wilt for 1-2 days.",
                "Chop finely and mix with other feeds."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Neem Leaves",
            "preparation": json.dumps([
                "Collect fresh neem leaves.",
                "Dry in shade to retain medicinal properties.",
                "Crush into powder or chop into small pieces.",
                "Mix in small quantities with other feeds."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Jackfruit Waste",
            "preparation": json.dumps([
                "Collect peels and seeds from jackfruit processing.",
                "Sun-dry thoroughly.",
                "Grind seeds into powder.",
                "Chop peels into small pieces.",
                "Mix with other fibrous feeds."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Mango Seed Kernels",
            "preparation": json.dumps([
                "Extract kernels from mango seeds.",
                "Sun-dry to reduce moisture.",
                "Grind into powder.",
                "Mix with other feeds in limited quantities due to tannins."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Corn Cobs",
            "preparation": json.dumps([
                "Collect leftover corn cobs after grain extraction.",
                "Sun-dry completely.",
                "Grind into coarse powder.",
                "Mix with molasses or other feeds for better taste."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Sesame Seed Cake",
            "preparation": json.dumps([
                "Collect by-product from sesame oil extraction.",
                "Dry to prevent mold growth.",
                "Feed directly or mix with other concentrates."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Brewers Spent Grain",
            "preparation": json.dumps([
                "Obtain fresh brewers grains from breweries.",
                "Dry under shade or sun.",
                "Feed directly or mix with other roughages.",
                "Use immediately or store in a cool place."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Citrus Pulp",
            "preparation": json.dumps([
                "Collect pulp and peel waste from citrus processing.",
                "Sun-dry to reduce moisture.",
                "Grind into powder.",
                "Mix with other fibrous feeds to balance acidity."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Molasses",
            "preparation": json.dumps([
                "Obtain as a by-product from sugar processing.",
                "Dilute with water for easy mixing.",
                "Mix with fibrous feeds to improve palatability."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Tea Waste",
            "preparation": json.dumps([
                "Collect waste leaves from tea processing.",
                "Sun-dry to remove moisture.",
                "Chop into small pieces.",
                "Mix with other forage or concentrate feeds."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Papaya Peels and Leaves",
            "preparation": json.dumps([
                "Collect peels and young leaves.",
                "Sun-dry or feed fresh.",
                "Chop into small pieces.",
                "Mix with other roughages for balanced nutrition."
            ]),
            "animal_id": cattle.id
        },
        {
            "feed_name": "Shea Nut Cake",
            "preparation": json.dumps([
                "Obtain as a by-product from shea butter extraction.",
                "Sun-dry to prevent mold.",
                "Grind into powder.",
                "Mix with other protein sources."
            ]),
            "animal_id": cattle.id
        },
    ]

    db.session.bulk_insert_mappings(Feed, cattle_feeds)
    db.session.commit()
    print("Cattle feeds seeded successfully!")

def feed_poultry_seed():
    poultry = Animal.query.filter_by(name="Poultry").first()

    if not poultry:
        print("Poultry animal not found.")
        return
    
    poultry_feeds = [
        {
            "feed_name": "Black Soldier Fly Larvae (BSFL)",
            "preparation": json.dumps([
                "Collect larvae from compost or special farming units.",
                "Wash to remove dirt.",
                "Sun-dry or oven-dry to reduce moisture.",
                "Grind into powder or feed whole.",
                "Mix with other feeds for balanced nutrition."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Azolla",
            "preparation": json.dumps([
                "Cultivate Azolla in shallow water tanks.",
                "Harvest fresh daily.",
                "Wash thoroughly to remove contaminants.",
                "Sun-dry or feed fresh.",
                "Mix with other feeds or serve as a supplement."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Duckweed",
            "preparation": json.dumps([
                "Collect fresh duckweed from ponds or grow in water tanks.",
                "Wash to remove dirt and debris.",
                "Sun-dry or feed fresh.",
                "Chop into small pieces if needed.",
                "Mix with other poultry feeds."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Moringa Leaves",
            "preparation": json.dumps([
                "Harvest fresh Moringa leaves.",
                "Dry under shade to retain nutrients.",
                "Grind into powder.",
                "Mix with other feed ingredients.",
                "Store in airtight containers."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Termites",
            "preparation": json.dumps([
                "Collect termites using termite traps.",
                "Dry under the sun to reduce moisture.",
                "Grind into powder or feed whole.",
                "Mix with other protein-rich feeds."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Earthworms",
            "preparation": json.dumps([
                "Cultivate earthworms in compost bins.",
                "Harvest mature worms.",
                "Rinse with clean water.",
                "Sun-dry or feed live.",
                "Mix with other protein sources."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Coconut Residue",
            "preparation": json.dumps([
                "Obtain coconut residue after oil extraction.",
                "Sun-dry to remove moisture.",
                "Grind into powder.",
                "Mix with other energy-rich feeds."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Fish Waste",
            "preparation": json.dumps([
                "Collect fish scraps from markets or processing units.",
                "Boil to reduce bacteria.",
                "Sun-dry thoroughly.",
                "Grind into fish meal powder.",
                "Mix with other protein feeds."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Rice Bran",
            "preparation": json.dumps([
                "Collect rice bran from milling process.",
                "Sun-dry if moist.",
                "Mix directly with other feeds.",
                "Ensure it's fresh to avoid rancidity."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Maize Chaff",
            "preparation": json.dumps([
                "Collect chaff during maize processing.",
                "Sun-dry completely.",
                "Grind into powder.",
                "Mix with other carbohydrate feeds."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Pumpkin Seeds",
            "preparation": json.dumps([
                "Collect seeds from ripe pumpkins.",
                "Sun-dry to reduce moisture.",
                "Grind into powder or feed whole.",
                "Mix with other energy-rich feeds."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Shrimp Shells",
            "preparation": json.dumps([
                "Collect shells from shrimp processing.",
                "Sun-dry to prevent mold.",
                "Grind into fine powder.",
                "Mix with other calcium-rich feeds."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Banana Peels",
            "preparation": json.dumps([
                "Collect banana peels from ripe bananas.",
                "Sun-dry for 2-3 days.",
                "Grind into powder.",
                "Mix with other energy sources."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Sweet Potato Vines",
            "preparation": json.dumps([
                "Harvest fresh vines.",
                "Sun-dry to preserve nutrients.",
                "Chop into small pieces.",
                "Mix with other green feeds."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Amaranth Leaves",
            "preparation": json.dumps([
                "Collect fresh amaranth leaves.",
                "Wash thoroughly.",
                "Sun-dry or feed fresh.",
                "Chop finely for easy consumption.",
                "Mix with other greens."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Cassava Peels",
            "preparation": json.dumps([
                "Collect fresh cassava peels.",
                "Wash thoroughly to remove dirt and toxins.",
                "Sun-dry for 2-3 days.",
                "Grind into powder.",
                "Mix with other feeds for balanced nutrition."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Sesame Seed Cake",
            "preparation": json.dumps([
                "Obtain by-product from sesame oil extraction.",
                "Dry to prevent mold.",
                "Grind into powder.",
                "Mix with other protein-rich feeds."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Brewers Yeast",
            "preparation": json.dumps([
                "Collect from breweries as a by-product.",
                "Dry under shade.",
                "Mix with other feeds as a supplement.",
                "Store in a cool, dry place."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Watermelon Rinds",
            "preparation": json.dumps([
                "Collect leftover watermelon rinds.",
                "Sun-dry to reduce moisture.",
                "Chop into small pieces.",
                "Mix with other roughages."
            ]),
            "animal_id": poultry.id
        },
        {
            "feed_name": "Neem Leaves",
            "preparation": json.dumps([
                "Collect fresh neem leaves.",
                "Dry under shade to retain medicinal properties.",
                "Crush into powder.",
                "Feed in small quantities as an herbal supplement."
            ]),
            "animal_id": poultry.id
        },
    ]
    
    db.session.bulk_insert_mappings(Feed, poultry_feeds)
    db.session.commit()
    print("Poultry feeds seeded successfully!")

def feed_goat_seed():
    goat = Animal.query.filter_by(name="Goat").first()

    if not goat:
        print("Goat animal not found")
        return
    
    goat_feeds = [
    {
        "feed_name": "Moringa Leaves",
        "preparation": json.dumps([
            "Collect fresh Moringa leaves.",
            "Dry the leaves under shade to retain nutrients.",
            "Grind the dried leaves into powder.",
            "Store in an airtight container."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Banana Peels",
        "preparation": json.dumps([
            "Collect banana peels and wash them thoroughly.",
            "Chop the peels into small pieces.",
            "Sun-dry until fully dehydrated.",
            "Store in a dry place or grind into powder."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Cassava Leaves",
        "preparation": json.dumps([
            "Harvest fresh cassava leaves.",
            "Wilt the leaves for 24 hours to reduce cyanide content.",
            "Chop the leaves into small pieces.",
            "Sun-dry and store in a cool, dry place."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Sweet Potato Vines",
        "preparation": json.dumps([
            "Collect fresh sweet potato vines.",
            "Wash to remove soil and contaminants.",
            "Chop into small pieces.",
            "Sun-dry to preserve for off-season feeding."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Pineapple Peels",
        "preparation": json.dumps([
            "Collect pineapple peels and wash thoroughly.",
            "Chop into small pieces.",
            "Sun-dry to prevent spoilage.",
            "Store in a cool, dry place."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Breadfruit Peels",
        "preparation": json.dumps([
            "Collect breadfruit peels after fruit processing.",
            "Chop into small pieces for easy drying.",
            "Sun-dry completely to avoid mold.",
            "Store in an airtight container."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Coconut Husks",
        "preparation": json.dumps([
            "Collect coconut husks and clean them.",
            "Grind into coarse fiber.",
            "Mix with other roughages to improve palatability."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Jackfruit Peels",
        "preparation": json.dumps([
            "Collect jackfruit peels and remove the sticky latex.",
            "Chop into small pieces.",
            "Sun-dry or feed fresh in moderation."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Papaya Leaves",
        "preparation": json.dumps([
            "Harvest mature papaya leaves.",
            "Chop into small pieces.",
            "Sun-dry or feed fresh as a supplement."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Watermelon Rinds",
        "preparation": json.dumps([
            "Collect watermelon rinds and wash thoroughly.",
            "Chop into small, chewable pieces.",
            "Feed fresh or sun-dry for later use."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Coffee Pulp",
        "preparation": json.dumps([
            "Collect coffee pulp after bean extraction.",
            "Sun-dry to reduce moisture content.",
            "Mix with other feeds to balance nutrient profile."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Orange Peels",
        "preparation": json.dumps([
            "Collect orange peels and wash thoroughly.",
            "Sun-dry to reduce moisture and bitterness.",
            "Grind into powder or chop for roughage."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Mango Seed Kernels",
        "preparation": json.dumps([
            "Extract kernels from mango seeds.",
            "Sun-dry to reduce moisture content.",
            "Grind into powder and mix with other feeds."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Avocado Leaves",
        "preparation": json.dumps([
            "Collect mature avocado leaves.",
            "Chop into small pieces.",
            "Sun-dry or feed fresh in controlled quantities."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Guava Leaves",
        "preparation": json.dumps([
            "Harvest fresh guava leaves.",
            "Chop into small pieces.",
            "Sun-dry to preserve for future use."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Pumpkin Leaves",
        "preparation": json.dumps([
            "Collect young pumpkin leaves.",
            "Chop into small pieces.",
            "Sun-dry or feed fresh as a nutritious supplement."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Cabbage Waste",
        "preparation": json.dumps([
            "Collect outer leaves and trimmings from cabbage.",
            "Chop into small pieces.",
            "Sun-dry to prevent spoilage."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Groundnut Haulms",
        "preparation": json.dumps([
            "Collect leftover groundnut vines after harvesting.",
            "Sun-dry to reduce moisture.",
            "Store in a dry place for off-season feeding."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Sesame Leaves",
        "preparation": json.dumps([
            "Harvest sesame leaves after seed collection.",
            "Sun-dry to reduce moisture content.",
            "Store in a cool, dry place for later use."
        ]),
        "animal_id": goat.id
    },
    {
        "feed_name": "Cactus Pads (Nopal)",
        "preparation": json.dumps([
            "Harvest cactus pads and remove spines.",
            "Chop into small, chewable pieces.",
            "Feed fresh or sun-dry for preservation."
        ]),
        "animal_id": goat.id
    },
    ]

    db.session.bulk_insert_mappings(Feed, goat_feeds)
    db.session.commit()
    print("Goat feeds seeded successfully!")

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
        feed_cattle_seed() 
        feed_poultry_seed()      # Seed feeds
        feed_goat_seed()

if __name__ == '__main__':
    seed_database()  # Seed the database when starting the app
    app.run(debug=True)

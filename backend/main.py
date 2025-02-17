from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample data for animals and their icons
animals_data = [
    {"name": "Cattle", "icon": "🐄"},
    {"name": "Poultry", "icon": "🐔"},
    {"name": "Pigs", "icon": "🐖"},

    {"name": "Goats", "icon": "🐐"},
]

@app.route('/api/animals', methods=['GET'])
def get_animals():
    print("Request received")
    return jsonify(animals_data)

# Existing feeds endpoint
feeds_data = {
    "cattle": [
        {"name": "Moringa Leaves", "icon": "🍃"},
        {"name": "Cassava Peels", "icon": "🥔"},
        {"name": "Brewers Grains", "icon": "🍺"}
    ],
    "poultry": [
        {"name": "Black Soldier Fly Larvae", "icon": "🐛"},
        {"name": "Azolla", "icon": "🌿"},
        {"name": "Duckweed", "icon": "🌱"}
    ],
}

@app.route('/feeds/<animal>', methods=['GET'])
def get_feeds(animal):
    print("Request received for", animal)
    animal = animal.lower()
    if animal in feeds_data:
        return jsonify(feeds_data[animal])
    else:
        return jsonify([])

# Sample data for feed details
feed_details = {
    "moringa-leaves": {
        "name": "Moringa Leaves",
        "description": "Moringa leaves are highly nutritious and can be used as a protein supplement for livestock.",
        "instructions": [
            "Harvest fresh moringa leaves",
            "Dry the leaves in a shaded area for 3-4 days",
            "Grind the dried leaves into a powder",
            "Mix 10-20% of moringa leaf powder with regular feed",
        ],
    },
    "cassava-peels": {
        "name": "Cassava Peels",
        "description": "Cassava peels are a good energy source for livestock and should be properly processed before feeding.",
        "instructions": [
            "Collect fresh cassava peels",
            "Sun-dry them for 3-5 days",
            "Chop or grind into smaller pieces",
            "Mix with other feed components",
        ],
    },
}

@app.route('/<animal>/<feedname>', methods=['GET'])
def get_feed_details(animal, feedname):
    # Normalize input for better matching
    feedname = feedname.lower()
    feed = feed_details.get(feedname)
    
    if feed:
        return jsonify(feed)
    else:
        return jsonify({"error": "Feed not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)

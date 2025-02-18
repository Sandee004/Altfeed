import json
from utils import db, Animal, Feed

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

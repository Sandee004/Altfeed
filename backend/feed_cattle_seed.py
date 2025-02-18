import json
from utils import db, Animal, Feed

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

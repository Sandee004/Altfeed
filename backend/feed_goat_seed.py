import json
from utils import db, Animal, Feed

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

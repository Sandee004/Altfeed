from utils import db, Animal

def seed_animals():
    cattle = Animal(name="Cattle", icon="🐄")
    poultry = Animal(name="Poultry", icon="🐔")
    goat = Animal(name="Goat", icon="🐐")

    db.session.add_all([cattle, poultry, goat])
    db.session.commit()

    print("Animals seeded successfully!")
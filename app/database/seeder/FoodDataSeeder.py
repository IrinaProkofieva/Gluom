from lib2to3.pytree import Base

from flask_seeder import FlaskSeeder


# SQLAlchemy database model
class FoodData(Base):
    def __init__(self, id, food, protein, fat, carbohydrate, kcal):
        self.id = id
        self.food = food
        self.protein = protein,
        self.fat = fat,
        self.carbohydrate = carbohydrate,
        self.kcal = kcal


class FoodDataSeeder(FlaskSeeder):

    def run(self):
        print("Start seeding db")
        with open("app/database/seeder/products.txt") as f:
            id = 0
            for line in f.readlines():
                data = line.split(',')
                new_data = FoodData(
                    id = id,
                    food=data[0],
                    protein=data[1],
                    fat=data[2],
                    carbohydrate=data[3],
                    kcal=data[4]
                )
                self.db.session.add(new_data)
                print("Added " + data[0])
                id += 1
            self.db.session.commit()  # Commits all changes
            print("Seeding ends")

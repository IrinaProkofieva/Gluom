from app import db
import json


class FoodData(db.Model):
    """Model for foodData."""

    __tablename__ = 'foodData'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    food = db.Column(db.String(250, collation="C.UTF-8"),
                     index=True,
                     nullable=False)
    kcal = db.Column(db.Double)
    protein = db.Column(db.Double)
    fat = db.Column(db.Double)
    carbohydrate = db.Column(db.Double)

    def __repr__(self):
        return '<Food data {}, {} kcal, {} prots, {} fats, {} carbs>'.format(self.food,
                                                                             self.kcal,
                                                                             self.protein,
                                                                             self.fat,
                                                                             self.carbohydrate)

    def toJson(self):
        obj = {
            'name': self.food,
            'kcal': self.kcal,
            'protein': self.protein,
            'fat': self.fat,
            'carbohydrate': self.carbohydrate
        }
        return obj

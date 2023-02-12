import asyncio

from flask import current_app as app, Response, request

from .database.models.foodData import FoodData
from . import db


@app.route('/', methods=['GET'])
def hello_world():
    return {
        'hello': 'world'
    }


@app.route('/ping', methods=['GET'])
def ping():
    return '200;Ok'


@app.route('/api/list', methods=['GET'])
def get_all():
    return list(map(lambda x: x.toJson(), FoodData.query.all()))


@app.get("/api/search")
def search():
    args = request.args
    foodName = args.get('text').lower()
    search_request = "%{}%".format(foodName)
    result = FoodData.query.filter(FoodData.food.ilike(search_request)).all()
    return list(map(lambda x: x.toJson(), result))


@app.post("/api/seed")
def seed():
    seed_db()
    return Response(
        mimetype='application/json',
        status=200
    )


def seed_db():
    FoodData.query.delete()
    print("Start seeding db")
    with open("app/database/seeder/products.txt") as f:
        id = 0
        for line in f.readlines():
            data = line.split(',')
            new_data = FoodData(
                id=id,
                food=data[0],
                protein=data[1],
                fat=data[2],
                carbohydrate=data[3],
                kcal=data[4]
            )
            db.session.add(new_data)
            print("Added " + data[0])
            id += 1
        db.session.commit()  # Commits all changes
        print("Seeding ends")

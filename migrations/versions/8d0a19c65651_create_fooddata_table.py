"""create foodData table

Revision ID: 8d0a19c65651
Revises: 
Create Date: 2023-02-05 16:19:57.224576

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
from app import db
from app.database.models.foodData import FoodData

revision = '8d0a19c65651'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # op.create_table(
    #     'foodData',
    #     sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
    #     sa.Column('food', sa.String(250, collation="C.UTF-8"), nullable=False),
    #     sa.Column('kcal', sa.Double),
    #     sa.Column('protein', sa.Double),
    #     sa.Column('fat', sa.Double),
    #     sa.Column('carbohydrate', sa.Double)
    # )

    db.create_all()

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



def downgrade():
    op.drop_table('foodData')

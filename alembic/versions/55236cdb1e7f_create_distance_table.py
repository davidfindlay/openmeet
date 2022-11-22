"""create distance table

Revision ID: 55236cdb1e7f
Revises: 0d79c9663ad3
Create Date: 2022-11-13 21:55:20.240063

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey


# revision identifiers, used by Alembic.
revision = '55236cdb1e7f'
down_revision = '0d79c9663ad3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    distance_table = op.create_table(
        'distance',
        Column('distance_id', Integer, primary_key=True),
        Column('qty', Float, nullable=False),
        Column('splits', Float, nullable=True),
        Column('unit_id', Integer, ForeignKey('unit.unit_id'), nullable=False),
        Column('course_id', Integer, ForeignKey('course.course_id'), nullable=True),
        Column('title', String(40), nullable=False)
    )

    op.bulk_insert(distance_table,
                   [
                       {'qty': 25,
                        'splits': 1,
                        'unit_id': 1,
                        'course_id': 2,
                        'title': '25m SC'},
                       {'qty': 50,
                        'splits': 2,
                        'unit_id': 1,
                        'course_id': 2,
                        'title': '50m SC'},
                       {'qty': 100,
                        'splits': 4,
                        'unit_id': 1,
                        'course_id': 2,
                        'title': '100m SC'},
                       {'qty': 200,
                        'splits': 8,
                        'unit_id': 1,
                        'course_id': 2,
                        'title': '200m SC'},
                       {'qty': 400,
                        'splits': 16,
                        'unit_id': 1,
                        'course_id': 2,
                        'title': '400m SC'},
                       {'qty': 800,
                        'splits': 32,
                        'unit_id': 1,
                        'course_id': 2,
                        'title': '800m SC'},
                       {'qty': 1500,
                        'splits': 60,
                        'unit_id': 1,
                        'course_id': 2,
                        'title': '1500m SC'},
                       {'qty': 50,
                        'splits': 2,
                        'unit_id': 1,
                        'course_id': 1,
                        'title': '50m LC'},
                       {'qty': 100,
                        'splits': 4,
                        'unit_id': 1,
                        'course_id': 1,
                        'title': '100m LC'},
                       {'qty': 200,
                        'splits': 8,
                        'unit_id': 1,
                        'course_id': 1,
                        'title': '200m LC'},
                       {'qty': 400,
                        'splits': 16,
                        'unit_id': 1,
                        'course_id': 1,
                        'title': '400m LC'},
                       {'qty': 800,
                        'splits': 32,
                        'unit_id': 1,
                        'course_id': 1,
                        'title': '800m LC'},
                       {'qty': 1500,
                        'splits': 30,
                        'unit_id': 1,
                        'course_id': 1,
                        'title': '1500m LC'}
                   ]
                   )


def downgrade() -> None:
    op.drop_table('distance')

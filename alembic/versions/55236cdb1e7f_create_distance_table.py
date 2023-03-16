"""create distance table

Revision ID: 55236cdb1e7f
Revises: 48ffa49ac36b

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey

# revision identifiers, used by Alembic.
revision = '55236cdb1e7f'
down_revision = '48ffa49ac36b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    distance_table = op.create_table(
        'distance',
        Column('distance_code', String(10), primary_key=True),
        Column('qty', Float, nullable=False),
        Column('splits', Float, nullable=True),
        Column('unit_code', Integer, ForeignKey('unit.unit_code'), nullable=False),
        Column('course_code', Integer, ForeignKey('course.course_code'), nullable=True),
        Column('title', String(40), nullable=False)
    )

    op.bulk_insert(distance_table,
                   [
                       {'distance_code': 'SC25M',
                        'qty': 25,
                        'splits': 1,
                        'unit_code': 'm',
                        'course_code': 'SCM',
                        'title': '25m SC'},
                       {'distance_code': 'SC50M',
                        'qty': 50,
                        'splits': 2,
                        'unit_code': 'm',
                        'course_code': 'SCM',
                        'title': '50m SC'},
                       {'distance_code': 'SC100M',
                        'qty': 100,
                        'splits': 4,
                        'unit_code': 'm',
                        'course_code': 'SCM',
                        'title': '100m SC'},
                       {'distance_code': 'SC200M',
                        'qty': 200,
                        'splits': 8,
                        'unit_code': 'm',
                        'course_code': 'SCM',
                        'title': '200m SC'},
                       {'distance_code': 'SC400M',
                        'qty': 400,
                        'splits': 16,
                        'unit_code': 'm',
                        'course_code': 'SCM',
                        'title': '400m SC'},
                       {'distance_code': 'SC800M',
                        'qty': 800,
                        'splits': 32,
                        'unit_code': 'm',
                        'course_code': 'SCM',
                        'title': '800m SC'},
                       {'distance_code': 'SC1500M',
                        'qty': 1500,
                        'splits': 60,
                        'unit_code': 'm',
                        'course_code': 'SCM',
                        'title': '1500m SC'},
                       {'distance_code': 'LC50M',
                        'qty': 50,
                        'splits': 2,
                        'unit_code': 'm',
                        'course_code': 'LCM',
                        'title': '50m LC'},
                       {'distance_code': 'LC100M',
                        'qty': 100,
                        'splits': 4,
                        'unit_code': 'm',
                        'course_code': 'LCM',
                        'title': '100m LC'},
                       {'distance_code': 'LC200M',
                        'qty': 200,
                        'splits': 8,
                        'unit_code': 'm',
                        'course_code': 'LCM',
                        'title': '200m LC'},
                       {'distance_code': 'LC400M',
                        'qty': 400,
                        'splits': 16,
                        'unit_code': 'm',
                        'course_code': 'LCM',
                        'title': '400m LC'},
                       {'distance_code': 'LC800M',
                        'qty': 800,
                        'splits': 32,
                        'unit_code': 'm',
                        'course_code': 'LCM',
                        'title': '800m LC'},
                       {'distance_code': 'LC1500M',
                        'qty': 1500,
                        'splits': 30,
                        'unit_code': 'm',
                        'course_code': 'LCM',
                        'title': '1500m LC'}
                   ]
                   )


def downgrade() -> None:
    op.drop_table('distance')

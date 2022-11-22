"""create unit table

Revision ID: 0d79c9663ad3
Revises: 6d82fa334b00
Create Date: 2022-11-13 21:52:31.266685

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey

# revision identifiers, used by Alembic.
revision = '0d79c9663ad3'
down_revision = '6d82fa334b00'
branch_labels = None
depends_on = None


def upgrade() -> None:
    unit_table = op.create_table(
        'unit',
        Column('unit_id', Integer, primary_key=True, autoincrement=True),
        Column('unit_name', String(50), nullable=False),
        Column('abbreviation', String(10), nullable=False),
    )

    op.bulk_insert(unit_table,
                   [{'unit_name': 'metre',
                     'abbreviation': 'm'},
                    {'unit_name': 'yard',
                     'abbreviation': 'yd'},
                    {'unit_name': 'feet',
                     'abbreviation': 'ft'}]
                   )


def downgrade() -> None:
    op.drop_table('unit')

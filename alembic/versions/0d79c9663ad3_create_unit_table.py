"""create unit table

Revision ID: 0d79c9663ad3
Revises: 85cfe8a5be4c

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey

# revision identifiers, used by Alembic.
revision = '0d79c9663ad3'
down_revision = '85cfe8a5be4c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    unit_table = op.create_table(
        'unit',
        Column('unit_code', String(10), primary_key=True),
        Column('unit_name', String(50), nullable=False),
        Column('abbreviation', String(10), nullable=False),
    )

    op.bulk_insert(unit_table,
                   [{'unit_code': 'm',
                     'unit_name': 'metre',
                     'abbreviation': 'm'},
                    {'unit_code': 'yd',
                     'unit_name': 'yard',
                     'abbreviation': 'yd'},
                    {'unit_code': 'ft',
                     'unit_name': 'feet',
                     'abbreviation': 'ft'}]
                   )


def downgrade() -> None:
    op.drop_table('unit')

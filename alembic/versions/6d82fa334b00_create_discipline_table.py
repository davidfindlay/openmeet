"""create meet discipline table

Revision ID: 6d82fa334b00
Revises: 5b9f245b6be9
Create Date: 2022-11-13 21:45:14.877474

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey, Text, text, func


# revision identifiers, used by Alembic.
revision = '6d82fa334b00'
down_revision = '85cfe8a5be4c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    discipline_table = op.create_table(
        'discipline',
        Column('discipline_id', Integer, primary_key=True),
        Column('discipline_name', String(50), nullable=False),
        Column('abbreviation', String(10), nullable=False),
        Column('description', Text, nullable=True)
    )

    op.bulk_insert(discipline_table,
                   [{'discipline_name': 'Freestyle',
                     'abbreviation': 'FS'},
                    {'discipline_name': 'Breaststroke',
                     'abbreviation': 'BR'},
                    {'discipline_name': 'Backstroke',
                     'abbreviation': 'BS'},
                    {'discipline_name': 'Butterfly',
                     'abbreviation': 'FL'},
                    {'discipline_name': 'Individual Medley',
                     'abbreviation': 'IM'},
                    {'discipline_name': 'Medley',
                     'abbreviation': 'Med'}
                    ]
                   )


def downgrade() -> None:
    op.drop_table('discipline')

"""create meet discipline table

Revision ID: 6d82fa334b00
Revises: 55236cdb1e7f

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey, Text, text, func

# revision identifiers, used by Alembic.
revision = '6d82fa334b00'
down_revision = '55236cdb1e7f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    discipline_table = op.create_table(
        'discipline',
        Column('discipline_code', String(10), primary_key=True),
        Column('discipline_name', String(50), nullable=False),
        Column('abbreviation', String(10), nullable=False),
        Column('description', Text, nullable=True)
    )

    op.bulk_insert(discipline_table,
                   [{'discipline_code': 'FS',
                     'discipline_name': 'Freestyle',
                     'abbreviation': 'FS'},
                    {'discipline_code': 'BR',
                     'discipline_name': 'Breaststroke',
                     'abbreviation': 'BR'},
                    {'discipline_code': 'BS',
                     'discipline_name': 'Backstroke',
                     'abbreviation': 'BS'},
                    {'discipline_code': 'FL',
                     'discipline_name': 'Butterfly',
                     'abbreviation': 'FL'},
                    {'discipline_code': 'IM',
                     'discipline_name': 'Individual Medley',
                     'abbreviation': 'IM'},
                    {'discipline_code': 'MED',
                     'discipline_name': 'Medley',
                     'abbreviation': 'Med'}
                    ]
                   )


def downgrade() -> None:
    op.drop_table('discipline')

"""create meet event type table

Revision ID: 85cfe8a5be4c
Revises: 5b9f245b6be9
Create Date: 2022-11-13 21:08:41.387092

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey, text, func


# revision identifiers, used by Alembic.
revision = '85cfe8a5be4c'
down_revision = '996300c31a3a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    meet_event_type_table = op.create_table(
        'meet_event_type',
        Column('type_id', Integer, primary_key=True),
        Column('type_name', String(50), nullable=False)
    )

    op.bulk_insert(meet_event_type_table,
                   [{'type_name': 'Seeded Individual Mixed Finals'},
                    {'type_name': 'Seeded Mens Relay Finals'},
                    {'type_name': 'Seeded Womens Relay Finals'},
                    {'type_name': 'Seeded Mixed Relay Finals'},
                    {'type_name': 'Mixed Postal'}]
                   )


def downgrade() -> None:
    op.drop_table('meet_event_type')

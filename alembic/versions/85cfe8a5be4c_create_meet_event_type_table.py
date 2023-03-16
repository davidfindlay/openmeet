"""create meet event type table

Revision ID: 85cfe8a5be4c
Revises:

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey, text, func


# revision identifiers, used by Alembic.
revision = '85cfe8a5be4c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    meet_event_type_table = op.create_table(
        'meet_event_type',
        Column('type_code', String(10), primary_key=True),
        Column('type_name', String(50), nullable=False)
    )

    op.bulk_insert(meet_event_type_table,
                   [{'type_code': 'PS_SXIF', 'type_name': 'Seeded Individual Mixed Finals'},
                    {'type_code': 'PS_SMRF', 'type_name': 'Seeded Mens Relay Finals'},
                    {'type_code': 'PS_SWRF', 'type_name': 'Seeded Womens Relay Finals'},
                    {'type_code': 'PS_SXRF', 'type_name': 'Seeded Mixed Relay Finals'},
                    {'type_code': 'PS_MP', 'type_name': 'Mixed Postal'}]
                   )


def downgrade() -> None:
    op.drop_table('meet_event_type')

"""create entry table

Revision ID: fde67b28d19b
Revises: 65f3342114a7
Create Date: 2022-11-21 20:39:03.278943

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey, func, text, Boolean


# revision identifiers, used by Alembic.
revision = 'fde67b28d19b'
down_revision = '65f3342114a7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'entry',
        Column('athlete_id', Integer, ForeignKey('athlete.athlete_id'), primary_key=True),
        Column('meet_id', Integer, ForeignKey('meet.meet_id'), primary_key=True),
        Column('program_number', Integer, ForeignKey('meet_event.program_number'), primary_key=True),
        Column('seed_time', Float, nullable=True),
        Column('status', Integer, nullable=False),
        Column('cancelled', Boolean, nullable=True),
        Column('scratched', Boolean, nullable=True),
        Column('exhibition', Boolean, nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP)
    )


def downgrade() -> None:
    op.drop_table('entry')

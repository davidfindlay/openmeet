"""create heat lane table

Revision ID: 51663ab3dcd2
Revises: fde67b28d19b
Create Date: 2022-11-21 21:02:37.746995

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey, func, text, Boolean


# revision identifiers, used by Alembic.
revision = '51663ab3dcd2'
down_revision = '38be55d02c35'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'heat_lane',
        Column('meet_id', Integer, ForeignKey('heat.meet_id'), primary_key=True),
        Column('program_number', Integer, ForeignKey('heat.program_number'), primary_key=True),
        Column('heat_number', Integer, ForeignKey('heat.heat_number'), primary_key=True),
        Column('lane', Integer, primary_key=True),
        Column('athlete_id', Integer, ForeignKey('athlete.athlete_id'), nullable=True),
        Column('entry_id', Integer, ForeignKey('entry.entry_id'), nullable=True),
        Column('place', Integer, nullable=True),
        Column('tied', Boolean, nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP)
    )


def downgrade() -> None:
    op.drop_table('heat_lane')

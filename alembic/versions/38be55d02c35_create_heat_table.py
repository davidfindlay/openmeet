"""create heat table

Revision ID: 38be55d02c35
Revises: c38725a46378
Create Date: 2022-11-22 18:51:19.162605

"""
from alembic import op
from sqlalchemy import Column, Integer, Text, String, Date, DateTime, TIMESTAMP, ForeignKey, func, text, Boolean


# revision identifiers, used by Alembic.
revision = '38be55d02c35'
down_revision = '4845920c719f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'heat',
        Column('meet_id', Integer, ForeignKey('meet.meet_id'), primary_key=True),
        Column('program_number', Integer, ForeignKey('meet_event.program_number'), primary_key=True),
        Column('heat_number', Integer, primary_key=True),
        Column('start_dt', DateTime, nullable=True),
        Column('end_dt', DateTime, nullable=True),
        Column('skipped', Boolean, nullable=True),
        Column('skip_reason', String, nullable=True)
    )


def downgrade() -> None:
    op.drop_table('heat')

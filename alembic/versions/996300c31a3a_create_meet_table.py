"""create meet table

Revision ID: 996300c31a3a
Revises: 
Create Date: 2022-11-13 19:49:45.198314

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey, text, func


# revision identifiers, used by Alembic.
revision = '996300c31a3a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'meet',
        Column('meet_id', Integer, primary_key=True),
        Column('meetname', String(100), nullable=False),
        Column('startdate', Date, nullable=False),
        Column('enddate', Date, nullable=False),
        Column('deadline', DateTime, nullable=True),
        Column('max_individual_events', Integer, nullable=True),
        Column('max_relay_events', Integer, nullable=True),
        Column('max_total_events', Integer, nullable=True),
        Column('age_up_date', DateTime, nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP)
    )


def downgrade() -> None:
    op.drop_table('meet')

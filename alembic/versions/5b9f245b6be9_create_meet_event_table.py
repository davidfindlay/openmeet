"""create meet event table

Revision ID: 5b9f245b6be9
Revises: 996300c31a3a
Create Date: 2022-11-13 20:55:11.796857

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey, func, text


# revision identifiers, used by Alembic.
revision = '5b9f245b6be9'
down_revision = '55236cdb1e7f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'meet_event',
        Column('meet_id', Integer, ForeignKey('meet.meet_id'), primary_key=True),
        Column('program_number', String(4), primary_key=True),
        Column('event_name', String(100), nullable=True),
        Column('event_order', Integer, nullable=False),
        Column('event_type_id', Integer, ForeignKey('meet_event_type.type_id'), nullable=False),
        Column('discipline_id', Integer, ForeignKey('discipline.discipline_id'), nullable=False),
        Column('legs', Integer, nullable=False),
        Column('distance_id', Integer, ForeignKey('distance.distance_id'), nullable=False),
        Column('deadline', DateTime, nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP)
    )


def downgrade() -> None:
    op.drop_table('meet_event')

"""create meet event table

Revision ID: 5b9f245b6be9
Revises: f3af3ad433e8

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey, func, text


# revision identifiers, used by Alembic.
revision = '5b9f245b6be9'
down_revision = 'f3af3ad433e8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'meet_event',
        Column('meet_id', Integer, ForeignKey('meet.meet_id'), primary_key=True),
        Column('program_number', String(4), primary_key=True),
        Column('event_name', String(100), nullable=True),
        Column('event_order', Integer, nullable=False),
        Column('event_type_code', String(10), ForeignKey('meet_event_type.type_code'), nullable=False),
        Column('discipline_code', String(10), ForeignKey('discipline.discipline_code'), nullable=False),
        Column('legs', Integer, nullable=False),
        Column('distance_code', String(10), ForeignKey('distance.distance_code'), nullable=False),
        Column('deadline', DateTime, nullable=True),
        Column('age_group_type_code', String(10), ForeignKey('age_group_type.age_group_type_code'), nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP)
    )


def downgrade() -> None:
    op.drop_table('meet_event')

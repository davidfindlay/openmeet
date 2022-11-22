"""create athlete table

Revision ID: 65f3342114a7
Revises: e7d4dc6d357e
Create Date: 2022-11-18 15:07:57.987746

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey, func, text


# revision identifiers, used by Alembic.
revision = '65f3342114a7'
down_revision = 'e7d4dc6d357e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'athlete',
        Column('athlete_id', Integer, primary_key=True),
        Column('meet_id', Integer, ForeignKey('meet.meet_id'), primary_key=True),
        Column('surname', String(100), nullable=False),
        Column('first_name', String(50), nullable=False),
        Column('other_names', String(50), nullable=True),
        Column('preferred_name', String(100), nullable=True),
        Column('sex', String(1), nullable=True),
        Column('dob', Date, nullable=True),
        Column('age', Integer, nullable=True),
        Column('member_number', String(20), nullable=True),
        Column('team_id', Integer, ForeignKey('team.team_id'), nullable=True),
        Column('updated_at', DateTime, nullable=False),
        Column('created_at', DateTime, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('team')

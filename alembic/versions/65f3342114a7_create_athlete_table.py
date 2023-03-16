"""create athlete table

Revision ID: 65f3342114a7
Revises: 4845920c719f

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey, func, text


# revision identifiers, used by Alembic.
revision = '65f3342114a7'
down_revision = '4845920c719f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'athlete',
        Column('athlete_id', Integer, primary_key=True),
        Column('surname', String(100), nullable=False),
        Column('first_name', String(100), nullable=False),
        Column('other_names', String(100), nullable=True),
        Column('preferred_name', String(100), nullable=True),
        Column('sex', String(1), nullable=True),
        Column('dob', Date, nullable=True),
        Column('age', Integer, nullable=True),
        Column('member_number', String(20), nullable=True),
        Column('team_id', Integer, ForeignKey('team.team_id'), nullable=True),
        Column('import_id', Integer, nullable=True),
        Column('updated_at', DateTime, nullable=False),
        Column('created_at', DateTime, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('team')

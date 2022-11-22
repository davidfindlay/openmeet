"""create team table

Revision ID: a5af5b44b7fc
Revises: 48ffa49ac36b
Create Date: 2022-11-18 14:16:20.400831

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey, func, text


# revision identifiers, used by Alembic.
revision = 'a5af5b44b7fc'
down_revision = '48ffa49ac36b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'team',
        Column('team_id', Integer, primary_key=True),
        Column('meet_id', Integer, ForeignKey('meet.meet_id'), primary_key=True),
        Column('team_name', String(100), nullable=False),
        Column('team_number', Integer, nullable=True),
        Column('short_name', String(50), nullable=True),
        Column('abbreviation', String, nullable=True),
        Column('updated_at', DateTime, nullable=False),
        Column('created_at', DateTime, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('team')

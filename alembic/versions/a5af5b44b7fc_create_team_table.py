"""create team table

Revision ID: a5af5b44b7fc
Revises: e7d4dc6d357e

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey, func, text


# revision identifiers, used by Alembic.
revision = 'a5af5b44b7fc'
down_revision = 'e7d4dc6d357e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'team',
        Column('team_id', Integer, primary_key=True),
        Column('team_name', String(100), nullable=False),
        Column('short_name', String(50), nullable=True),
        Column('abbreviation', String(5), nullable=True),
        Column('import_id', Integer, nullable=True),
        Column('updated_at', DateTime, nullable=False),
        Column('created_at', DateTime, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('team')

"""create organisation table

Revision ID: e7d4dc6d357e
Revises: a5af5b44b7fc
Create Date: 2022-11-18 14:29:33.020047

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey, func, text


# revision identifiers, used by Alembic.
revision = 'e7d4dc6d357e'
down_revision = '996300c31a3a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'organisation',
        Column('organisation_id', Integer, primary_key=True),
        Column('organisation_name', String(100), nullable=False),
        Column('short_name', String(50), nullable=True),
        Column('abbreviation', String(5), nullable=True),
        Column('parent_id', Integer, ForeignKey('organisation.organisation_id'), nullable=True)
    )


def downgrade() -> None:
    op.drop_table('organisation')

"""create official table

Revision ID: 1042f0b6b124
Revises: d3265b331012
Create Date: 2022-12-03 11:30:33.883198

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKeyConstraint, TIMESTAMP, ForeignKey, func, text, Boolean, Text


# revision identifiers, used by Alembic.
revision = '1042f0b6b124'
down_revision = 'd3265b331012'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'official',
        Column('official_id', Integer, primary_key=True),
        Column('surname', String(100)),
        Column('first_name', String(100)),
        Column('other_name', String(100), nullable=True),
        Column('preferred_name', String(100), nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP)
    )


def downgrade() -> None:
    op.drop_table('official')

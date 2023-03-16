"""create score type table

Revision ID: 6240d43493dc
Revises: 157b52287580
Create Date: 2022-12-06 20:55:16.980970

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKeyConstraint, TIMESTAMP, ForeignKey, func, text, Boolean, Text


# revision identifiers, used by Alembic.
revision = '6240d43493dc'
down_revision = '157b52287580'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'score_type',
        Column('score_type_code', String(10), primary_key=True),
        Column('score_type_name', String(10), nullable=True),
        Column('description', String(40), nullable=False),
    )


def downgrade() -> None:
    op.drop_table('score_type')

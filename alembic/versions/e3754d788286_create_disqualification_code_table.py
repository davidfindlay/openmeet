"""create disqualification code table

Revision ID: e3754d788286
Revises: 1042f0b6b124
Create Date: 2022-12-03 11:34:47.220645

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKeyConstraint, TIMESTAMP, ForeignKey, func, text, Boolean, Text


# revision identifiers, used by Alembic.
revision = 'e3754d788286'
down_revision = '1042f0b6b124'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'disqualification_code',
        Column('disqualification_code', String(10), primary_key=True),
        Column('discipline_code', String(10), nullable=True),
        Column('description', String(40), nullable=False),
        Column('long_description',Text, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('disqualification_code')

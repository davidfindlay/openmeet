"""create time standard type table

Revision ID: 34a0b84805f8
Revises: b5132e6194ba
Create Date: 2022-12-06 21:34:05.899250

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DECIMAL, TIMESTAMP, ForeignKey, func, text, Boolean, Text


# revision identifiers, used by Alembic.
revision = '34a0b84805f8'
down_revision = 'b5132e6194ba'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'time_standard_type',
        Column('time_standard_type_code', String(10), primary_key=True),
        Column('time_standard_type_name', String(10), nullable=True),
        Column('organisation_id', Integer, ForeignKey('organisation.organisation_id'), nullable=True),
        Column('team_id', Integer, ForeignKey('team.team_id'), nullable=True),
        Column('description', String(40), nullable=False),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP)
    )


def downgrade() -> None:
    op.drop_table('time_standard_type')

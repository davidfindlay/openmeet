"""create record type table

Revision ID: 25718e84f56c
Revises: 21a74d661645
Create Date: 2022-12-06 21:17:52.272712

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKeyConstraint, TIMESTAMP, ForeignKey, func, text, Boolean, Text


# revision identifiers, used by Alembic.
revision = '25718e84f56c'
down_revision = '21a74d661645'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'record_type',
        Column('record_type_code', String(10), primary_key=True),
        Column('record_type_name', String(10), nullable=True),
        Column('description', String(40), nullable=False),
        Column('organisation_id', Integer, ForeignKey('organisation.organisation_id'), nullable=True),
        Column('team_id', Integer, ForeignKey('team.team_id'), nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP)
    )


def downgrade() -> None:
    op.drop_table('record_type')

"""create relay member table

Revision ID: 38d52928d540
Revises: 474e84382d72
Create Date: 2022-12-02 15:27:45.772889

"""
from alembic import op
from sqlalchemy import Column, Integer, DECIMAL, String, TIMESTAMP, ForeignKey, ForeignKeyConstraint, Boolean


# revision identifiers, used by Alembic.
revision = '38d52928d540'
down_revision = '474e84382d72'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'relay_member',
        Column('relay_entry_id', Integer, ForeignKey('relay_entry.relay_entry_id'), primary_key=True),
        Column('leg', Integer, primary_key=True),
        Column('athlete_id', Integer, ForeignKey('athlete.athlete_id')),
        Column('cancelled', Boolean, nullable=True),
        Column('seed_time', DECIMAL(9, 3), nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP),
    )


def downgrade() -> None:
    op.drop_table('relay_member')

"""create result time table

Revision ID: c38725a46378
Revises: 4845920c719f
Create Date: 2022-11-22 11:15:25.129794

"""
from alembic import op
from sqlalchemy import Column, Integer, DECIMAL, Float, String, Date, DateTime, TIMESTAMP, ForeignKey, func, text, Boolean, Text


# revision identifiers, used by Alembic.
revision = 'c38725a46378'
down_revision = '51663ab3dcd2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'result_time',
        Column('meet_id', Integer, ForeignKey('heat.meet_id'), primary_key=True),
        Column('program_number', Integer, ForeignKey('heat.program_number'), primary_key=True),
        Column('heat_number', Integer, ForeignKey('heat.heat_number'), primary_key=True),
        Column('lane', Integer, ForeignKey('heat.lane'), primary_key=True),
        Column('time_type_id', Integer, ForeignKey('time_type.time_type_id'), primary_key=True),
        Column('time', DECIMAL(9, 3), nullable=False),
        Column('rejected', Boolean, nullable=False, default=False),
        Column('rejected_reason', String, nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP)
    )


def downgrade() -> None:
    op.drop_table('result_time')

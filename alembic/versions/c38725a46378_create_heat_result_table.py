"""create result time table

Revision ID: c38725a46378
Revises: 51663ab3dcd2
Create Date: 2022-11-22 11:15:25.129794

"""
from alembic import op
from sqlalchemy import Column, Integer, DECIMAL, ForeignKeyConstraint, String, TIMESTAMP, ForeignKey, func, text, Boolean, Text


# revision identifiers, used by Alembic.
revision = 'c38725a46378'
down_revision = '51663ab3dcd2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'heat_result',
        Column('meet_id', Integer, primary_key=True),
        Column('program_number', Integer, primary_key=True),
        Column('heat_number', Integer, primary_key=True),
        Column('lane', Integer, primary_key=True),
        Column('time_type_code', String(10), ForeignKey('time_type.time_type_code'), primary_key=True),
        Column('seconds', DECIMAL(9, 3), nullable=False),
        Column('rejected', Boolean, nullable=False, default=False),
        Column('rejected_reason', String, nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP),
        ForeignKeyConstraint(
            ["meet_id", "program_number", "heat_number", "lane"],
            ["heat_lane.meet_id", "heat_lane.program_number", 'heat_lane.heat_number', 'heat_lane.lane']
        )
    )


def downgrade() -> None:
    op.drop_table('heat_result')

"""create disqualification table

Revision ID: 157b52287580
Revises: e3754d788286
Create Date: 2022-12-03 11:40:17.996115

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKeyConstraint, TIMESTAMP, ForeignKey, func, text, Boolean, Text


# revision identifiers, used by Alembic.
revision = '157b52287580'
down_revision = 'e3754d788286'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'disqualification',
        Column('disqualification_id', Integer, primary_key=True),
        Column('meet_id', Integer),             # Composite Foreign Key to heat_lane
        Column('program_number', String(4)),    # Composite Foreign Key to heat_lane
        Column('heat_number', Integer),         # Composite Foreign Key to heat_lane
        Column('lane', Integer),                # Composite Foreign Key to heat_lane
        Column('entry_id', Integer, ForeignKey('entry.entry_id'), nullable=True),
        Column('relay_entry_id', Integer, ForeignKey('relay_entry.relay_entry_id'), nullable=True),
        Column('discipline_code', String(10), nullable=True),
        Column('official_id', Integer, ForeignKey('official.official_id'), nullable=True),
        Column('referee_id', Integer, ForeignKey('official.official_id'), nullable=True),
        Column('reason', Text, nullable=True),
        Column('cancelled', Boolean, nullable=True),
        Column('cancelled_reason', Text, nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP),
        ForeignKeyConstraint(
            ["meet_id", "program_number", "heat_number", "lane"],
            ["heat_lane.meet_id", "heat_lane.program_number", 'heat_lane.heat_number', 'heat_lane.lane']
        )
    )


def downgrade() -> None:
    op.drop_table('disqualification')

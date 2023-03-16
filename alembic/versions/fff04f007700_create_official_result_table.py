"""create official result table

Revision ID: fff04f007700
Revises: 4b9245f97216
Create Date: 2022-12-02 16:24:24.443159

"""
from alembic import op
from sqlalchemy import Column, Integer, DECIMAL, String, TIMESTAMP, ForeignKey, ForeignKeyConstraint, Boolean


# revision identifiers, used by Alembic.
revision = 'fff04f007700'
down_revision = '4b9245f97216'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'official_result',
        Column('result_id', Integer, primary_key=True),
        Column('meet_id', Integer),             # Composite foreign key to meet_event
        Column('program_number', String(4)),    # Composite foreign key to meet_event
        Column('entry_id', Integer, ForeignKey('entry.entry_id'), nullable=True),
        Column('relay_entry_id', Integer, ForeignKey('relay_entry.relay_entry_id'), nullable=True),
        Column('age_group_code', String(4), ForeignKey('age_group.age_group_code'), nullable=True),
        Column('team_id', Integer, ForeignKey('team.team_id'), nullable=True),
        Column('seconds', DECIMAL(9, 3), nullable=True),
        Column('distance', Integer, nullable=True),
        Column('unit_id', Integer, ForeignKey('unit.unit_id'), nullable=True),
        Column('place', Integer, nullable=True),
        Column('tied', Boolean, nullable=True),
        Column('no_start', Boolean, nullable=True),
        Column('no_finish', Boolean, nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP),
        ForeignKeyConstraint(
            ["meet_id", "program_number"], ["meet_event.meet_id", "meet_event.program_number"]
        )
    )


def downgrade() -> None:
    op.drop_table('official_result')

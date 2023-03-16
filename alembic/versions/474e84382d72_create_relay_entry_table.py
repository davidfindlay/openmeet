"""create relay entry table

Revision ID: 474e84382d72
Revises: fde67b28d19b
Create Date: 2022-12-02 15:19:46.783119

"""
from alembic import op
from sqlalchemy import Column, Integer, DECIMAL, String, TIMESTAMP, ForeignKey, ForeignKeyConstraint, Boolean


# revision identifiers, used by Alembic.
revision = '474e84382d72'
down_revision = 'fde67b28d19b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'relay_entry',
        Column('relay_entry_id', Integer, primary_key=True),
        Column('meet_id', Integer),
        Column('program_number', String(4)),
        Column('team_id', Integer, ForeignKey('team.team_id'), nullable=True),
        Column('organisation_id', Integer, nullable=True),
        Column('seed_time', DECIMAL(9, 3), nullable=True),
        Column('letter', String(1), nullable=True),
        Column('team_name', String(40), nullable=True),
        Column('status_code', String(10), nullable=False),
        Column('cancelled', Boolean, nullable=True),
        Column('scratched', Boolean, nullable=True),
        Column('exhibition', Boolean, nullable=True),
        Column('age_group_code', Integer, ForeignKey('age_group.age_group_code'), nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP),
        ForeignKeyConstraint(
            ["meet_id", "program_number"], ["meet_event.meet_id", "meet_event.program_number"]
        )
    )


def downgrade() -> None:
    op.drop_table('relay_entry')

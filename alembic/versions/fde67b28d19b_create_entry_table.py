"""create entry table

Revision ID: fde67b28d19b
Revises: c38725a46378

"""
from alembic import op
from sqlalchemy import Column, Integer, DECIMAL, String, TIMESTAMP, ForeignKey, ForeignKeyConstraint, Boolean, UniqueConstraint


# revision identifiers, used by Alembic.
revision = 'fde67b28d19b'
down_revision = 'c38725a46378'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'entry',
        Column('entry_id', Integer, primary_key=True),
        Column('athlete_id', Integer, ForeignKey('athlete.athlete_id')),
        Column('meet_id', Integer),
        Column('program_number', String(4)),
        Column('seed_time', DECIMAL(9, 3), nullable=True),
        Column('status_code', String(10), nullable=False),
        Column('cancelled', Boolean, nullable=True),
        Column('scratched', Boolean, nullable=True),
        Column('exhibition', Boolean, nullable=True),
        Column('age_group_code', Integer, ForeignKey('age_group.age_group_code'), nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP),
        ForeignKeyConstraint(
            ["meet_id", "program_number"], ["meet_event.meet_id", "meet_event.program_number"]
        ),
        UniqueConstraint('athlete_id', 'meet_id', 'program_number', name='entry_unique')
    )


def downgrade() -> None:
    op.drop_table('entry')

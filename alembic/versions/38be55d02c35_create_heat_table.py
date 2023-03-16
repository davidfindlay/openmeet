"""create heat table

Revision ID: 38be55d02c35
Revises: 65f3342114a7

"""
from alembic import op
from sqlalchemy import Column, Integer, Text, String, Date, DateTime, TIMESTAMP, ForeignKeyConstraint, func, text, Boolean


# revision identifiers, used by Alembic.
revision = '38be55d02c35'
down_revision = '65f3342114a7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'heat',
        Column('meet_id', Integer, primary_key=True),
        Column('program_number', Integer, primary_key=True),
        Column('heat_number', Integer, primary_key=True),
        Column('start_dt', DateTime, nullable=True),
        Column('end_dt', DateTime, nullable=True),
        Column('skipped', Boolean, nullable=True),
        Column('skip_reason', String(20), nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP),
        ForeignKeyConstraint(
            ["meet_id", "program_number"], ["meet_event.meet_id", "meet_event.program_number"]
        )
    )


def downgrade() -> None:
    op.drop_table('heat')

"""create relay score table

Revision ID: 21a74d661645
Revises: 6bf438a1eb24
Create Date: 2022-12-06 21:10:05.556678

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKeyConstraint, TIMESTAMP, ForeignKey, func, text, Boolean, Text



# revision identifiers, used by Alembic.
revision = '21a74d661645'
down_revision = '6bf438a1eb24'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'relay_score',
        Column('meet_id', Integer, ForeignKey('meet.meet_id'), primary_key=True),
        Column('program_number', String(4), primary_key=True),
        Column('score_type_code', String(10), ForeignKey('score_type.score_type_code'), primary_key=True),
        Column('relay_entry_id', Integer, ForeignKey('relay_entry.relay_entry_id'), primary_key=True),
        Column('score', Float, nullable=False),
        Column('place', Integer, nullable=True),
        Column('tied', Boolean, nullable=True),
        Column('age_group_code', String(10), ForeignKey('age_group.age_group_code'), nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP),
        ForeignKeyConstraint(
            ["meet_id", "program_number"], ["meet_event.meet_id", "meet_event.program_number"]
        )
    )


def downgrade() -> None:
    op.drop_table('relay_score')

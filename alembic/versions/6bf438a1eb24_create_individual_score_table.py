"""create individual score table

Revision ID: 6bf438a1eb24
Revises: 6240d43493dc
Create Date: 2022-12-06 20:59:57.959433

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKeyConstraint, TIMESTAMP, ForeignKey, func, text, Boolean, Text


# revision identifiers, used by Alembic.
revision = '6bf438a1eb24'
down_revision = '6240d43493dc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'individual_score',
        Column('meet_id', Integer, ForeignKey('meet.meet_id'), primary_key=True),
        Column('program_number', String(4), primary_key=True),
        Column('score_type_code', String(10), ForeignKey('score_type.score_type_code'), primary_key=True),
        Column('athlete_id', Integer, ForeignKey('athlete.athlete_id'), primary_key=True),
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
    op.drop_table('individual_score')


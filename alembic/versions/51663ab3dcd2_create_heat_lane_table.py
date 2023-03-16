"""create heat lane table

Revision ID: 51663ab3dcd2
Revises: 38be55d02c35

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, ForeignKeyConstraint, TIMESTAMP, ForeignKey, func, text, Boolean


# revision identifiers, used by Alembic.
revision = '51663ab3dcd2'
down_revision = '38be55d02c35'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'heat_lane',
        Column('meet_id', Integer, primary_key=True),
        Column('program_number', Integer, primary_key=True),
        Column('heat_number', Integer, primary_key=True),
        Column('lane', Integer, primary_key=True),
        Column('athlete_id', Integer, ForeignKey('athlete.athlete_id'), nullable=True),
        Column('relay_team_id', Integer, ForeignKey('relay_team.relay_team_id'), nullable=True),
        Column('place', Integer, nullable=True),
        Column('tied', Boolean, nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP),
        ForeignKeyConstraint(
            ["meet_id", "program_number", "heat_number"], ["heat.meet_id", "heat.program_number", 'heat.heat_number']
        )
    )


def downgrade() -> None:
    op.drop_table('heat_lane')

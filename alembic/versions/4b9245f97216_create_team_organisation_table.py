"""create team organisation table

Revision ID: 4b9245f97216
Revises: 38d52928d540
Create Date: 2022-12-02 15:44:12.820088

"""
from alembic import op
from sqlalchemy import Column, Integer, ForeignKey


# revision identifiers, used by Alembic.
revision = '4b9245f97216'
down_revision = '38d52928d540'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'team_organisation',
        Column('team_id', Integer, ForeignKey('team.team_id'), primary_key=True),
        Column('organisation_id', Integer, ForeignKey('organisation.organisation_id'), primary_key=True)
    )


def downgrade() -> None:
    op.drop_table('team_organisation')

"""create official role table

Revision ID: d3265b331012
Revises: fff04f007700
Create Date: 2022-12-03 11:24:58.158589

"""
from alembic import op
from sqlalchemy import Column, Text, String


# revision identifiers, used by Alembic.
revision = 'd3265b331012'
down_revision = 'fff04f007700'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'official_role',
        Column('role_code', String(10), primary_key=True),
        Column('role_name', String(50), nullable=False),
        Column('description', Text, nullable=True)
    )


def downgrade() -> None:
    op.drop_table('official_role')

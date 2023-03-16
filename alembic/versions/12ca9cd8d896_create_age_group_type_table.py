"""create age group type table

Revision ID: 12ca9cd8d896
Revises: 6d82fa334b00

"""
from alembic import op
from sqlalchemy import Column, Integer, String, Text

# revision identifiers, used by Alembic.
revision = '12ca9cd8d896'
down_revision = '6d82fa334b00'
branch_labels = None
depends_on = None


def upgrade() -> None:
    age_group_types = op.create_table(
        'age_group_type',
        Column('age_group_type_code', String(10), primary_key=True),
        Column('age_group_type_name', String(50), nullable=False),
        Column('description', Text, nullable=True)
    )

    op.bulk_insert(age_group_types,
                   [
                       {
                           'age_group_type_code': 'USMS5YR',
                           'age_group_type_name': 'US 5 Year'
                       }
                   ])


def downgrade() -> None:
    op.drop_table('age_group_type')

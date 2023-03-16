"""create time standard table

Revision ID: 0eaf2b9a25c9
Revises: 34a0b84805f8
Create Date: 2022-12-06 21:36:35.568317

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DECIMAL, TIMESTAMP, ForeignKey, func, text, Boolean, Text


# revision identifiers, used by Alembic.
revision = '0eaf2b9a25c9'
down_revision = '34a0b84805f8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'time_standard',
        Column('time_standard_id', Integer, primary_key=True),
        Column('time_standard_type_code', String(4), ForeignKey('time_standard_type.time_standard_type_code')),
        Column('discipline_code', String(10), ForeignKey('discipline.discipline_code')),
        Column('distance_code', String(10), ForeignKey('distance.distance_code')),
        Column('age_group_code', String(10), ForeignKey('age_group.age_group_code'), nullable=True),
        Column('seconds', DECIMAL(9, 3), nullable=True),
        Column('distance', Integer, nullable=True),
        Column('unit_code', String(10), ForeignKey('unit.unit_code'), nullable=True),
        Column('legs', Integer, nullable=True),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP)
    )


def downgrade() -> None:
    op.drop_table('time_standard')

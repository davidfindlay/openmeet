"""create record table

Revision ID: b5132e6194ba
Revises: 25718e84f56c
Create Date: 2022-12-06 21:26:39.919109

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DECIMAL, TIMESTAMP, ForeignKey, func, text, Boolean, Text


# revision identifiers, used by Alembic.
revision = 'b5132e6194ba'
down_revision = '25718e84f56c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'record',
        Column('record_id', Integer, primary_key=True),
        Column('record_type_code', String(4), ForeignKey('record_type.record_type_code')),
        Column('discipline_code', String(10), ForeignKey('discipline.discipline_code')),
        Column('distance_code', String(10), ForeignKey('distance.distance_code')),
        Column('age_group_code', String(10), ForeignKey('age_group.age_group_code'), nullable=True),
        Column('seconds', DECIMAL(9,3), nullable=True),
        Column('distance', Integer, nullable=True),
        Column('unit_code', String(10), ForeignKey('unit.unit_code'), nullable=True),
        Column('legs', Integer, nullable=True),
        Column('record_date', Date),
        Column('holder_name', String(200)),
        Column('location', String(100)),
        Column('updated_at', TIMESTAMP),
        Column('created_at', TIMESTAMP)
    )


def downgrade() -> None:
    op.drop_table('record')

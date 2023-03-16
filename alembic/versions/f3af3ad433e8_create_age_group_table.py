"""create age group table

Revision ID: f3af3ad433e8
Revises: 12ca9cd8d896

"""
from alembic import op
from sqlalchemy import Column, Integer, String, ForeignKey


# revision identifiers, used by Alembic.
revision = 'f3af3ad433e8'
down_revision = '12ca9cd8d896'
branch_labels = None
depends_on = None


def upgrade() -> None:
    age_group = op.create_table(
        'age_group',
        Column('age_group_code', String(10), primary_key=True),
        Column('age_group_type_code', String(10), ForeignKey('age_group_type.age_group_type_code')),
        Column('min', Integer, nullable=False),
        Column('max', Integer, nullable=False),
        Column('sex', String(1), nullable=True),
        Column('legs', Integer, nullable=False),
        Column('age_group_name', String, nullable=False)
    )

    op.bulk_insert(age_group,
                   [
                       {
                           'age_group_code': 'M18_24',
                           'age_group_type_code': 'USMS5YR',
                           'min': 18,
                           'max': 24,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 18-24'
                       },
                       {
                           'age_group_code': 'F18_24',
                           'age_group_type_code': 'USMS5YR',
                           'min': 18,
                           'max': 24,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 18-24'
                       },
                       {
                           'age_group_code': 'M25_29',
                           'age_group_type_code': 'USMS5YR',
                           'min': 25,
                           'max': 29,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 25-29'
                       },
                       {
                           'age_group_code': 'F25_29',
                           'age_group_type_code': 'USMS5YR',
                           'min': 25,
                           'max': 29,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 25-29'
                       },
                       {
                           'age_group_code': 'M30_34',
                           'age_group_type_code': 'USMS5YR',
                           'min': 30,
                           'max': 34,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 30-34'
                       },
                       {
                           'age_group_code': 'F30_34',
                           'age_group_type_code': 'USMS5YR',
                           'min': 30,
                           'max': 34,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 30-34'
                       },
                       {
                           'age_group_code': 'M35_39',
                           'age_group_type_code': 'USMS5YR',
                           'min': 35,
                           'max': 39,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 35-39'
                       },
                       {
                           'age_group_code': 'F35_39',
                           'age_group_type_code': 'USMS5YR',
                           'min': 35,
                           'max': 39,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 35-39'
                       },
                       {
                           'age_group_code': 'M40_44',
                           'age_group_type_code': 'USMS5YR',
                           'min': 40,
                           'max': 44,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 40-44'
                       },
                       {
                           'age_group_code': 'F40_44',
                           'age_group_type_code': 'USMS5YR',
                           'min': 40,
                           'max': 44,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 40-44'
                       },
                       {
                           'age_group_code': 'M45_49',
                           'age_group_type_code': 'USMS5YR',
                           'min': 45,
                           'max': 49,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 45-49'
                       },
                       {
                           'age_group_code': 'F45_49',
                           'age_group_type_code': 'USMS5YR',
                           'min': 45,
                           'max': 49,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 45-49'
                       },
                       {
                           'age_group_code': 'M50-54',
                           'age_group_type_code': 'USMS5YR',
                           'min': 50,
                           'max': 54,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 50-54'
                       },
                       {
                           'age_group_code': 'F50-54',
                           'age_group_type_code': 'USMS5YR',
                           'min': 50,
                           'max': 54,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 50-54'
                       },
                       {
                           'age_group_code': 'M55-59',
                           'age_group_type_code': 'USMS5YR',
                           'min': 55,
                           'max': 59,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 55-59'
                       },
                       {
                           'age_group_code': 'F55-59',
                           'age_group_type_code': 'USMS5YR',
                           'min': 55,
                           'max': 59,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 55-59'
                       },
                       {
                           'age_group_code': 'M60-64',
                           'age_group_type_code': 'USMS5YR',
                           'min': 60,
                           'max': 64,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 60-64'
                       },
                       {
                           'age_group_code': 'F60-64',
                           'age_group_type_code': 'USMS5YR',
                           'min': 60,
                           'max': 64,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 60-64'
                       },
                       {
                           'age_group_code': 'M65-59',
                           'age_group_type_code': 'USMS5YR',
                           'min': 65,
                           'max': 69,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 65-69'
                       },
                       {
                           'age_group_code': 'F65-69',
                           'age_group_type_code': 'USMS5YR',
                           'min': 65,
                           'max': 69,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 65-69'
                       },
                       {
                           'age_group_code': 'M70-74',
                           'age_group_type_code': 'USMS5YR',
                           'min': 70,
                           'max': 74,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 70-74'
                       },
                       {
                           'age_group_code': 'F70-74',
                           'age_group_type_code': 'USMS5YR',
                           'min': 70,
                           'max': 74,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 70-74'
                       },
                       {
                           'age_group_code': 'M75-79',
                           'age_group_type_code': 'USMS5YR',
                           'min': 75,
                           'max': 79,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 75-79'
                       },
                       {
                           'age_group_code': 'F75-79',
                           'age_group_type_code': 'USMS5YR',
                           'min': 75,
                           'max': 79,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 75-79'
                       },
                       {
                           'age_group_code': 'M80-84',
                           'age_group_type_code': 'USMS5YR',
                           'min': 80,
                           'max': 84,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 80-84'
                       },
                       {
                           'age_group_code': 'F80-84',
                           'age_group_type_code': 'USMS5YR',
                           'min': 80,
                           'max': 84,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 80-84'
                       },
                       {
                           'age_group_code': 'M85-89',
                           'age_group_type_code': 'USMS5YR',
                           'min': 85,
                           'max': 89,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 85-89'
                       },
                       {
                           'age_group_code': 'F85-89',
                           'age_group_type_code': 'USMS5YR',
                           'min': 85,
                           'max': 89,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 85-89'
                       },
                       {
                           'age_group_code': 'M90-94',
                           'age_group_type_code': 'USMS5YR',
                           'min': 90,
                           'max': 94,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 90-94'
                       },
                       {
                           'age_group_code': 'F90-94',
                           'age_group_type_code': 'USMS5YR',
                           'min': 90,
                           'max': 94,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 90-94'
                       },
                       {
                           'age_group_code': 'M95-99',
                           'age_group_type_code': 'USMS5YR',
                           'min': 95,
                           'max': 99,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 95-99'
                       },
                       {
                           'age_group_code': 'F95-99',
                           'age_group_type_code': 'USMS5YR',
                           'min': 95,
                           'max': 99,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 95-99'
                       },
                       {
                           'age_group_code': 'M100-M104',
                           'age_group_type_code': 'USMS5YR',
                           'min': 100,
                           'max': 104,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 100-104'
                       },
                       {
                           'age_group_code': 'F100-F104',
                           'age_group_type_code': 'USMS5YR',
                           'min': 100,
                           'max': 104,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 100-104'
                       },
                       {
                           'age_group_code': 'M105-109',
                           'age_group_type_code': 'USMS5YR',
                           'min': 105,
                           'max': 109,
                           'sex': 'M',
                           'legs': 1,
                           'age_group_name': 'Men\'s 105-109'
                       },
                       {
                           'age_group_code': 'F105-109',
                           'age_group_type_code': 'USMS5YR',
                           'min': 105,
                           'max': 109,
                           'sex': 'F',
                           'legs': 1,
                           'age_group_name': 'Women\'s 105-109'
                       },
                   ])


def downgrade() -> None:
    op.drop_table('age_group')

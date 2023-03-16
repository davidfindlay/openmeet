"""create course table

Revision ID: 48ffa49ac36b
Revises: 0d79c9663ad3

"""
from alembic import op
from sqlalchemy import Column, Integer, String, ForeignKey

# revision identifiers, used by Alembic.
revision = '48ffa49ac36b'
down_revision = '0d79c9663ad3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    course_table = op.create_table(
        'course',
        Column('course_code', String(10), primary_key=True),
        Column('course_name', String(50), nullable=False),
        Column('course_full_name', String(50), nullable=False),
        Column('abbreviation', String(4), nullable=False),
        Column('length', Integer, nullable=False),
        Column('unit_code', String(10), ForeignKey('unit.unit_code'), nullable=False)
    )

    op.bulk_insert(course_table,
                   [{'course_code': 'LCM',
                     'course_name': 'Long Course',
                     'course_full_name': 'Long Course Metres',
                     'length': 50,
                     'abbreviation': 'LCM',
                     'unit_code': 'm'},
                    {'course_code': 'SCM',
                     'course_name': 'Short Course',
                     'course_full_name': 'Short Course Metres',
                     'length': 25,
                     'abbreviation': 'SCM',
                     'unit_code': 'm'},
                    {'course_code': 'LCY',
                     'course_name': 'Long Course',
                     'course_full_name': 'Long Course Yards',
                     'length': 50,
                     'abbreviation': 'LCY',
                     'unit_code': 'yd'},
                    {'course_code': 'SCY',
                     'course_name': 'Short Course',
                     'course_full_name': 'Short Course Yards',
                     'length': 25,
                     'abbreviation': 'SCY',
                     'unit_code': 'yd'}
                    ]
                   )


def downgrade() -> None:
    op.drop_table('course')

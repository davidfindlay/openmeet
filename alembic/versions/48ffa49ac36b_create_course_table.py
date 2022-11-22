"""create course table

Revision ID: 48ffa49ac36b
Revises: 5b9f245b6be9
Create Date: 2022-11-16 09:34:09.309818

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey

# revision identifiers, used by Alembic.
revision = '48ffa49ac36b'
down_revision = '5b9f245b6be9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    course_table = op.create_table(
        'course',
        Column('course_id', Integer, primary_key=True, autoincrement=True),
        Column('course_name', String(50), nullable=False),
        Column('course_full_name', String(50), nullable=False),
        Column('abbreviation', String(4), nullable=False),
        Column('length', Integer, nullable=False),
        Column('unit_id', Integer, ForeignKey('unit.unit_id'), nullable=False)
    )

    op.bulk_insert(course_table,
                   [{'course_name': 'Long Course',
                     'course_full_name': 'Long Course Metres',
                     'length': 50,
                     'abbreviation': 'LCM',
                     'unit_id': 1},
                    {'course_name': 'Short Course',
                     'course_full_name': 'Short Course Metres',
                     'length': 25,
                     'abbreviation': 'SCM',
                     'unit_id': 1},
                    {'course_name': 'Long Course',
                     'course_full_name': 'Long Course Yards',
                     'length': 50,
                     'abbreviation': 'LCY',
                     'unit_id': 2},
                    {'course_name': 'Short Course',
                     'course_full_name': 'Short Course Yards',
                     'length': 25,
                     'abbreviation': 'SCY',
                     'unit_id': 2}
                    ]
                   )


def downgrade() -> None:
    op.drop_table('course')

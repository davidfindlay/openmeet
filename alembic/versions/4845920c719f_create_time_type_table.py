"""create time type table

Revision ID: 4845920c719f
Revises: 51663ab3dcd2
Create Date: 2022-11-22 10:55:37.447929

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey, func, text, Boolean, Text


# revision identifiers, used by Alembic.
revision = '4845920c719f'
down_revision = 'fde67b28d19b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    time_type_table = op.create_table(
        'time_type',
        Column('time_type_id', Integer, primary_key=True, autoincrement=True),
        Column('time_type_name', String, nullable=False),
        Column('description', Text, nullable=True),
    )

    op.bulk_insert(time_type_table,
                   [{'time_type_name': 'Pad',
                     'description': 'Touchpads'
                     },
                    {'time_type_name': 'Backup 1',
                     'description': 'Plunger time'
                     },
                    {'time_type_name': 'Backup 2',
                     'description': 'Plunger time'
                     },
                    {'time_type_name': 'Backup 3',
                     'description': 'Plunger time'
                     },
                    {'time_type_name': 'Stopwatch',
                     'description': 'Backup stopwatch time'
                     },
                    {'time_type_name': 'Manual',
                     'description': 'Manual override time'
                     },
                    ])


def downgrade() -> None:
    op.drop_table('time_type')

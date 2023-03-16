"""create time type table

Revision ID: 4845920c719f
Revises: a5af5b44b7fc
Create Date: 2022-11-22 10:55:37.447929

"""
from alembic import op
from sqlalchemy import Column, Integer, Float, String, Date, DateTime, TIMESTAMP, ForeignKey, func, text, Boolean, Text

# revision identifiers, used by Alembic.
revision = '4845920c719f'
down_revision = 'a5af5b44b7fc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    time_type_table = op.create_table(
        'time_type',
        Column('time_type_code', String(10), primary_key=True),
        Column('time_type_name', String(20), nullable=False),
        Column('description', Text, nullable=True),
    )

    op.bulk_insert(time_type_table,
                   [{'time_type_code': 'PAD',
                     'time_type_name': 'Pad',
                     'description': 'Touchpads'
                     },
                    {'time_type_code': 'BACKUP1',
                     'time_type_name': 'Backup 1',
                     'description': 'Plunger time'
                     },
                    {'time_type_code': 'BACKUP2',
                     'time_type_name': 'Backup 2',
                     'description': 'Plunger time'
                     },
                    {'time_type_code': 'BACKUP3',
                     'time_type_name': 'Backup 3',
                     'description': 'Plunger time'
                     },
                    {'time_type_code': 'WATCH',
                     'time_type_name': 'Stopwatch',
                     'description': 'Backup stopwatch time'
                     },
                    {'time_type_code': 'MANUAL',
                     'time_type_name': 'Manual',
                     'description': 'Manual override time'
                     },
                    ])


def downgrade() -> None:
    op.drop_table('time_type')

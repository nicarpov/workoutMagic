"""Workout name is Optional

Revision ID: ae2eaf19e94a
Revises: 6e05fd804dc4
Create Date: 2025-05-29 15:52:37.054411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae2eaf19e94a'
down_revision = '6e05fd804dc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workout', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('workout', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)

    # ### end Alembic commands ###

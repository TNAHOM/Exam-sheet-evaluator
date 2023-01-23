"""'nobudget'

Revision ID: 70e568207abf
Revises: 5f556279599f
Create Date: 2022-12-31 13:52:46.033257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70e568207abf'
down_revision = '5f556279599f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('budget')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('budget', sa.INTEGER(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###

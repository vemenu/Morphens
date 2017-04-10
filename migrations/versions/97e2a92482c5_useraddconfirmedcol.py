"""'abc'

Revision ID: 97e2a92482c5
Revises: 02bf05d166db
Create Date: 2017-04-11 00:39:13.750834

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '97e2a92482c5'
down_revision = '02bf05d166db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
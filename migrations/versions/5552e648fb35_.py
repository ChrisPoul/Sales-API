"""empty message

Revision ID: 5552e648fb35
Revises: 98eb5fb7d911
Create Date: 2021-10-08 14:19:41.318997

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5552e648fb35'
down_revision = '98eb5fb7d911'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sold_product', sa.Column('price', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sold_product', 'price')
    # ### end Alembic commands ###
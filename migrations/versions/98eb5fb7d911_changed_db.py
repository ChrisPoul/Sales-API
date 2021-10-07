"""Changed db

Revision ID: 98eb5fb7d911
Revises: 
Create Date: 2021-10-07 18:46:30.191507

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98eb5fb7d911'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('receipt',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('time_created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('time_updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sold_product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('receipt_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('time_created', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('time_updated', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['receipt_id'], ['receipt.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sold_product')
    op.drop_table('receipt')
    # ### end Alembic commands ###

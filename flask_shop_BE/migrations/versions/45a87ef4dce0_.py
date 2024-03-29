"""empty message

Revision ID: 45a87ef4dce0
Revises: 1c907bd77c4b
Create Date: 2020-04-26 18:51:43.668423

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45a87ef4dce0'
down_revision = '1c907bd77c4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_goods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=512), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('introduce', sa.Text(), nullable=True),
    sa.Column('big_log', sa.String(length=256), nullable=True),
    sa.Column('small_log', sa.String(length=256), nullable=True),
    sa.Column('state', sa.Integer(), nullable=True),
    sa.Column('is_promte', sa.Integer(), nullable=True),
    sa.Column('hot_number', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.Column('cid_one', sa.Integer(), nullable=True),
    sa.Column('cid_two', sa.Integer(), nullable=True),
    sa.Column('cid_three', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cid_one'], ['t_category.id'], ),
    sa.ForeignKeyConstraint(['cid_three'], ['t_category.id'], ),
    sa.ForeignKeyConstraint(['cid_two'], ['t_category.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_goods')
    # ### end Alembic commands ###

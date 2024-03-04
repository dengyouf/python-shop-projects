"""empty message

Revision ID: e9fcdd60a65a
Revises: 2da8744f9089
Create Date: 2020-05-02 18:53:55.132354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9fcdd60a65a'
down_revision = '2da8744f9089'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('t_goods_attr',
    sa.Column('gid', sa.Integer(), nullable=False),
    sa.Column('aid', sa.Integer(), nullable=False),
    sa.Column('val', sa.String(length=512), nullable=True),
    sa.Column('_type', sa.String(length=8), nullable=True),
    sa.ForeignKeyConstraint(['aid'], ['t_attribute.id'], ),
    sa.ForeignKeyConstraint(['gid'], ['t_goods.id'], ),
    sa.PrimaryKeyConstraint('gid', 'aid')
    )
    op.create_table('t_picture',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sa.String(length=512), nullable=True),
    sa.Column('gid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['gid'], ['t_goods.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('t_picture')
    op.drop_table('t_goods_attr')
    # ### end Alembic commands ###
"""empty message

Revision ID: 765e993f5595
Revises: dc06c27a69e6
Create Date: 2023-01-24 16:23:45.747938

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '765e993f5595'
down_revision = 'dc06c27a69e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=True),
    sa.Column('estoque', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###

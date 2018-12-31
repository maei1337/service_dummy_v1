"""update

Revision ID: bb1c5bc39eed
Revises: 
Create Date: 2018-12-31 17:21:08.797442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb1c5bc39eed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product_model', sa.Column('neu', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product_model', 'neu')
    # ### end Alembic commands ###
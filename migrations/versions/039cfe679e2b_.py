"""empty message

Revision ID: 039cfe679e2b
Revises: 72f8826346ec
Create Date: 2018-07-22 13:23:10.661173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '039cfe679e2b'
down_revision = '72f8826346ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('zip_code', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'zip_code')
    # ### end Alembic commands ###

"""empty message

Revision ID: 35731f6f6b6f
Revises: a8f398a3bfbc
Create Date: 2021-04-18 11:18:48.779910

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35731f6f6b6f'
down_revision = 'a8f398a3bfbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ongoing_proj', sa.Column('revised_date', sa.Date(), nullable=True))
    op.add_column('ongoing_proj', sa.Column('revised_sum', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ongoing_proj', 'revised_sum')
    op.drop_column('ongoing_proj', 'revised_date')
    # ### end Alembic commands ###
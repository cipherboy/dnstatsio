"""Add SOA record and grade field

Revision ID: b0a3da6447a1
Revises: 993b64f703aa
Create Date: 2020-11-08 22:04:11.012902

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'b0a3da6447a1'
down_revision = '993b64f703aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('site_runs', sa.Column('j_soa_records', sa.JSON(), nullable=True))
    op.add_column('site_runs', sa.Column('soa_grade', sa.BigInteger(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('site_runs', 'soa_grade')
    op.drop_column('site_runs', 'j_soa_records')
    # ### end Alembic commands ###

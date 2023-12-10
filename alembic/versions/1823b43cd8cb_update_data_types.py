"""update data types

Revision ID: 1823b43cd8cb
Revises: 1b34ea72aab1
Create Date: 2023-12-11 01:01:04.190861

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '1823b43cd8cb'
down_revision: Union[str, None] = '1b34ea72aab1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_products_product_id', table_name='products')
    op.drop_table('products')
    op.drop_index('ix_affiliated_id', table_name='affiliated')
    op.drop_table('affiliated')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('affiliated',
    sa.Column('id', sa.UUID(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('commission_rate', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('commission', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='affiliated_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_affiliated_id', 'affiliated', ['id'], unique=False)
    op.create_table('products',
    sa.Column('product_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('affiliate_id', sa.UUID(), autoincrement=False, nullable=True),
    sa.Column('product_price', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['affiliate_id'], ['affiliated.id'], name='products_affiliate_id_fkey'),
    sa.PrimaryKeyConstraint('product_id', name='products_pkey')
    )
    op.create_index('ix_products_product_id', 'products', ['product_id'], unique=False)
    # ### end Alembic commands ###
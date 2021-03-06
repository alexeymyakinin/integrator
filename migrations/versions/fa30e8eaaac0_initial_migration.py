"""Initial migration

Revision ID: fa30e8eaaac0
Revises: 
Create Date: 2022-03-15 17:08:22.958709

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'fa30e8eaaac0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('sku', sa.String(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('description', sa.String(), nullable=True),
                    sa.Column('external_id', sa.String(), nullable=True),
                    sa.Column('external_vendor', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_item_external_id'), 'item', ['external_id'], unique=True)
    op.create_index(op.f('ix_item_external_vendor'), 'item', ['external_vendor'], unique=False)
    op.create_index(op.f('ix_item_sku'), 'item', ['sku'], unique=True)
    op.create_table('location',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('address', sa.String(), nullable=False),
                    sa.Column('external_id', sa.String(), nullable=True),
                    sa.Column('external_vendor', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_location_external_id'), 'location', ['external_id'], unique=False)
    op.create_index(op.f('ix_location_external_vendor'), 'location', ['external_vendor'], unique=False)
    op.create_table('order',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('price', sa.Integer(), nullable=False),
                    sa.Column('status', sa.Enum('NEW', 'DRAFT', 'SHIPPED', 'CANCELED', 'DELIVERED', name='orderstatus'),
                              nullable=False),
                    sa.Column('external_id', sa.String(), nullable=False),
                    sa.Column('external_number', sa.String(), nullable=False),
                    sa.Column('external_vendor', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_order_external_id'), 'order', ['external_id'], unique=False)
    op.create_index(op.f('ix_order_external_number'), 'order', ['external_number'], unique=False)
    op.create_index(op.f('ix_order_external_vendor'), 'order', ['external_vendor'], unique=False)
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('group', sa.Enum('USER', 'ADMIN', 'MANAGER', name='usergroup'), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('vendor',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(), nullable=False),
                    sa.Column('site', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('name')
                    )
    op.create_table('order_line',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('item', sa.Integer(), nullable=False),
                    sa.Column('order', sa.Integer(), nullable=False),
                    sa.Column('quantity', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['item'], ['item.id'], ),
                    sa.ForeignKeyConstraint(['order'], ['order.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_order_line_item'), 'order_line', ['item'], unique=False)
    op.create_index(op.f('ix_order_line_order'), 'order_line', ['order'], unique=False)
    op.create_table('stock',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('item', sa.Integer(), nullable=False),
                    sa.Column('quantity', sa.Integer(), nullable=False),
                    sa.Column('location', sa.Integer(), nullable=False),
                    sa.Column('external_id', sa.String(), nullable=True),
                    sa.Column('external_number', sa.String(), nullable=True),
                    sa.Column('external_vendor', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['item'], ['item.id'], ),
                    sa.ForeignKeyConstraint(['location'], ['location.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_stock_external_id'), 'stock', ['external_id'], unique=False)
    op.create_index(op.f('ix_stock_external_number'), 'stock', ['external_number'], unique=False)
    op.create_index(op.f('ix_stock_external_vendor'), 'stock', ['external_vendor'], unique=False)
    op.create_index(op.f('ix_stock_item'), 'stock', ['item'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_stock_item'), table_name='stock')
    op.drop_index(op.f('ix_stock_external_vendor'), table_name='stock')
    op.drop_index(op.f('ix_stock_external_number'), table_name='stock')
    op.drop_index(op.f('ix_stock_external_id'), table_name='stock')
    op.drop_table('stock')
    op.drop_index(op.f('ix_order_line_order'), table_name='order_line')
    op.drop_index(op.f('ix_order_line_item'), table_name='order_line')
    op.drop_table('order_line')
    op.drop_table('vendor')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_order_external_vendor'), table_name='order')
    op.drop_index(op.f('ix_order_external_number'), table_name='order')
    op.drop_index(op.f('ix_order_external_id'), table_name='order')
    op.drop_table('order')
    op.drop_index(op.f('ix_location_external_vendor'), table_name='location')
    op.drop_index(op.f('ix_location_external_id'), table_name='location')
    op.drop_table('location')
    op.drop_index(op.f('ix_item_sku'), table_name='item')
    op.drop_index(op.f('ix_item_external_vendor'), table_name='item')
    op.drop_index(op.f('ix_item_external_id'), table_name='item')
    op.drop_table('item')
    # ### end Alembic commands ###

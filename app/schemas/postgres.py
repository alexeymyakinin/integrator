from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, Enum, Numeric
from sqlalchemy.dialects.postgresql import JSONB

from app.schemas.enums import OrderStatus, UserGroup

metadata = MetaData()

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('email', String, nullable=False, unique=True, index=True),
    Column('group', Enum(UserGroup), nullable=False, default=UserGroup.USER),
    Column('password', String, nullable=False, unique=False),
)

item = Table(
    'item',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('sku', String, nullable=False, unique=True, index=True),
    Column('name', String, nullable=False),
    Column('price', Numeric, nullable=False),
    Column('options', JSONB, nullable=True),
    Column('description', String, nullable=True),
    Column('external_id', String, nullable=True, unique=True, index=True),
    Column('external_vendor', Integer, nullable=False, unique=False, index=True),
)

stock = Table(
    'stock',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('item', Integer, ForeignKey('item.id'), nullable=False, index=True),
    Column('quantity', Integer, nullable=False, unique=False),
    Column('location', Integer, ForeignKey('location.id'), nullable=False, unique=False),
    Column('external_id', String, nullable=True, unique=False, index=True),
    Column('external_number', String, nullable=True, unique=False, index=True),
    Column('external_vendor', Integer, nullable=False, unique=False, index=True),
)

order = Table(
    'order',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('price', Integer, nullable=False),
    Column('status', Enum(OrderStatus), nullable=False, default=OrderStatus.NEW),
    Column('external_id', String, nullable=False, unique=False, index=True),
    Column('external_number', String, nullable=False, unique=False, index=True),
    Column('external_vendor', Integer, nullable=False, unique=False, index=True),
)

order_line = Table(
    'order_line',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('item', Integer, ForeignKey('item.id'), nullable=False, index=True),
    Column('order', Integer, ForeignKey('order.id'), nullable=False, index=True),
    Column('price', Numeric, nullable=False),
    Column('quantity', Integer, nullable=False),
)

location = Table(
    'location',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False, unique=False),
    Column('address', String, nullable=False, unique=False),
    Column('external_id', String, nullable=True, unique=False, index=True),
    Column('external_vendor', Integer, nullable=False, unique=False, index=True),
)

vendor = Table(
    'vendor',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False, unique=True),
    Column('site', String, nullable=True, unique=False),
)

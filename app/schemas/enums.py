import enum


class OrderStatus(enum.Enum):
    NEW = 'NEW'
    DRAFT = 'DRAFT'
    SHIPPED = 'SHIPPED'
    CANCELED = 'CANCELED'
    DELIVERED = 'DELIVERED'


class UserGroup(enum.Enum):
    USER = 'USER'
    ADMIN = 'ADMIN'
    MANAGER = 'MANAGER'

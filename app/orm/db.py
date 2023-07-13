from sqlalchemy import (JSON, Column, Enum, ForeignKey, Integer, SmallInteger, String, Table, Numeric, DateTime, Text)

from orm.db_setup import metadata

User = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', Text, nullable=True),
)

User_Detail = Table(
    'user_detail',
    metadata,
    Column('user_id', Integer, primary_key=True),
    Column('name', Text, nullable=True),
    Column('email', Text, nullable=True),
    Column('phone', Integer, nullable=True)
)

Package = Table(
    'package',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', Text, nullable=False),
    Column('partner_id', Integer, nullable=False)
)

Package_Detail = Table(
    'package_detail',
    metadata,
    Column('date_created', Text, nullable=False),
    Column('package_id', Integer, primary_key=True),
    Column('name', Text, nullable=False),
    Column('duration', Integer, nullable=False),
    Column('price', Integer, nullable=False),
    Column('province', Text, nullable=True),
    Column('city', Text, nullable=True),
    Column('location', Text, nullable=True),
    Column('language', Text, Nullable=True)
)

Partner = Table(
    'partner',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', Text, nullable=False)
)

Partner_Detail = Table(
    'partner_detail',
    metadata,
    Column('partner_id', Integer, primary_key=True),
    Column('name', Text, nullable=False),
    Column('ratings', Integer, nullable=True)
)

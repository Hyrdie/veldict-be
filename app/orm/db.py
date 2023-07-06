from sqlalchemy import (JSON, Column, Enum, ForeignKey, Integer, SmallInteger, String, Table, Numeric, DateTime, Text)

from orm.db_setup import metadata

User = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('email', Text, nullable=True),
    Column('phone', Text, nullable=True)
)
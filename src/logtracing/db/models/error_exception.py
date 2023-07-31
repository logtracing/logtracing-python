from main import BaseModel
from log_group import LogGroup
from peewee import DateTimeField, CharField, ForeignKeyField, TextField


class UnknownField(object):
    def __init__(self, *_, **__): pass


class ErrorException(BaseModel):
    flow = CharField(null=True)
    name = CharField(null=True)
    package = CharField(null=True)
    message = CharField(null=True)
    created_at = DateTimeField(column_name='createdAt')
    updated_at = DateTimeField(column_name='updatedAt')
    stack_str = TextField(column_name='stackStr', null=True)
    log_group = ForeignKeyField(column_name='logGroupId', field='id', model=LogGroup, null=True)

    class Meta:
        table_name = 'errorExceptions'

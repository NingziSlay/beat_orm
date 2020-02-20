import sqlalchemy
import orm

__all__ = ["metadata", "BaseOrmModel"]

metadata = sqlalchemy.MetaData()


class BaseOrmModel(orm.Model):
    __abstract__ = True

    id = orm.Integer(primary_key=True)
    created_datetime = orm.DateTime()
    updated_datetime = orm.DateTime()

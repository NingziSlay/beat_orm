import databases
import sqlalchemy
import orm

__all__ = ["metadata", "init_orm", "BaseOrmModel"]

metadata = sqlalchemy.MetaData()
_session = None


def _init(engine):
    global _session
    _session = databases.Database(engine)
    BaseOrmModel.__database__ = _session
    return _session


init_orm = _init


class BaseOrmModel(orm.Model):
    __abstract__ = True

    id = orm.Integer(primary_key=True)
    created_datetime = orm.DateTime()
    updated_datetime = orm.DateTime()

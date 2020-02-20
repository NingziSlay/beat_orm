from .models import BaseOrmModel, metadata
from .db_tools import get_session


def init_orm(engine):
    session = get_session(engine)
    BaseOrmModel.__database__ = session
    return session

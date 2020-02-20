from .models import BaseOrmModel, metadata
from . import db_tools


def init_orm(db_url, debug=False):
    # 创建数据库引擎
    engine = db_tools.get_engine(db_url, debug=debug)
    metadata.create_all(engine)
    # 创建session
    session = db_tools.get_session(engine.url)
    BaseOrmModel.__database__ = session

import databases
import sqlalchemy

from .models import BaseOrmModel, metadata


__all__ = ["init_orm", "session"]


session = None


def init_orm(db_url: str, debug=False) -> None:
    """
    初始化数据库映射，确保要在项目启动之前调用
    :param db_url: url
    :param debug: default = False
    :return: None
    """
    # 创建数据库引擎
    engine = __get_engine(db_url, debug=debug)
    metadata.create_all(engine)
    # 创建session
    global session
    session = __get_session(engine.url)
    BaseOrmModel.__database__ = session


__session = None
__engine = None


def __get_session(url):
    global __session
    if not __session:
        __session = databases.Database(url)
    return __session


def __get_engine(url, debug=False):
    global __engine
    if not __engine:
        __engine = sqlalchemy.create_engine(
            url,
            echo=debug,
            echo_pool=True,
            pool_recycle=3600,
            pool_size=100,
            max_overflow=200,
            pool_timeout=300
        )
    return __engine

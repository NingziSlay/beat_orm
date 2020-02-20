"""数据库相关接口"""
import databases
import sqlalchemy

__all__ = ["get_engine", "get_session", "session"]

_engine = None
_session = None
session = _session


def get_session(url):
    global _session
    if not _session:
        _session = databases.Database(url)
    return _session


def get_engine(url, debug=False):
    global _engine
    if not _engine:
        _engine = sqlalchemy.create_engine(
            url,
            echo=debug,
            echo_pool=True,
            pool_recycle=3600,
            pool_size=100,
            max_overflow=200,
            pool_timeout=300
        )
    return _engine

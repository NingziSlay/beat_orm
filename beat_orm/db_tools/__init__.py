import databases


__all__ = ["get_session", "session"]


_session = None
session = _session


def get_session(engine):
    """获取数据库session
    确保项目启动时一定运行！"""
    global _session
    if not _session:
        _session = databases.Database(engine)
    return _session

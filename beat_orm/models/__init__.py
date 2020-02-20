from typing import Dict, Any

import sqlalchemy
import orm

__all__ = ["metadata", "BaseOrmModel"]

metadata = sqlalchemy.MetaData()


class BaseOrmModel(orm.Model):
    __abstract__ = True

    id = orm.Integer(primary_key=True)
    created_datetime = orm.DateTime()
    updated_datetime = orm.DateTime()

    def get_information(self, *fields, **kwargs) -> Dict[str, Any]:
        """
        一个获取 json 数据的接口
        :param fields: 要获取的字段名
        :param kwargs: json 中字段名需要更换的时候使用

        usage:
            >>> BaseOrmModel().get_information("id", createdDatetime="created_datetime")
        """
        res = dict()
        for field in fields:
            if hasattr(self, field):
                res[field] = getattr(self, field)
        for key, value in kwargs.items():
            if hasattr(self, value):
                res[key] = getattr(self, value)
        return res

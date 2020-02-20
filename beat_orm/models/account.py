import orm

from beat_orm import BaseOrmModel, metadata


class Profile(BaseOrmModel):
    __tablename__ = "profile"
    __metadata__ = metadata
    username = orm.String(max_length=64)


class Account(BaseOrmModel):
    __tablename__ = "account"
    __metadata__ = metadata

    name = orm.String(max_length=64)
    phone = orm.String(max_length=16)
    profile_id = orm.ForeignKey(Profile)

from . import metadata, sqlalchemy

Account = sqlalchemy.Table(
    "account",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String),
    sqlalchemy.Column("phone", sqlalchemy.String),
    sqlalchemy.Column("profile_id", sqlalchemy.ForeignKey("profile.id"))
)


Profile = sqlalchemy.Table(
    "profile",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String)
)

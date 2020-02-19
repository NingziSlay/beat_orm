import sqlalchemy

metadata = sqlalchemy.MetaData()


def init_tables(engine: sqlalchemy.engine.base.Engine):
    metadata.create_all(bind=engine)

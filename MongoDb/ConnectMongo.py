import mongoengine


def connect_db(db_database: str):
    mongoengine.register_connection(alias='DataPoints', name=db_database)
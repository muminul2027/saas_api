#SaaS_API
#HANDLE:    _MUMINUL__ISLAM___


#Code Section->
#Create Session for Database Connection
from app.db.database_engine import db_engine

from sqlalchemy.orm import sessionmaker


#Session
create_session=sessionmaker(autocommit=False,bind=db_engine)


def get_db():
    session_thread=create_session()

    try:
        yield session_thread

    except Exception as databaseSessionError:
        print("Error Happen ",databaseSessionError)

    finally:
        session_thread.close()
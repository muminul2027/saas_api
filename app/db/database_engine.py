#SaaS_API
#HANDLE:    _MUMINUL__ISLAM___



#Code Section->
#Making a Database Engine & Connector

from sqlalchemy import create_engine

from app.db.database_url import database_url

#Create a engine
db_engine=create_engine(database_url,echo=True)


#Create(Write) Table into Database-Service File


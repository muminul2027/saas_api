#SaaS_API
#HANDLE:    _MUMINUL__ISLAM___


#CODE SECTION->
#User Model for Database

from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey

from app.models.base_table import Base



class user_table(Base):
    __tablename__='users'
    #Column
    user_id=Column(Integer,nullable=False,primary_key=True)
    user_pass=Column(String,nullable=False)
    user_role=Column(String,nullable=False)

    user_create_at=Column(DateTime,nullable=True)

    #Team Relation
    user_team=Column(Integer,ForeignKey('teams.team_id'),nullable=True)
    user_team_rel=relationship('team_table',foreign_keys=[user_team])

    

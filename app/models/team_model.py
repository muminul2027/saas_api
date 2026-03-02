#SaaS_API
#HANDLE:    _MUMINUL__ISLAM___



#CODE SECTION->
#Team Model For Database

from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,Table

from app.models.base_table import Base


class team_table(Base):
    __tablename__='teams'
    #Column
    team_id=Column(Integer,nullable=False,primary_key=True)
    team_name=Column(String,nullable=False)

    #Owner Relation
    team_owner=Column(Integer,ForeignKey('users.user_id'),unique=True,nullable=False)
    owner_rel=relationship('user_table',foreign_keys=[team_owner])

 
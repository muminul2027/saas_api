#SaaS_API
#HANDLE:    _MUMINUL__ISLAM___



#CODE SECTION->
#Task Model For Database

from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String,DateTime,Date,ForeignKey

from app.models.base_table import Base


class task_table(Base):
    __tablename__='tasks'
    #Column
    task_id=Column(Integer,primary_key=True,nullable=False)
    task_title=Column(String,nullable=False)
    task_description=Column(String,nullable=False)

    task_status=Column(String,nullable=False)
    task_priority=Column(String,nullable=False)
    task_due=Column(Date,nullable=False)

    task_created_at=Column(DateTime,nullable=True)

    #Link
    task_user=Column(Integer,ForeignKey('users.user_id'),nullable=False)
    task_team=Column(Integer,ForeignKey('teams.team_id'),nullable=False)

    task_user_rel=relationship('user_table',foreign_keys=[task_user])
    task_team_rel=relationship('team_table',foreign_keys=[task_team])



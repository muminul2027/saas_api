#SaaS_API
#HANDLE:    _MUMINUL__ISLAM___


#CODE SECTION->
#Task Schema For Data Validation
        ####Complete

from pydantic import BaseModel,ConfigDict
from datetime import date
from enum import Enum
from typing import Annotated
from fastapi import Query


class task_priority_class(Enum):
    Task_High_Priority="high"
    Task_Mid_Priority="mid"
    Task_Low_Priority="low"
    Task_Optional="optional"

class task_status_class(Enum):
    Task_Wait="waiting"
    Task_Ongoing="ongoing"
    Task_Done="done"
    Task_Cancelled="cancelled"

class task_class(BaseModel):
    task_id : int
    task_title: Annotated[ str, Query(max_length=64) ]
    task_description: Annotated[ str, Query(max_length=256) ]
    
    task_status: str
    task_priority: str
    task_due: date

    #task_created: None | datetime #User Not Supply

    task_user: int  #Foreign Key #done
    task_team: int  #Foreign Key #done

class task_out(BaseModel):
    task_id: int
    task_title: str
    task_status: str


    class Config:
        orm_mode = True


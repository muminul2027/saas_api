#SaaS_API
#HANDLE:    _MUMINUL__ISLAM___


#CODE SECTION->
#User Schema for Data Validation
        ####Complete

from typing import Optional
from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from typing import Optional

user_role_class={
    "Admin": "admin",
    "Supervisor": "supervisor",
    "Member": "member"
}

class user_cLass(BaseModel):
    userID:    int    
    userPass:   str
    userTeam: Optional[int]=None
    #userCreatedAt: Optional[datetime]=None #User Not Supply

class user_sign_in(BaseModel):
    userID: int
    userPass: str

class user_out(BaseModel):
    userID: int
    
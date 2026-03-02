#SaaS_API
#HANDLE:    _MUMINUL__ISLAM___


#CODE SECTION->
#Team Schema for Data Validation
        ####Complete

from pydantic import BaseModel

class team_class(BaseModel):
    teamID: int
    teamName:   str
    teamOwnerID: int #Foreign Key -> User ID

class team_class_out(BaseModel):
    teamID: int

    class Config:
        orm_mode = True


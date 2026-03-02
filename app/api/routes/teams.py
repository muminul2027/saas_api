#SaaS_API
#HANDLE:    _MUMINUL__ISLAM___



#CODE SECTION->
#Team URL
#POST /teams/
#GET /teams/
#POST /teams{id}/members

from app.db.database_session import get_db

from app.service.factory import create_team,get_all_teams,add_member_to_a_team

from app.schemas.user_schema import user_role_class
from app.schemas.team_schema import team_class,team_class_out

from app.api.dependency import get_role

from fastapi import APIRouter,Depends,Request
from sqlalchemy.orm import Session


team_router=APIRouter()

#POST /teams/
@team_router.post('/',response_model=team_class_out)
def add_team(teamIn:team_class, get_request_header: Request, db_in: Session=Depends(get_db)):
    role=get_role(get_request_header)
    create_team(role=role,db_provided=db_in,team_id=teamIn.teamID,team_name=teamIn.teamName,team_owner=teamIn.teamOwnerID)
    return team_class_out(teamID=teamIn.teamID)

#GET /teams/
#For Admin
@team_router.get('/')
def read_team(get_requested_header: Request, db_in: Session=Depends(get_db)):
    role=get_role(get_requested_header)
    all_team_list=get_all_teams(db_provided=db_in,role=role)
    return all_team_list


#POST /teams/{id}/members
@team_router.post('/{team_id}/{member_id}')
def add_member_to_team(team_id,member_id,get_request_header: Request, db_in: Session=Depends(get_db)):
    role=get_role(get_request_header)
    add_member_to_a_team(db_provided=db_in,role=role,team_id=team_id,user_id=member_id)
    return member_id
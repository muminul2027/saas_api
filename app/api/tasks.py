#SaaS_API
#HANDLE:    _MUMINUL__ISLAM___



#CODE SECTION->
#Task URL
#POST /tasks/
#GET /tasks/?status=&page=
#PUT /tasks/{id}
#DELETE /tasks/{id}

from app.api.dependency import get_role
from app.service.factory import create_task,remove_task,update_task,read_task
from app.db.database_session import get_db
from app.schemas.task_schema import task_class,task_out

from fastapi import APIRouter,Request,Depends,Body,Query
from sqlalchemy.orm import Session
from typing import List,Dict

task_router=APIRouter()

#POST /tasks/
@task_router.post('/',response_model=task_out)
def create_a_task(get_task: task_class, get_request:Request, db_in: Session=Depends(get_db)):
    role=get_role(get_request)
    create_task(db_provided=db_in,role=role,
                task_id=get_task.task_id,
                task_title=get_task.task_title,
                task_description=get_task.task_description,
                task_status=get_task.task_status,
                task_priority=get_task.task_priority,
                task_due=get_task.task_due,
                task_user=get_task.task_user,
                task_team=get_task.task_team)
    
    return task_out(task_id=get_task.task_id,
                    task_title=get_task.task_title,
                    task_status=get_task.task_status)


#GET /tasks/{team_id}/?status=&page=
@task_router.get('/{team_id}',response_model=List[task_out])
def read_a_task(team_id,get_request:Request,status:str=Query(...,alias="status"),page:int=Query(1,alias="page"),db_in: Session=Depends(get_db)):
    per_page_record_limit=2
    offset=((page-1)*per_page_record_limit) 

    role=get_role(get_request)
    task_list=read_task(db_provided=db_in,team_id=team_id,task_filter=status,role=role,offset=offset,limit=per_page_record_limit)
    return task_list

#PUT /tasks/{id}
@task_router.put('/{task_id}')
def update_a_task(task_id,get_request:Request,task_status:Dict[str,str]=Body(...),db_in:Session=Depends(get_db)):
    role=get_role(get_request)
    status=task_status.get("task_status")
    task_now=update_task(role=role,db_provided=db_in,task_id=task_id,task_new_status=status)
    return {"Update" :"Success"}


#DELETE /tasks/{id}
@task_router.delete('/{task_id}')
def delete_task(task_id,get_request:Request,db_in: Session=Depends(get_db)):
    role=get_role(get_request)
    if(remove_task(role=role,db_provided=db_in,task_id=task_id)):
        return {"Status":"Deleted"}
    else:
        return {"Status":"Can not Deleted"}
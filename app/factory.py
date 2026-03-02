#TaskForge_API
#HANDLE:    _MUMINUL__ISLAM___



#CODE SECTION->
#Factory of =Create,Remove,Update,Delete = User, Team, Task



from app.db.database_engine import db_engine
from app.db.database_session import get_db

from app.models.base_table import Base
from app.models.task_model import task_table
from app.models.team_model import team_table
from app.models.user_model import user_table

from app.auth.security import verify_incoming_password,make_incoming_password_hashed
from app.schemas.user_schema import user_role_class

from fastapi import HTTPException
from datetime import datetime

    #Create Database
def db_init():
    Base.metadata.create_all(db_engine)
    

    #Registration
def registration(db_provided,user_id,user_pass):
    db_search=db_provided.query(user_table).filter(user_table.user_id==user_id).first()
    if(db_search):
        raise HTTPException(status_code=409,detail="user already in database")
    else:
        db_new_user=user_table(user_id=user_id,user_pass=make_incoming_password_hashed(user_pass),
                              user_create_at=datetime.now(),user_role=user_role_class["Member"])
        db_provided.add(db_new_user)
        db_provided.commit()
        db_provided.refresh(db_new_user)
        return db_new_user
    #Sign_in


def sign_in(db_provided,user_id,user_pass):
    db_search=db_provided.query(user_table).filter(user_table.user_id==user_id).first()
    if(verify_incoming_password(input_database_hash_entry=db_search.user_pass,input_password_text=user_pass)):
        return {"message":"login success"}
    else:
        raise HTTPException(status_code=401,detail="Name and Password not matched")
''' 

    #Create User
def create_user(db_provided,role,user_id,user_name,user_pass,user_role,user_team_instance):
    if (role==user_role_class["Admin"]):
        db_user_row=user_table(user_id=user_id,
                                user_name=user_name,
                                user_pass=make_incoming_password_hashed(user_pass),
                                user_role=user_role,
                                user_team_ref=user_team_instance)
        
        db_provided.add(db_user_row)
        db_provided.commit()
        db_provided.refresh(db_user_row)
        return db_user_row
    else:
        raise HTTPException(status_code=401,detail="For Admin User Only")

'''
    #Read User
def read_user(db_provided,role,user_id):
    if(role==user_role_class["Admin"]):
        db_user_row=db_provided.query(user_table).filter(user_table.user_id==user_id).first()
        if db_user_row:
            return db_user_row
        return False
    else:
        raise HTTPException(status_code=403,detail="Access Denied. For Admin Only")

    #Update User
def update_user(db_provide,role,user_old_id,user_new_id,user_new_role,
                user_new_team):
    if(role==user_role_class["Admin"]):
        db_user_row=db_provide.query(user_table).filter(user_table.user_id==user_old_id).first()
        if(db_user_row):
            db_user_row.user_id=user_new_id
            db_user_row.user_role=user_new_role
            db_provide.commit()
            db_provide.refresh(db_user_row)
            return db_user_row
        else:
            return False
    else:
        raise HTTPException(status_code=403,detail="Permission Denied. For Admin Only")

    #Delete User
def remove_user(db_provided,role,user_id):
    if(role==user_role_class["Admin"]):
        db_user_row=db_provided.query(user_table).filter(user_table.user_id==user_id).first()
        if db_user_row:
            db_provided.delete(db_user_row)
            db_provided.commit()
            return True
        return False
    else:
        raise HTTPException(status_code=403,detail="Permission Error. For Admin Only")
    
    #Get all Users List
def get_all_users(db_provided,role):
    if(role==user_role_class["Admin"]):
        db_user_table=db_provided.query(user_table).all()
        return db_user_table
    else:
        raise HTTPException(status_code=403,detail="For Admin only")

    #Create Team
def create_team(db_provided,role,team_id,team_name,team_owner):
    if(role==user_role_class["Admin"]):
        db_team_row=team_table(team_id=team_id,team_name=team_name,team_owner=team_owner)
        db_provided.add(db_team_row)
        db_provided.commit()
        db_provided.refresh(db_team_row)
        return True
    else:
        raise HTTPException(status_code=403,detail="For Admin only")
    
    #Read Team
def read_team(db_provided,role,team_id,team_owner=None):
    if(role==user_role_class["Admin"]):
        db_team_row=db_provided.query(team_table).filter(team_table.team_id==team_id).first()
        return db_team_row
    
    elif(role==user_role_class["Supervisor"]):
        db_team_row=db_provided.query(team_table).filter(team_table.team_owner==team_owner).first()
        return db_team_row.team_name
    
    else:
        raise HTTPException(status_code=401,detail="Admin or Supervisor Only")


    #Update Team
def update_team(db_provided,role,team_id,team_new_name):
    if(role==user_role_class["Admin"]):
        db_team_row=db_provided.query(team_table).filter(team_table.team_id==team_id).first()
        db_team_row.team_name=team_new_name
        db_provided.commit()
        db_provided.refresh(db_team_row)
        return db_team_row
    else:
        raise HTTPException(status_code=403,detail="For Admin Only")

    #Delete Team
def remove_team(db_provided,role,team_id):
    if(role==user_role_class["Admin"]):
        db_team_row=db_provided.query(team_table).filter(team_table.team_id==team_id).first()
        if db_team_row:
            db_provided.delete(db_team_row)
            db_provided.commit()
            return True
        return False
    else:
        raise HTTPException(status_code=401,detail="For Admin Only")

    #Get all Teams
def get_all_teams(db_provided,role):
    if(role==user_role_class["Admin"]):
        db_team_table=db_provided.query(team_table).all()
        return db_team_table
    else:
        raise HTTPException(status_code=401,detail="For Admin Only")
    
    #Add Team Member
def add_member_to_a_team(db_provided,role,team_id,user_id):
    if(user_role_class["Admin"]==role):
        db_user_row=db_provided.query(user_table).filter(user_table.user_id==user_id).first()
        db_user_row.user_team=team_id
        db_provided.commit()
        db_provided.refresh(db_user_row)
        return True
    else:
        raise HTTPException(status_code=401,detail="For Admin Only")

    #Create Task
def create_task(db_provided,role,task_id,task_title,task_description,
                task_status,task_priority,task_due,task_user,task_team):
    
    if(role==user_role_class["Admin"]):
        db_task_row=task_table(task_id=task_id,task_title=task_title,task_description=task_description,
                                task_status=task_status,task_priority=task_priority,task_due=task_due,
                                task_created_at=datetime.now(),task_user=task_user,task_team=task_team)
        
        db_provided.add(db_task_row)
        db_provided.commit()
        db_provided.refresh(db_task_row)
        return True  
    else:
        raise HTTPException(status_code=401,detail="For Admin Only")
    
    #Read Task
def read_task(db_provided,team_id,task_filter,role,offset=0,limit=10):  #Pagination
        if(role=="user_role_class['Supervisor']" or role==user_role_class["Admin"]):
            db_task_row_team_filter=db_provided.query(task_table).filter(task_table.task_team==team_id)
            db_task_row_status_filer=db_task_row_team_filter.filter(task_table.task_status==task_filter)
            db_task_row_pagination=db_task_row_status_filer.offset(offset).limit(limit).all()
            return db_task_row_pagination
        else:
            raise HTTPException(status_code=401,detail="Supervisor or Admin Only")

    #Update Task
def update_task(db_provided,role,task_id,task_new_status):
    if(role==user_role_class["Supervisor"] or role==user_role_class["Admin"]):
        db_task_row=db_provided.query(task_table).filter(task_table.task_id==task_id).first()
        if(db_task_row):
            db_task_row.task_status=task_new_status
            db_provided.commit()
            db_provided.refresh(db_task_row)
            return True
    else:
        raise HTTPException(status_code=401,detail="Supervisor or Admin Only")
    
    #Delete Task
def remove_task(db_provided,role,task_id):

    if(role==user_role_class["Admin"]):
        db_task_row=db_provided.query(task_table).filter(task_table.task_id==task_id).first()
        if db_task_row:
            db_provided.delete(db_task_row)
            db_provided.commit()
            return True
        return False
    else:
        raise HTTPException(status_code=401,detail="For Admin Only")

    #Get all Tasks List
def get_all_tasks(db_provided,role):
    if(role==user_role_class["Admin"]):
        db_task_table=db_provided.query(task_table).all()
        return db_task_table
    raise HTTPException(status_code=401,detail="For Admin Only")

#DEBUG


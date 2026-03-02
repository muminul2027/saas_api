
########################################################

#PROJECT_NAME:  SaaS_API
#PROJECT_TYPE:  PERSONAL/PORTFOLIO

#OWNER/AUTHOR:  MUMINUL ISLAM
#HANDLE:        _MUMINUL__ISLAM___

#LICENSE:   PROPRIETARY
#PURPOSE:   JOB_APPLICATION_EVALUATION

########################################################
##ADDITIONAL_INFORMATION

##PRODUCT_GOAL:    PRODUCTION_GRADE_MVP_FOR_PORTFOLIO
##ALLOCATED_TIME:    10[DAYS]

##STATUS:   COMPLETED

##GitHub: https://github.com/muminul2027/saas_api
#########################################################


#ACTUAL CODE-   START
from fastapi import FastAPI
from pydantic import BaseModel

from app.service.factory import db_init

from app.api.routes.auth import auth_router
from app.api.routes.tasks import task_router
from app.api.routes.teams import team_router

#Start the Database
db_init()

#Name the WebApp + Create the WebApp Object
web_app=FastAPI()


#Include router to main file
web_app.include_router(auth_router,prefix="/auth",tags=["auth"])
web_app.include_router(task_router,prefix="/tasks",tags=["task"])
web_app.include_router(team_router,prefix="/teams",tags=["team"])

#Welcom screen
welcome_data={
    "Welcome":"Welcome To SaaS_API",
    "Task_Priority":"high,mid,low,optional",
    "Task_Status":"waiting,ongoing,done,cancelled"
}

#Base URL
@web_app.get('/')
def welcome():
    return welcome_data

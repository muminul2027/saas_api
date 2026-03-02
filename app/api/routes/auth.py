#SaaS_API
#HANDLE:    _MUMINUL__ISLAM___



#CODE SECTION->
#User Authorization URL (Input & Output Method)=JSON Format
#POST    /auth/register
#POST    /auth/login

from app.schemas.user_schema import user_cLass,user_sign_in,user_out,user_role_class
from app.service.factory import registration,sign_in
from app.auth.token import generate_token,decode_token
from app.db.database_session import get_db

from fastapi import APIRouter,Request,Response,Depends
from sqlalchemy.orm import Session

auth_router=APIRouter()

#POST /auth/register
@auth_router.post('/register',response_model=user_out)
def register_a_user(userIn:user_cLass,response:Response,db_in:Session=Depends(get_db)):
    if(registration(db_in,userIn.userID,userIn.userPass)):
        token=generate_token(userIn.userID,user_role_class["Member"])
        response.set_cookie(key="access_token",value=token,httponly=True)
        return user_out(userID=userIn.userID)
    else:
        return {"status":"falied registration"}

#POST /auth/login
@auth_router.post('/login',response_model=user_out)
def login_a_user(userIn: user_sign_in,response:Response,db_in:Session=Depends(get_db)):
    if(sign_in(db_provided=db_in,user_id=userIn.userID,user_pass=userIn.userPass)):
        token=generate_token(userIn.userID,user_role_class["Member"])
        response.set_cookie(key="access_token",value=token,httponly=True)
        return user_out(userID=userIn.userID)
    else:
        return {"status":"failed sign in"}

#POST /auth/login/admin
#Special Kind of Routing, Dont Use in Production Server
@auth_router.get('/admin')
def login_admin(response:Response):
        token=generate_token("admin","admin")
        response.set_cookie(key="access_token",value=token,httponly=True)
        return {"status":"welcome admin"}


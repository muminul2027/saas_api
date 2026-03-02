#SaaS_API
#HANDLE:    _MUMINUL_ISLAM___


#CODE SECTION->
#DECODE JWT and GET ROLE

from fastapi import Request

from app.auth.token import get_role_from_token

def get_role(incomingRequest:Request):
    cookie_data=incomingRequest.cookies.get('access_token')

    user_role=get_role_from_token(cookie_data)

    return user_role
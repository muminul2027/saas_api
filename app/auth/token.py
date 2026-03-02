#SaaS_API
#HANDLE:    _MUMINUL__ISLAM___



#CODE SECTION->
#JWT Lib- PyJWT
import jwt
from datetime import datetime,timezone,timedelta

from app.config import private_key,public_Key

SECRET_KEY=private_key
PUBLIC_KEY=public_Key

#Payload

#Generate Token
def generate_token(user_id,user_role):
    payload={
        'user_id':user_id,
        'user_role':user_role,
        'iat':datetime.now(timezone.utc),
        'exp':datetime.now(timezone.utc)+timedelta(minutes=3)
        
    }
    token=jwt.encode(payload,SECRET_KEY,algorithm='ES256')
    return token

#Decode Token
def decode_token(token):
    try:
        plain_data=jwt.decode(token,PUBLIC_KEY,algorithms='ES256')
    except jwt.ExpiredSignatureError:
        return "Token has expired"
    except jwt.InvalidTokenError:
        return "Invalid Token"
    return plain_data

#Decode Token Role
def get_role_from_token(token):
    try:
        plain_data=jwt.decode(token,PUBLIC_KEY,algorithms='ES256')
    except jwt.ExpiredSignatureError as e:
        print(e)
        return False
    except jwt.InvalidTokenError as e:
        print(e)
        return False
    return plain_data["user_role"]


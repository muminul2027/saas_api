#SaaS_API
#HANDLE:    _MUMINUL__ISLAM___



#CODE SECTION->

#Password Hash Lib- Argon2 Wrapper
from argon2 import PasswordHasher

#Global hash function
pass_hasher_method=PasswordHasher(
    time_cost=4,
    memory_cost=102400,
    parallelism=2
)

#Let Hash Password
def make_incoming_password_hashed(input_plain_text):
    hashed_output=pass_hasher_method.hash(input_plain_text)
    return hashed_output

#Let Verify Password
def verify_incoming_password(input_database_hash_entry,input_password_text):
    try:
        is_password_same=pass_hasher_method.verify(input_database_hash_entry,
                                                   input_password_text)
        
        return True    #True or Raise Exception for False
    except:
        return False

    #JWT Token

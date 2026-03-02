#SaaS_API
#HANDLE:    _MUMINUL__ISLAM___



#CODE SECTION->

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

#Generate Key
private_key=ec.generate_private_key(ec.SECP256R1())

public_Key=private_key.public_key()

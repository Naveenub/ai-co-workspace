from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

api_key_header = APIKeyHeader(name="Authorization", auto_error=False)

def verify_api_key(api_key: str = Security(api_key_header)):
    if api_key != "supersecret":  # Replace with proper auth
        raise HTTPException(status_code=401, detail="Unauthorized")

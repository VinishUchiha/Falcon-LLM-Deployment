from fastapi.security.api_key import APIKeyHeader
from fastapi import Security, HTTPException, Depends
from starlette.status import HTTP_403_FORBIDDEN
from api_key_utils import validate_key

api_key_header = APIKeyHeader(name="api_key", auto_error=False)

async def get_username(api_key_header: str = Security(api_key_header)):
    flag, username = validate_key(api_key_header)
    if flag:
        return username
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )
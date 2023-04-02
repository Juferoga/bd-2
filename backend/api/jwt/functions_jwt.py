from jwt import encode, decode
from datetime import datetime, timedelta
from os import getenv
from fastapi.responses import JSONResponse

def expire_date(days: int):
    date = datetime.now()
    new_date = date + timedelta(days)
    return new_date

def write_token(data: dict):
    token = encode(payload={**data, "exp": expire_date(2)}, key=getenv("SECRET"), algorithm="HS256")
    return token

def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv("SECRET"), algorithm="HS256")
        decode(token, key=getenv("SECRET"), algorithm="HS256")
    except:
        return JSONResponse(content={"message": "Invalid token"}, status_code=401)
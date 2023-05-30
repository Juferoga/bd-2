from pydantic import BaseModel
from typing import Any

class ApiResponse(BaseModel):
    status: str
    data: Any or None = None
    message: str

class InternalResponse(BaseModel):
    success: bool
    content: Any or None = None
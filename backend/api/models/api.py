from pydantic import BaseModel
from typing import Any, Optional

class ApiResponse(BaseModel):
    status: str
    data: Optional[Any] = None
    message: str

class InternalResponse(BaseModel):
    success: bool
    content: Any or None = None
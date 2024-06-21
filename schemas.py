from typing import Optional

from pydantic import BaseModel, ConfigDict


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class STask(STaskAdd):
    model_config = ConfigDict(from_attributes=True)

    id: int


class STaskId(BaseModel):
    ok: bool = True
    id: int

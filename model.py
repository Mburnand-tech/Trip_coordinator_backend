from pydantic import BaseModel
from typing import Union, List

class User(BaseModel):
    group_id: str
    username: Union[ List[str], None] = None
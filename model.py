from pydantic import BaseModel
from typing import Union, List

class User(BaseModel):
    group_name: str
    group_members: List[str]
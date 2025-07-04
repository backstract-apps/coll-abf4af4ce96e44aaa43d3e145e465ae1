from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class User1(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: str
    password: str


class ReadUser1(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: str
    password: str
    class Config:
        from_attributes = True


class User2(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: str


class ReadUser2(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: str
    class Config:
        from_attributes = True



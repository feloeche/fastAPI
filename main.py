#Python
from uuid import UUID
from datetime import date
from typing import Optional

# Pydantic
from pydantic import BaseModel

# FastAPI
from fastapi import FastAPI
from pydantic.networks import EmailStr
from pydantic import Field


app = FastAPI()


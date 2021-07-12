from datetime import datetime
from pydantic import BaseModel, Field, validator
from typing import Optional


class DomainQuery(BaseModel):
    domain: str = Field(min_length=1)
    group: Optional[str] = Field(regex=r"^[A-Za-z\-]+$")


class EntryQuery(DomainQuery):
    title: str = Field(regex=r"^[A-Za-z\-]+$")
    group: str = Field(regex=r"^[A-Za-z\-]+$")


class EntryCreation(EntryQuery):
    definitions: list[str] = Field(min_length=1)
    translations: Optional[list[str]] = Field(default=[])
    created_at: Optional[datetime] = Field(default=None)
    image: Optional[str] = Field(
        regex=r"^data:image/.*;base64,[A-Za-z0-9\+/]+={0,2}$",
        max_length=2_700_20,
    )

    @validator("created_at", pre=True, always=True)
    def set_ts_now(cls, v):
        return v or datetime.utcnow()


class EntryUpdate(BaseModel):
    title: Optional[str] = Field(regex=r"^[A-Za-z\-]+$")
    group: Optional[str] = Field(regex=r"^[A-Za-z\-]+$")
    definitions: Optional[list[str]] = Field(min_length=1)
    translations: Optional[list[str]] = Field(min_length=1)

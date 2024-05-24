from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel, Field


class Base(DeclarativeBase):
    pass


class EmployeeTable(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)


class Employee(BaseModel):
    id: int
    name: str
    email: str


class EmployeeCreate(BaseModel):
    name: str = Field(max_length=255, examples=["Jane Doe", "John Doe"])
    email: str = Field(max_length=255, examples=["janedoe@example.com", "johndoe@example.com"])

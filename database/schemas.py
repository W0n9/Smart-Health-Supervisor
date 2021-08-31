# 此文件用来规范数据库表里的数据
from datetime import datetime

# from typing import List, Optional

from pydantic import BaseModel, Field


class DoctorBase(BaseModel):
    doctor_name: str = Field(..., max_length=20)
    hospital_id: int

    class Config:
        orm_mode = True


class DoctorCreate(DoctorBase):
    pass


class DoctorReturn(DoctorBase):
    doctor_id: int


class HospitalBase(BaseModel):
    hospital_name: str = Field(..., max_length=20)

    class Config:
        orm_mode = True


class HospitalCreate(HospitalBase):
    pass


class HospitalReturn(HospitalCreate):
    hospital_id: int


# class Employee(BaseModel):
#     doctor_id:int
#     hospital_id:int

#     class Config:
#         orm_mode = True


class JournalBase(BaseModel):
    # 在请求和响应中将表示为 ISO 8601 格式的 str ，比如: 2008-09-15T15:53:00+05:00.
    timestamp: datetime

    class Config:
        orm_mode = True


class JournalCreate(JournalBase):
    current_doctor_id: int
    current_hospital_id: int


class JournalReturn(JournalCreate):
    pass

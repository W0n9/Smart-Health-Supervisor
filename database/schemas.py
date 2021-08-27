# 此文件用来规范数据库表里的数据
from typing import Any, List, Optional

from pydantic import BaseModel

class DoctorCreate(BaseModel):
    doctor_name:str
    hospital_id:int

    class Config:
        orm_mode = True

class DoctorReturn(DoctorCreate):
    doctor_id:int

class HospitalCreate(BaseModel):
    hospital_name:str

    class Config:
        orm_mode = True

class HospitalReturn(HospitalCreate):
    hospital_id:int

# class Employee(BaseModel):
#     doctor_id:int
#     hospital_id:int

#     class Config:
#         orm_mode = True

class Journal(BaseModel):
    timestamp:Any
    current_doctor_id:int
    current_hospital_id:int

    class Config:
        orm_mode = True


# 此文件用来定义数据库表结构
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime

# from sqlalchemy.orm import backref, relationship

from .database import Base


class Doctor(Base):

    __tablename__ = "doctors"

    doctor_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    doctor_name = Column(String, index=True)
    hospital_id = Column(Integer, index=True, autoincrement=True)
    # all_doctor_name = relationship("Employee", back_populates="doctor_names")


class Hospital(Base):

    __tablename__ = "hospitals"

    hospital_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    hospital_name = Column(String, index=True)
    # all_hospital_name = relationship("Employee",
    #                                  back_populates="hospital_names")


# class Employee(Base):

#     __tablename__ = "employees"

#     doctor_id = Column(Integer,
#                        ForeignKey("doctors.doctor_id"),
#                        primary_key=True)
#     hospital_id = Column(Integer, ForeignKey("hospitals.hospital_id"))
#     doctor_names = relationship("Doctor", back_populates="all_doctor_name")
#     hospital_names = relationship("Hospital",
#                                   back_populates="all_hospital_name")


class Journal(Base):

    __tablename__ = "journals"

    timestamp = Column(DateTime, primary_key=True, index=True)
    current_doctor_id = Column(Integer, index=True)
    current_hospital_id = Column(Integer, index=True)
    # docter_name=relationship("Hospital",
    #                               backref="all_hospital_name")

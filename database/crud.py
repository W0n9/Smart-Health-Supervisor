import datetime
from sqlalchemy.orm import Session

from . import models, schemas


## 医生相关操作
def get_doctor(db: Session, id: int):
    return db.query(models.Doctor).filter(models.Doctor.doctor_id == id).first()


def validate_doctor(db: Session, doctor_id: int, hospital_id: int):
    conds = [
        models.Doctor.doctor_id == doctor_id,
        models.Doctor.hospital_id == hospital_id,
    ]
    return db.query(models.Doctor).filter(*conds).first()


def get_doctor_by_name(db: Session, name: str):
    return db.query(models.Doctor).filter(models.Doctor.doctor_name == name).all()


def get_doctor_by_hospital(db: Session, id: int):
    return db.query(models.Doctor).filter(models.Doctor.hospital_id == id).all()


def get_doctor_by_hospital_and_name(db: Session, hospital_id: int, doctor_name: str):
    conds = [
        models.Doctor.hospital_id == hospital_id,
        models.Doctor.doctor_name == doctor_name,
    ]
    return db.query(models.Doctor).filter(*conds).first()


def get_doctors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Doctor).offset(skip).limit(limit).all()


def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


## 医院相关操作
def get_hospital(db: Session, id: int):
    return db.query(models.Hospital).filter(models.Hospital.hospital_id == id).first()


def get_hospital_by_name(db: Session, name: str):
    return (
        db.query(models.Hospital).filter(models.Hospital.hospital_name == name).first()
    )


def get_hospitals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Hospital).offset(skip).limit(limit).all()


def create_hospital(db: Session, hospital: schemas.HospitalCreate):
    db_hospital = models.Hospital(**hospital.dict())
    db.add(db_hospital)
    db.commit()
    db.refresh(db_hospital)
    return db_hospital


## 日志相关操作
def get_journal_by_day(
    db: Session, date: datetime.date, skip: int = 0, limit: int = 100
):
    # today_begin=datetime.datetime.strptime(date,"%Y-%m-%d").date()
    today_begin = date
    today_end = today_begin + datetime.timedelta(1)
    conds = [
        models.Journal.timestamp > today_begin,
        models.Journal.timestamp < today_end,
    ]
    return db.query(models.Journal).filter(*conds).offset(skip).limit(limit).all()


def get_journal_by_datetime(db: Session, time: datetime.datetime):
    return db.query(models.Journal).filter(models.Journal.timestamp == time).first()


def create_journal(db: Session, journal: schemas.JournalCreate):
    db_journal = models.Journal(**journal.dict())
    db.add(db_journal)
    db.commit()
    db.refresh(db_journal)
    return db_journal

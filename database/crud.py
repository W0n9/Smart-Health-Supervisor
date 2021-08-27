from sqlalchemy.orm import Session

from . import models, schemas

## 医生相关操作
def get_doctor(db: Session, id: int):
    return db.query(models.Doctor).filter(models.Doctor.doctor_id == id).first()

def get_doctor_by_name(db: Session, name: str):
    return db.query(models.Doctor).filter(models.Doctor.doctor_name == name).all()

def get_doctor_by_hospital(db: Session, id: int):
    return db.query(models.Doctor).filter(models.Doctor.hospital_id == id).all()

def get_doctors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Doctor).offset(skip).limit(limit).all()

def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(doctor_name=doctor.doctor_name,hospital_id=doctor.hospital_id)
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor


## 医院相关操作
def get_hospital(db: Session, id: int):
    return db.query(models.Hospital).filter(models.Hospital.hospital_id == id).first()

def get_hospital_by_name(db: Session, name: str):
    return db.query(models.Hospital).filter(models.Hospital.hospital_name == name).first()

def get_hospitals(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Hospital).offset(skip).limit(limit).all()

def create_hospital(db: Session, hospital: schemas.HospitalCreate):
    db_hospital = models.Hospital(hospital_name=hospital.hospital_name)
    db.add(db_hospital)
    db.commit()
    db.refresh(db_hospital)
    return db_hospital


## 日志相关操作
def get_journal_by_time(db: Session, skip: int = 0, limit: int = 100):
    pass

def create_journal(db:Session):
    pass


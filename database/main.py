from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        # 按需连接数据库，防止冲突
        yield db
    finally:
        db.close()


@app.get('/')
async def get_root():
    return {'message': 'Welcome to the Smart Health Supervisor API'}


# 医生信息
@app.get("/doctors/", response_model=List[schemas.DoctorReturn],tags=["Doctor"])
async def read_doctors(skip: int = 0,
                       limit: int = 100,
                       db: Session = Depends(get_db)):
    doctors = crud.get_doctors(db, skip=skip, limit=limit)
    return doctors


@app.post("/doctors/",
          response_model=schemas.DoctorReturn,
          status_code=status.HTTP_201_CREATED,tags=["Doctor"])
async def create_doctor(doctor: schemas.DoctorCreate,
                        db: Session = Depends(get_db)):
    db_doctor=crud.get_doctor_by_hospital_and_name(db,**doctor.dict())
    if db_doctor:
        raise HTTPException(status_code=400,
                            detail="Doctor already registered")
    return crud.create_doctor(db, doctor)


# 医院信息
@app.get("/hospitals/", response_model=List[schemas.HospitalReturn],tags=["Hospital"])
async def read_hospitals(skip: int = 0,
                         limit: int = 100,
                         db: Session = Depends(get_db)):
    hospitals = crud.get_hospitals(db, skip=skip, limit=limit)
    return hospitals


## 此处创建hospital时自动分配id，创建完返回id+名字
@app.post("/hospitals/",
          response_model=schemas.HospitalReturn,
          status_code=status.HTTP_201_CREATED,tags=["Hospital"])
async def create_hospital(hospital: schemas.HospitalCreate,
                          db: Session = Depends(get_db)):
    db_hospital = crud.get_hospital_by_name(db, hospital.hospital_name)
    if db_hospital:
        raise HTTPException(status_code=400,
                            detail="Hospital already registered")
    return crud.create_hospital(db, hospital)


# 日志信息
@app.get("/journals/", response_model=List[schemas.Journal],tags=["Journal"])
async def read_journal():
    pass

@app.post("/journals/", response_model=schemas.Journal,tags=["Journal"])
async def create_journal():
    pass
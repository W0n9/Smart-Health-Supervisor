# 数据库表结构

## journals
|字段名|类型|备注|
|-|-|-|
|timestamp|DATETIME|医生出镜的时间戳，主键|
|current_doctor_id|INT|出镜的医生的唯一ID|
|current_hospital_id|INT|出镜的医院的ID|
---
## doctors
|字段名|类型|备注|
|-|-|-|
|doctor_id|INT|医生的唯一ID，主键,自增|
|doctor_name|VARCHAR(20)|医生的名字|
|hospital_id|INT|医院的唯一ID,外键hospitals.hospital_id ON DELETE CASCADE|
---
## hospitals
|字段名|类型|备注|
|-|-|-|
|hospital_id|INT|医院的唯一ID，主键,自增|
|hospital_name|VARCHAR(20)|医院的名字|
<!-- ---
## employees
|字段名|类型|备注|
|-|-|-|
|doctor_id|INT|医生的唯一ID，主键，外键doctors.doctor_id ON DELETE CASCADE|
|hospital_id|INT|医院的ID，外键hospitals.hospital_id ON DELETE CASCADE| -->
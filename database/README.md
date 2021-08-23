# 数据库表结构

## journal
|字段名|类型|备注|
|-|-|-|
|time|TIMESTAMP|医生出镜的时间戳，主键|
|current_doctor_id|INT|出镜的医生的唯一ID|
|current_hospital_id|INT|出镜的医院的ID|
---
## doctor
|字段名|类型|备注|
|-|-|-|
|doctor_id|INT|医生的唯一ID，主键|
|doctor_name|VARCHAR(20)|医生的名字|
---
## hospital
|字段名|类型|备注|
|-|-|-|
|hospital_id|INT|医院的唯一ID，主键|
|hospital_name|VARCHAR(20)|医院的名字|
---
## employee
|字段名|类型|备注|
|-|-|-|
|doctor_id|INT|医生的唯一ID，主键，外键ON DELETE CASCADE|
|hospital_id|INT|医院的ID，外键ON DELETE CASCADE|
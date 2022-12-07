from fastapi import FastAPI,Path
from models import *

app=FastAPI()

students=[
  {
    "usn": "01jst20cs036",
    "sr_no": "202110",
    "name": "Chandan",
    "dob": "07062002",
    "sem": "5",
    "section": "B5",
    "courses": [
      "20cs510",
      "20cs520",
      "20cs530",
      "20cs540",
      "20cs552"
    ]
  },
  {
    "usn": "01jst20cs150",
    "sr_no": "206007",
    "name": "Shivam Menda",
    "dob": "02032002",
    "sem": "5",
    "section": "B5",
    "courses": [
      "20cs510",
      "20cs540",
      "20cs552"
    ]
  },
  {
    "usn": "01jst20cs072",
    "sr_no": "202062",
    "name": "Kartik Punit Sureja",
    "dob": "02122002",
    "sem": "5",
    "section": "B5",
    "courses": [
      "20cs510",
      "20cs520",
      "20cs530",
      "20cs540",
      "20cs552"
    ]
  },
  {
    "usn": "01jst20cs013",
    "sr_no": "202061",
    "name": "Akash N",
    "dob": "22032002",
    "sem": "5",
    "section": "B5",
    "courses": [
      "20cs510",
      "20cs520",
      "20cs540",
      "20cs552"
    ]
  },
  {
    "usn": "01jst20cs110",
    "sr_no": "202060",
    "name": "Nakul MK",
    "dob": "01012002",
    "sem": "5",
    "section": "B5",
    "courses": [
      "20cs510",
      "20cs520",
      "20cs530",
      "20cs540",
      "20cs552"
    ]
  }
]


    

@app.get('/')
def index():
    return {"name":"My first API"}

@app.get('/get-students')
def get_students():
    return students

@app.get('/get-student/{usn}')
def get_student(usn:str=Path(None,description="A unique key to identify the student")):
    for i in students:
        if i['usn']==usn:
            return i
    return "Student doesn't exist"

@app.post('/create-student/{usn}')
def create_student(*,usn:str=Path(None,description="A unique key to identify the student"),student:Student):
    for i in students:
        if i['usn']==usn:
            return {"message":"Student data already exists"}
        else:
            students.append(student)
        return student

@app.patch('/update-student/{usn}')
def update_student(*,usn:str=Path(None,description="A unique key to identify the student"),updateStudent:UpdateStudent):
  for i in students:
    if i['usn']==usn:
      if updateStudent.name!=None:
        i['name']=updateStudent.name
      if updateStudent.dob!=None:
        i['dob']=updateStudent.dob
      if updateStudent.sr_no!=None:
        i['sr_no']=updateStudent.sr_no
      if updateStudent.sem!=None:
        i['sem']=updateStudent.sem
      if updateStudent.section!=None:
        i['section']=updateStudent.section
      if updateStudent.courses!=None:
        i['courses']=updateStudent.courses
      return i
  
  return {"message":"student data doesn't exist"}
      
@app.put('/alter-student/{usn}')
def alter_student(*,usn:str=Path(None,description="A unique key to identify the student"),student:Student):
  for i in students:
    if i['usn']==usn:
      i['usn']=student.usn
      i['sr_no']=student.sr_no
      i['name']=student.name
      i['dob']=student.dob
      i['sem']=student.sem
      i['section']=student.section
      i['courses']=student.courses
      return i  
  return {"message":"student data doesn't exist"}
#to run : uvicorn myapi:app --reload
#Add data
# {
#     "usn": "01jst20cs038",
#     "sr_no": "200027",
#     "name": "Brahma Keerthi",
#     "dob": "07062002",
#     "sem": "5",
#     "section": "B5",
#     "courses": [
#       "20cs510",
#       "20cs520",
#       "20cs540",
#       "20cs552"
#     ]
#   }
#Update student data
# {
#     "usn": "01jst20cs013",
#     "sr_no": "202037",
#     "name": "Akash N",
#     "dob": "22032002",
#     "sem": "5",
#     "section": "B5",
#     "courses": [
#       "20cs510",
#       "20cs520",
#       "20cs540",
#       "20cs552"
#     ]
#   }
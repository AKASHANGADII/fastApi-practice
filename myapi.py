from fastapi import FastAPI,Path
from pydantic import BaseModel

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

class Student(BaseModel):
    usn: str
    sr_no: str
    name: str
    dob: str
    sem: str
    section: str
    courses: list[str]
    

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
#to run : uvicorn myapi:app --reload
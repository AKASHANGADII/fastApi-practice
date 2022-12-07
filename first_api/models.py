
from typing import Optional
from pydantic import BaseModel


class Student(BaseModel):
    usn: str
    sr_no: str
    name: str
    dob: str
    sem: str
    section: str
    courses: list[str]
    
class UpdateStudent(BaseModel):
  usn: Optional[str]=None
  sr_no: Optional[str]=None
  name: Optional[str]=None
  dob: Optional[str]=None
  sem: Optional[str]=None
  section: Optional[str]=None
  courses: Optional[list[str]]=None
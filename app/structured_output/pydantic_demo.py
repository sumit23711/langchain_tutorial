from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name : str
    age : Optional[int] = None
    email : EmailStr
    cgpa : float = Field(gt=0, lt=10)

new_student = {'name': 'sumit', 'age' : 32, 'email': 'abc@gmail.com', 'cgpa': 9}

student = Student(**new_student)


student_dict = student.model_dump
student_json = student.model_dump_json
print(student)
print(student_dict)
print(student_json)
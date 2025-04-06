from fastapi import FastAPI
from pydantic import BaseModel,EmailStr

app = FastAPI()

class EmployeeBase(BaseModel):
    empid:int
    name : str
    email : EmailStr

class EmployeeIn(EmployeeBase):
    password: str

class EmployeeOut(EmployeeBase):
    pass

class EmployeeDB(EmployeeBase):
     hashed_password: str

def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password

def fake_save_user(user_in: EmployeeIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = EmployeeDB(**user_in.model_dump(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db

@app.post("/user/",response_model=EmployeeDB)
async def create_user(user_in:EmployeeIn):
    user_saved=fake_save_user(user_in) #saving the like in a database
    return user_saved

from fastapi import FastAPI,HTTPException,status
from fast_api.model import Users

app = FastAPI()

users = [Users(id=1,name='luffy',email='luffy@gmail.com',password='luffy123'),
         Users(id=2,name='zoro',email='zoro@gmail.com',password='zoro123'),
         Users(id=3,name='sanji',email='sanji@gmail.com',password='sanji123')]

@app.get('/')
def view():
    return users

@app.post('/add_user')
def add(adduser:Users):
    match_id = [u for u in users if u.id == adduser.id]
    if match_id:
        raise HTTPException(400,detail='Already exist')
    users.append(adduser)
    return {'message':'successfully added'}
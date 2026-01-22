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

@app.post('/update_user')
def update(updateuser:Users):
    for u in users:
        if updateuser.id == u.id:
            u.id = updateuser.id
            u.name = updateuser.name
            u.email = updateuser.email
            u.password = updateuser.password
            return {'message': 'update succefully'}
    raise HTTPException(404, detail='user not exist')

@app.post('/delete_user')
def delete(userid:Users):
    for u in users:
        if userid.id == u.id:
            users.remove(u)
            return {'message': 'delete successfully'}

    raise HTTPException(404,detail='user not found')


from fastapi import FastAPI
from fast_api.model import Users

app = FastAPI()

users = [Users(id=1234,name='luffy',email='luffy@gmail.com',password='luffy1'),
         Users(id=12345,name='zoro',email='zoro@gmail.com',password='zoro1')
         ]

@app.get('/')
def show():
    return users

from fastapi import FastAPI
from api.routers import task, done

app = FastAPI() #FastAPI 인스턴스

"""@app.get("/hello") #get 방식 경로 async로 비동기
async def hello():
    return {"message": "hello world!"}"""


app.include_router(task.router) #내장 메서드 include_router
app.include_router(done.router)
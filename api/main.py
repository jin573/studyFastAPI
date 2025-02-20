from fastapi import FastAPI

app = FastAPI() #FastAPI 인스턴스

@app.get("/hello") #get 방식 경로 async로 비동기
async def hello():
    return {"message": "hello world!"}

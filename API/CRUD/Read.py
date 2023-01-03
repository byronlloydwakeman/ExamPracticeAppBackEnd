from fastapi import FastAPI
from Database.DBConnection import DBConnection
from Database.CRUD.Read import Read
from Database.CRUD.Read import ReadAll

app = FastAPI()


@app.get("/ReadOne/{search}/{value}")
async def read_one(search, value):
    try:
        conn = DBConnection("mongodb://localhost:27017", "exampracticeapp", "pythonexamquestions")
        return Read(conn, {search : value})
    except Exception as e:
        return {"Error": e.__str__()}



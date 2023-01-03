from Database.DBConnection import DBConnection
from Database.CRUD.Read import ReadAll


@app.get("/ReadAll/{search}/{value}")
async def read_all(search, value):
    try:
        conn = DBConnection("mongodb://localhost:27017", "exampracticeapp", "pythonexamquestions")
        return ReadAll(conn, {search : value})
    except Exception as e:
        return {"Error": e.__str__()}
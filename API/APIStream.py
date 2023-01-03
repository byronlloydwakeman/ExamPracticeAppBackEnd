from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import List

from ConvertAPIToDB import ConvertAPIModelToDBModel
from ConvertAPIToDB import ConvertAPIModelListToDBModelList

from Database.DBConnection import DBConnection
from Database.CRUD.Read import Read
from Database.CRUD.Read import ReadAll
from Database.CRUD.Create import Create
from Database.CRUD.Create import CreateMany
from Database.CRUD.Update import UpdateOne
from Database.CRUD.Delete import Delete
from Database.CRUD.Delete import DeleteMany

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class DBConnectionData(BaseModel):
    hostName: str
    databaseName: str
    collectionName: str


class APIPracticeQuestionModel(BaseModel):
    dbConnectionData: DBConnectionData
    question: str
    correctAnswer: str
    answers: List[str]
    explanation: str
    knowledgeArea: str


class APIPracticeQuestionModelForList(BaseModel):
    question: str
    correctAnswer: str
    answers: List[str]
    explanation: str
    knowledgeArea: str


class APIPracticeQuestionListModel(BaseModel):
    dbConnectionData: DBConnectionData
    listOfAPIPracticeQuestionModel: List[APIPracticeQuestionModelForList]


@app.get("/Test")
async def test():
    return {"value": "someValue"}


@app.post("/GetOne/{search}/{value}")
async def read_one(search, value, dbConnectionData: DBConnectionData):
    try:
        conn = DBConnection(dbConnectionData.hostName, dbConnectionData.databaseName, dbConnectionData.collectionName)
        return Read(conn, {search: value})
    except Exception as e:
        return {"Error": e.__str__()}


@app.get("/GetAll/{search}/{value}")
async def read_all(search, value, dbConnectionData: DBConnectionData):
    try:
        conn = DBConnection(dbConnectionData.hostName, dbConnectionData.databaseName, dbConnectionData.collectionName)
        return ReadAll(conn, {search: value})
    except Exception as e:
        return {"Error": e.__str__()}

@app.post("/GetAll")
async def read_all(dbConnectionData: DBConnectionData):
    try:
        conn = DBConnection(dbConnectionData.hostName, dbConnectionData.databaseName, dbConnectionData.collectionName)
        return ReadAll(conn, {})
    except Exception as e:
        return {"Error": e.__str__()}

@app.post("/Post")
async def post_one(practiceQuestionModel: APIPracticeQuestionModel):
    try:
        conn = DBConnection(practiceQuestionModel.dbConnectionData.hostName,
                            practiceQuestionModel.dbConnectionData.databaseName,
                            practiceQuestionModel.dbConnectionData.collectionName)
        del practiceQuestionModel.dbConnectionData
        dbModel = ConvertAPIModelToDBModel(practiceQuestionModel)
        return Create(conn, dbModel)

    except Exception as e:
        return {"Error": e.__cause__()}


@app.post("/PostMany")
async def post_many(practiceQuestionListModel: APIPracticeQuestionListModel):
    try:
        conn = DBConnection(practiceQuestionListModel.dbConnectionData.hostName,
                            practiceQuestionListModel.dbConnectionData.databaseName,
                            practiceQuestionListModel.dbConnectionData.collectionName)
        del practiceQuestionListModel.dbConnectionData
        dbModelList = ConvertAPIModelListToDBModelList(practiceQuestionListModel.listOfAPIPracticeQuestionModel)
        return CreateMany(conn, dbModelList)
    except Exception as e:
        return {"Error": e.__str__}


@app.put("/Put/{search}/{value}")
async def put(search, value, practiceQuestionModel: APIPracticeQuestionModel):
    try:
        conn = DBConnection(practiceQuestionModel.dbConnectionData.hostName,
                            practiceQuestionModel.dbConnectionData.databaseName,
                            practiceQuestionModel.dbConnectionData.collectionName)
        del practiceQuestionModel.dbConnectionData
        dbModel = ConvertAPIModelToDBModel(practiceQuestionModel)

        return {"count": UpdateOne(conn, {search: value}, dbModel.__dict__)}

    except Exception as e:
        return {"Error": e.__str__()}


@app.delete("/Delete/{search}/{value}")
async def delete(search, value, dbConnectionData: DBConnectionData):
    try:
        conn = DBConnection(dbConnectionData.hostName, dbConnectionData.databaseName, dbConnectionData.collectionName)
        return {"count": Delete(conn, {search: value})}
    except Exception as e:
        return {"Error": e.__str__()}


@app.delete("/DeleteMany/{search}/{value}")
async def delete_many(search, value, dbConnectionData: DBConnectionData):
    try:
        conn = DBConnection(dbConnectionData.hostName, dbConnectionData.databaseName, dbConnectionData.collectionName)
        return {"count": DeleteMany(conn, {search: value})}
    except Exception as e:
        return {"Error": e.__str__()}

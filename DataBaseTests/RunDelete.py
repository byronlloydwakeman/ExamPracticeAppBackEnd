from Database.CRUD.Delete import DeleteMany
from Database.DBConnection import DBConnection

conn = DBConnection("mongodb://localhost:27017", "exampracticeapp", "pythonexamquestions")

obj = DeleteMany(conn, {"knowledgeArea": "geography"})

from Database.CRUD.Create import Create
from Database.PracticeQuestionSchema import PracticeQuestion
from Database.DBConnection import DBConnection

question = PracticeQuestion("is the moon made of cheese?", "no", ["no", "yes", "obviously", "idk"],
                            "The moon is made of milk and the moon is old so its now cheese", "geography")


conn = DBConnection("mongodb://localhost:27017", "exampracticeapp", "pythonexamquestions")

print(Create(conn, question))
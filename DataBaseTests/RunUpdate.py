from Database.CRUD.Update import UpdateOne
from Database.PracticeQuestionSchema import PracticeQuestion
from Database.DBConnection import DBConnection

newQuestion = PracticeQuestion("is the moon made of cheese?", "idk", ["no", "yes", "obviously", "idk"],
                               "The moon is made of milk and the moon is old so its now cheese", "geography")

conn = DBConnection("mongodb://localhost:27017", "exampracticeapp", "pythonexamquestions")

obj = UpdateOne(conn, {"correctAnswer": "idk"}, {"question": "do I have a small willy", "correctAnswer": "no its huge", "answers": ["no", "yes", "obviously","idk"],"explanation": "The moon is made of milk and the moon is old so its now cheese", "knowledgeArea": "geography"})
print(obj)

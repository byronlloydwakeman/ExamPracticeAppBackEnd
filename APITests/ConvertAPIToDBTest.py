from API.ConvertAPIToDB import ConvertAPIModelToDBModel

someObject = {
    "question": "is the moon made of cheese?",
    "correctAnswer": "yes",
    "answers": [
        "no",
        "yes",
        "obviously",
        "idk"
    ],
    "explanation": "The moon is made of milk and the moon is old so its now cheese",
    "knowledgeArea": "geography"
}

obj = ConvertAPIModelToDBModel(someObject)
print(obj)
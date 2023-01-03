from Database.PracticeQuestionSchema import PracticeQuestion


def ConvertAPIModelToDBModel(APIModel):
    toReturn = PracticeQuestion(APIModel.question, APIModel.correctAnswer,
                                APIModel.answers, APIModel.explanation,
                                APIModel.knowledgeArea)
    return toReturn


def ConvertAPIModelListToDBModelList(APIModelList):
    toReturn = []
    for model in APIModelList:
        toReturn.append(ConvertAPIModelToDBModel(model))

    return toReturn
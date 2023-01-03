def Create(DbConnectionObject, QuestionObject):
    """
    Insert the QuestionObject into the DBConnectionObjects database
    :param DbConnectionObject: an instance of the DBConnectionClass which is connected to a db collection
    :param QuestionObject: an instance of the PracticeQuestionSchema class
    :return: returns the primary key of the new db entry
    """
    return str(DbConnectionObject.collection.insert_one(QuestionObject.__dict__).inserted_id)


def CreateMany(DbConnectionObject, ListOfQuestionObjects):
    listOfIds = []
    for question in ListOfQuestionObjects:
        listOfIds.append(Create(DbConnectionObject, question))

    return listOfIds

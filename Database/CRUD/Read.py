def Read(DbConnectionObject, searchDict):
    dictToReturn = DbConnectionObject.collection.find_one(searchDict)
    dictToReturn["_id"] = str(dictToReturn["_id"])
    return dictToReturn


def ReadAll(DbConnectionObject, searchDict):
    dicts = DbConnectionObject.collection.find(searchDict)
    dicts = list(dicts)
    for el in dicts:
        el["_id"] = str(el["_id"])
    return dicts
def UpdateOne(DbConnection, searchDict, newValue):
    return DbConnection.collection.update_one(searchDict, {"$set" : newValue}).matched_count
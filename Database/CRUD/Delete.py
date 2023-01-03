def Delete(DbConnection, searchDict):
    return DbConnection.collection.delete_one(searchDict).deleted_count


def DeleteMany(DbConnection, searchDict):
    return DbConnection.collection.delete_many(searchDict).deleted_count



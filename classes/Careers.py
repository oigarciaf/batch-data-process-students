
class Careers:
    def __init__(self,name, id=" "):
        self.name=name
        self.__id = id
        self.__collection = "careers"
        
    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id

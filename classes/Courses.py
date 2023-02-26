from classes import DbMongo, data, Students

class Courses:
    def __init__(self,name, id=""):
        self.name = name
        self.__collection = "course"
   
    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id

    def update(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        objStore = { '$set' : self.__dict__ }
        collection.update_one( filterToUse , objStore )

    def delete(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        collection.delete_one( filterToUse )

    @staticmethod
    def get_one(db, id):
        collection = db["name"]
        filterToUse = { '_id' : id }
        result = collection.find_one(filterToUse)
        
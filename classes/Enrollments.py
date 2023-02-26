from classes import DbMongo, data, Students


class Enrollments:
    def __init__(self,  student, course, passed):
        self.student = student
        self.course = course
        self.passed = passed
        self.__collection = "Enrollomen"
    
    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id

        
        

    
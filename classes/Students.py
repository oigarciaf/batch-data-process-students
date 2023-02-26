

class Students:
    def __init__(self, student_id, full_name,age,career):
        self.student_id = student_id 
        self.full_name = full_name
        self.age = age
        self.career = career
        self.__collection = "students"
    
    def create(self, name, account_number, age, career ):
        student = {
            "name":name,
            "account_number":account_number,
            "age": age,
            "career":career,
        }
        result = self.collection.insert_one(student)
        return result.inserted
    
    def save(self, db):
        collection = db[self.__collection]
        result = collection.insert_one(self.__dict__)
        self.__id =  result.inserted_id

    def update(self, db):
        collection = db[self.__collection]
        filterToUse = { '_id' : self.__id }
        objStore = { '$set' : self.__dict__ }
        collection.update_one( filterToUse , objStore )

    

    @staticmethod
    def get_one(db, id):
        collection = db["students"]
        filterToUse = { '_id' : id }
        result = collection.find_one(filterToUse)
        